deploy: node_modules
	serverless deploy

node_modules:
	npm i
	rm -rf node_modules/serverless-scaleway-functions
	git -C node_modules clone -b aws-like-info https://github.com/n-Arno/serverless-scaleway-functions
	cd node_modules/serverless-scaleway-functions && npm i && cd -

clean: remove

remove:
	- serverless remove --service=apiGateway
	- serverless remove --service=myApp

dist-clean: remove
	- rm -rf node_modules package-lock.json
	- find . -name .serverless -exec rm -rf "{}" +
