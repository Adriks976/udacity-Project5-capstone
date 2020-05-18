# udacity-Project5-capstone
Udacity Devops nanodegree Capstone project


## Setup infrastructure

This project uses cloudformation to create an EKS cluster on AWS.

To create the cluster and nodes:

```bash
./do_stack.sh create network
./do_stack.sh create eks
./do_stack.sh create eks-nodes
```

With these following steps you have now a cluster deployed.

## Run application

- `make setup` to setup the virtualenv 
- `make install`to install requirements for the app
- `make lint` to check lint docker and python app
- `make run_docker` if you want to run the application quicly on your local docker.
- `cd app && python app.py` to run app locally.