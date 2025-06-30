#! /bin/bash

echo "Building the docker image"
docker build -t inventory-flask .
echo "Docker image built with tag: inventory-flask"

