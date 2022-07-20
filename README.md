# Getting started with MLflow

**TLDR;** this repo contains some starter code in order to become familiar with [MLflow Tracking](https://www.mlflow.org/docs/latest/tracking.html) and [MLflow Model Registry](https://www.mlflow.org/docs/latest/model-registry.html).

This is a companion repo to this Medium blog post: Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2

## Dependencies

* Python 3.8.7
* Visual Studio Code
    * Jupyter Extension

## Quickstart

* Clone this repo: `git clone https://github.com/rafaelvp-db/mlflow-getting-started.git`
* From the local repo folder:
    * Create a virtual environment with `python -m venv .venv`
    * Run `make init` to install the required packages and configure pre-commit hooks
* Run the notebooks from the `databricks` or `jupyter` folder
    * If you have a non-community Databricks workspace, feel free to link this repo to your workspace and run the notebooks in the `databricks` folder
    * If you don't have a Databricks environment and want to run the code locally, please run the notebooks in the `jupyter` folder

## Workflow Steps

* In the `01_train_register` notebook, we create multiple `scikit-learn` model runs and log the resulting models in MLflow
* In `02_register_model`:
    * We browse the runs from the previous step and select one of them to register its model into Model Registry
    * Next, we run an inference test with this model, in order to guarantee that it works
    * Finally, we promote this model to **Staging**

## Additional details

* For simplicity purposes, we are using MLflow with a SQLite backend. This is not recommended in a production setting, but it is good enough for the sake of this example.

## References

* [MLflow Website](https://mlflow.org/)
* [MLflow Github Repo](https://www.github.com/mlflow/mlflow)
* [MLflow Model Registry on Databricks](https://docs.databricks.com/applications/mlflow/model-registry.html)
