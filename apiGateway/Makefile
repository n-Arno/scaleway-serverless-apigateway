deploy: node_modules
	./helper.py myService kong/kong.yml
	serverless deploy

node_modules:
	npm i

remove:
	- serverless remove

dist-clean: remove
	- rm -rf node_modules package-lock.json
