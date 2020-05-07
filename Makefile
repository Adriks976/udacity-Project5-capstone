## The Makefile includes instructions on environment setup and lint tests
# Create and activate a virtual environment
# Install dependencies in requirements.txt
# Dockerfile should pass hadolint
# app.py should pass pylint
# (Optional) Build a simple integration test

setup:
	# Create python virtualenv & source it
	# source ~/.devops/bin/activate
	python3 -m venv ~/.capstone
	source ~/.capstone/bin/activate

install:
	# This should be run from inside a virtualenv
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

test:
	# Additional, optional, tests could go here
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	# This is linter for Dockerfiles
	source ~/.capstone/bin/activate
	hadolint Dockerfile
	# This is a linter for Python source code linter: https://www.pylint.org/
	# This should be run from inside a virtualenv
	pylint --disable=R,C,W1203,W1202 app/app.py --extension-pkg-whitelist=cv2

run_docker:
	./tools/run_docker.sh

upload_docker:
	./upload_docker.sh

run_kubernetes:
	./run_kubernetes.sh

all: install lint test
