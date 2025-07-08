
PHONY := all virtualenv


all: virtualenv
	echo "Starting the Inventory app..."
	python3 app.py
	deactivate

virtualenv:
	sh ../bin/activate