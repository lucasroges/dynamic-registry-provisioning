# Importing Python libraries
from subprocess import Popen, DEVNULL, TimeoutExpired

import itertools
import os

NUMBER_OF_PARALLEL_PROCESSES =  os.cpu_count() - 1

SEED = "1"

def run_simulation(algorithm, dataset, replicas):
    """Executes the simulation with the specified parameters.

    Args:
        algorithm (str): Algorithm to be executed.
        dataset (str): Dataset to be used.
        replicas (int): Number of replicas to be used.
    """
    cmd = f"poetry run python -m simulation -a {algorithm} -d {dataset} -s {SEED} -n 3600 -r {replicas}"
    print(f"    cmd = {cmd}")

    return Popen([cmd], stdout=DEVNULL, stderr=DEVNULL, shell=True)


# Parameters
algorithms = [
    ("resource_aware_dynamic", "p2p"),
]

number_of_nodes = [
    100,
    196
]

users_per_apps = [4, 16]

replicas = [1, 2, 3, 4]

print(f"GENERATING {len(algorithms) * len(number_of_nodes) * len(users_per_apps) * len(replicas)} COMBINATIONS")

# Generating list of combinations with the parameters specified
combinations = list(
    itertools.product(
        algorithms,
        number_of_nodes,
        users_per_apps,
        replicas,
    )
)

processes = []

# Executing simulations and collecting results
print(f"EXECUTING {len(combinations)} COMBINATIONS")
for i, parameters in enumerate(combinations, 1):
    # Parsing parameters
    algorithm = parameters[0]
    number_of_nodes = parameters[1]
    users_per_app = parameters[2]
    replicas = parameters[3]

    print(f"\t[Execution {i}]")
    print(f"\t\t[algorithm={algorithm[0]}] [number_of_nodes={number_of_nodes}] [users_per_app={users_per_app}] [replicas={replicas}]")

    # Executing algorithm
    proc = run_simulation(
        algorithm=algorithm[0],
        dataset=f"datasets/{algorithm[1]}\;nodes={number_of_nodes}\;users_per_app={users_per_app}.json",
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
