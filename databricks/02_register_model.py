# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Registering our Model
# MAGIC ### Getting our best runs

# COMMAND ----------

import mlflow
from mlflow.tracking import MlflowClient
import os

# COMMAND ----------

#Get experiment
experiment_name = "/Shared/elastic_net_experiment"
experiment = mlflow.get_experiment_by_name(experiment_name)
experiment

# COMMAND ----------

# Get experiment runs
client = MlflowClient()
runs = client.search_runs(experiment_ids = [experiment.experiment_id])
display(runs)

# COMMAND ----------

#Get the best metrics value and use it to find the best run

metrics = [run.data.metrics["rmse"] for run in runs]
best_rmse = min(metrics)
best_run = [run for run in runs if run.data.metrics["rmse"] == best_rmse][0]
best_run.info

# COMMAND ----------

# Register the model from the best run and log it

model_name = "my_enet_model"
mlflow.set_experiment(experiment_name = experiment_name)
model_uri = f"runs:/{best_run.info.run_id}/model"
model_version = mlflow.register_model(model_uri = model_uri, name = model_name)
model_version

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Loading our model artifact

# COMMAND ----------

model = client.get_registered_model(name = model_name)
model

# COMMAND ----------

model_artifact = mlflow.sklearn.load_model(model_uri)
model_artifact

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # Running inference

# COMMAND ----------

from sklearn import datasets
import numpy as np

diabetes = datasets.load_diabetes()
data = diabetes.data
pred = model_artifact.predict(data)
pred

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Adding metadata to our model

# COMMAND ----------

client.set_model_version_tag(model_name, model_version.version, key = "prediction_works", value = "true")

# COMMAND ----------

model_version_info = client.get_model_version(model_name, model_version.version)
model_version_info.tags

# COMMAND ----------

# MAGIC %md
# MAGIC ## Promoting our model to Staging
# MAGIC 
# MAGIC We are happy with our model (for now), so let's promote it to Staging

# COMMAND ----------

client.transition_model_version_stage(model_name, model_version.version, stage = "Staging")

# COMMAND ----------

model_version_info = client.get_model_version(model_name, model_version.version)
model_version_info.current_stage

# COMMAND ----------


