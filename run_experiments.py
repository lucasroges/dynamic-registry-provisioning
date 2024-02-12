# Importing Python libraries
from subprocess import Popen, DEVNULL, TimeoutExpired

import itertools
import os

NUMBER_OF_PARALLEL_PROCESSES =  os.cpu_count()

SEED = "1"

def run_simulation(algorithm, dataset, replicas):
    """Executes the simulation with the specified parameters.

    Args:
        algorithm (str): Algorithm to be executed.
        dataset (str): Dataset to be used.
        replicas (int): Number of replicas to be used in the resource aware dynamic strategy.
    """
    cmd = (
        f"poetry run python -m simulation -a {algorithm} -d {dataset} -s {SEED} -n 3600 -r {replicas}"
        if replicas is not None
        else f"poetry run python -m simulation -a {algorithm} -d {dataset} -s {SEED} -n 3600"
    )
    print(f"    cmd = {cmd}")

    return Popen([cmd], stdout=DEVNULL, stderr=DEVNULL, shell=True)


# Parameters
algorithms = [
    ("central", "central"),
    ("community", "community12p"),
    ("community", "community25p"),
    ("p2p", "p2p"),
    ("dynamic", "p2p"),
    ("resource_aware_dynamic", "p2p", 1),
    ("resource_aware_dynamic", "p2p", 2),
    ("resource_aware_dynamic", "p2p", 3),
    ("resource_aware_dynamic", "p2p", 4),
]

variations = [
    "nodes=100;unique_images=08",
    "nodes=100;unique_images=32",
    "nodes=196;unique_images=16",
    "nodes=196;unique_images=64",
]

print(f"GENERATING {len(algorithms) * len(variations)} COMBINATIONS")

# Generating list of combinations with the parameters specified
combinations = list(
    itertools.product(
        algorithms,
        variations,
    )
)

processes = []

# Executing simulations and collecting results
print(f"EXECUTING {len(combinations)} COMBINATIONS")
for i, parameters in enumerate(combinations, 1):
    # Parsing parameters
    algorithm = parameters[0]
    variation = parameters[1]
    number_of_nodes = variation[6:9]
    number_of_unique_images = variation[24:]
    replicas = algorithm[2] if len(algorithm) == 3 else None

    print(f"\t[Execution {i}]")
    print(f"\t\t[algorithm={algorithm[0]}] [nodes={number_of_nodes}] [unique_images={number_of_unique_images}]")

    # Executing algorithm
    proc = run_simulation(
        algorithm=algorithm[0],
        dataset=f"datasets/{algorithm[1]}\;nodes\={number_of_nodes}\;unique_images={number_of_unique_images}.json",
        replicas=replicas,
    )

    processes.append(proc)

    while len(processes) >= NUMBER_OF_PARALLEL_PROCESSES:
        for proc in processes:
            try:
                proc.wait(timeout=1)

            except TimeoutExpired:
                pass

            else:
                processes.remove(proc)
                print(f"PID {proc.pid} finished")

    print(f"{len(processes)} processes running in parallel")
