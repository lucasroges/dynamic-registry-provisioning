# Dynamic Registry Provisioning

TBD.

## Configuring the environment

This project was configured with Poetry to manage its dependencies. Please ensure you have Python 3.10+ and Poetry installed. If not, you can install Poetry following the instructions [here](https://python-poetry.org/docs/#installation).

After installing these tools, you can install the dependencies of the project with the following command:


```sh
poetry install
```

## Building the datasets

To build the necessary datasets to replicate the paper's experiments, run the following commands at the repository root folder:

```sh
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=4.json -o central\;nodes=100\;users_per_app=4 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=4.json -o central\;nodes=196\;users_per_app=4 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=4.json -o community12p\;nodes=100\;users_per_app=4 -rp community -c 3 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=4.json -o community25p\;nodes=100\;users_per_app=4 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=4.json -o community12p\;nodes=196\;users_per_app=4 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=4.json -o community25p\;nodes=196\;users_per_app=4 -rp community -c 12 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=4.json -o p2p\;nodes=100\;users_per_app=4 -rp p2p >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=4.json -o p2p\;nodes=196\;users_per_app=4 -rp p2p >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=16.json -o central\;nodes=100\;users_per_app=16 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=16.json -o central\;nodes=196\;users_per_app=16 -rp central >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=16.json -o community12p\;nodes=100\;users_per_app=16 -rp community -c 3 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=16.json -o community25p\;nodes=100\;users_per_app=16 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=16.json -o community12p\;nodes=196\;users_per_app=16 -rp community -c 6 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=16.json -o community25p\;nodes=196\;users_per_app=16 -rp community -c 12 >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=100\;users_per_app=16.json -o p2p\;nodes=100\;users_per_app=16 -rp p2p >> create_datasets.log && \
poetry run python -m datasets -s 1 -i datasets/inputs/nodes=196\;users_per_app=16.json -o p2p\;nodes=196\;users_per_app=16 -rp p2p >> create_datasets.log
```

## Running the experiments

To run the experiments, navigate to the repository root folder and run the following command:

```sh
poetry run python run_experiments.py
```

Although the script runs a few cases in parallel, we recommend to run the script in background because it might take a while to complete all the executions.

## Getting the results

After the executions finished, the logs are available at the `logs` directory. To analyze the results, run the `analysis.ipynb` notebook. You can modify this notebook to explore different metrics and datasets for various scenarios.
