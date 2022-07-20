# Getting started with MLflow

**TLDR;** this repo contains some starter code in order to become familiar with [MLflow Tracking](https://www.mlflow.org/docs/latest/tracking.html) and [MLflow Model Registry](https://www.mlflow.org/docs/latest/model-registry.html).

This is a companion repo to this Medium blog post: [Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2](https://medium.com/@rafaelpierre/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc)

## Dependencies

* Python 3.8.7
* Visual Studio Code
    * Jupyter Extension

## Quickstart

Please follow the steps described in this [Medium post](https://medium.com/@rafaelpierre/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc).

## Workflow Steps

* In the `01_train_register` notebook, we create multiple `scikit-learn` model runs and log the resulting models in MLflow
* In `02_register_model`:
    * We browse the runs from the previous step and select one of them to register its model into Model Registry
    * Next, we run an inference test with this model, in order to guarantee that it works
    * Finally, we promote this model to **Staging**

## Additional details

* For simplicity purposes, for the **Jupyter** version we are using MLflow with a SQLite backend. This is not recommended in a production setting, but it is good enough for the sake of this example.

## References

* [MLflow Website](https://mlflow.org/)
* [MLflow Github Repo](https://www.github.com/mlflow/mlflow)
* [MLflow Model Registry on Databricks](https://docs.databricks.com/applications/mlflow/model-registry.html)
