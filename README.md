scaleway-serverless-apigateway
==============================

This example demonstrate how to setup kong DB-less as API Gateway for serverless functions in Scaleway ecosystem.

Note: this upgraded version use serverless-compose. It needs an update to the scaleway provider to support `serverless info`: https://github.com/scaleway/serverless-scaleway-functions/issues/71

First, 2 serverless functions are deployed and then kong is deployed as a serverless container.

A small python helper (included in the docker image) will populate the kong.yml with the functions endpoints when starting the container.

Once fully deployed, you can access the first function through the apigateway directly (/) and the second function through /second.

Pre-requisites:
- gnu make
- serverless cli (will get serverless compose through `npm i`)
- SCW_* environment variables set (SCW_SECRET_KEY, etc...)
