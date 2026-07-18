

PHONY := tests all virtualenv 
.PHONY : tests all virtualenv
tests: stop
	python3 -m pytest && python3 app.py

all: virtualenv tests
	echo "Starting the Inventory app..." && python app.py
	deactivate

virtualenv:
	sh ../bin/activate
# 	python3  -m pip install requirements.txt


image:
	docker build -t inventory-app .
	docker run -p 5001 inventory-app
stop:
	docker stop inventory-app || true
