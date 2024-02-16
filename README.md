# Dynamic Registry Provisioning

This repository contains the material related to my Master's thesis.

The aim of this work is to dynamically provision and deprovision P2P registries (cache-based registries) in edge computing infrastructures to minimize the latency between users and applications, the provisioning time of application, and the infrastructure resource usage.

## Configuring the environment

This project was configured with Poetry to manage its dependencies. Please ensure you have Python 3.10+ and Poetry installed. If not, you can install Poetry following the instructions [here](https://python-poetry.org/docs/#installation).

After installing these tools, you can install the dependencies of the project with the following command:

```sh
poetry install
```

## Building the datasets

To build the necessary datasets to replicate the paper's experiments, navigate to the repository root folder and run the following command:

```sh
sh create_datasets.sh
```

## Running the experiments

To run the experiments, navigate to the repository root folder and run the following command:

```sh
poetry run python run_experiments.py
```

Although the script runs a few cases in parallel, we recommend to run the script in background because it might take a while to complete all the executions.

## Getting the results

After the executions finished, the logs are available at the `logs` directory. To analyze the results, run the `analysis.ipynb` notebook. You can modify this notebook to explore different metrics and datasets for various scenarios.
