#!/bin/bash

action=$1
stack=$2

if [[ "$action" =~ ^(create|update)$ ]]; then
    echo "You will perform $action for stack $stack"

    aws cloudformation ${action}-stack \
        --stack-name $2 \
        --template-body file://stacks/$2.yml \
        --parameters file://parameters/$2.json \
        --region=eu-west-1 \
        --capabilities CAPABILITY_NAMED_IAM
    
    echo "Done"
    exit

elif [[ "$action" =~ ^(delete)$ ]]; then
    echo "You will perform $action for stack $stack"

    aws cloudformation ${action}-stack \
    --stack-name $2 \
    --region=eu-west-1
    echo "Done"
    exit
else
    echo "Not a valid action"
    exit
fi
