.PHONY: env clean

env:
	export SYSTEM_VERSION_COMPAT=1 && \
	source .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install wheel && \
	pip install -r requirements.txt && \
	pre-commit install

config:
	git config --local include.path ../.gitconfig

init: env config

clean:
	rm -rf notebooks/jupyter/mlflow && rm -rf notebooks/jupyter/mlruns && rm -rf jupyter/mlruns.db

