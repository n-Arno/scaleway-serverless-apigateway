scaleway-serverless-apigateway
==============================

This example demonstrate how to setup kong DB-less as API Gateway for serverless functions in Scaleway ecosystem.

Note: this upgraded version use serverless-compose. It requires at least 0.4.0 version of the Scaleway Serverless Framework plugin.

First, 2 serverless functions are deployed and then kong is deployed as a serverless container.

The outputs of the first deployment are used as environment variables in the second one to populate the kong.yml template.

Once fully deployed, you can access the first function through the apigateway directly (/) and the second function through /orders.

Pre-requisites:
- gnu make
- serverless cli (will get serverless compose through `npm i`)
