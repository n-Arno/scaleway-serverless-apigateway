all:
	make -C myService deploy
	make -C apiGateway deploy

clean:
	- make -C apiGateway remove
	- make -C myService remove

dist-clean:
	- make -C apiGateway dist-clean
	- make -C myService dist-clean
