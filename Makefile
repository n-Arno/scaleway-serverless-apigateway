deploy: node_modules
	serverless deploy

node_modules:
	npm i

remove:
	- serverless remove --service=apiGateway
	- serverless remove --service=myService

dist-clean: remove
	- rm -rf node_modules package-lock.json
	- find . -name .serverless -exec rm -rf "{}" +
