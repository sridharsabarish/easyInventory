PHONY := tests all virtualenv 
.PHONY : tests all virtualenv
tests: 
	python3 -m pytest

all: virtualenv test
	echo "Starting the Inventory app..."
	python app.py
	deactivate

virtualenv:
	sh ../bin/activate
# 	python3  -m pip install requirements.txt


