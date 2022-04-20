scaleway-serverless-apigateway
==============================

This example demonstrate how to setup kong DB-less as API Gateway for serverless functions in Scaleway ecosystem.

First, 2 serverless functions are deployed and then kong is deployed as a serverless container.

A small python helper will populate the kong.yml with the functions endpoints before building/deploying the container.

Once fully deployed, you can access the first function through the apigateway directly and the second function through /second.

Pre-requisites:
- gnu make
- serverless cli
- python3
- pyyaml and requests python modules
- SCW_* environment variables set (is SCW_SECRET_KEY, etc...)
