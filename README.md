# udacity-Project5-capstone
Udacity Devops nanodegree Capstone project


## About the app

This app is a quick project using flask and AWS Textract.

You can submit a png or jpeg containing text, like a scan document.
After uploading it, the text will be extracted.

This is a quick demo :) There's no beautiful interface nor a good output for the extracted text.

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

## Kubernetes

You can find deployment and service files for Kubernetes.
It will setup a loadbalancer endpoint to connect to the application

## Access the demo 

http://a1f9fbbaf45ee435697ed81d2f5cab4d-1329538271.eu-west-1.elb.amazonaws.com/

This endpoint will be available only during review time from Udacity.