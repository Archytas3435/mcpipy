#!/usr/bin/env bash

sudo apt-get update -y

sudo apt-get install openjdk-8-jdk -y

java -version

sudo apt install software-properties-common -y 

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update -y

sudo apt install python3.8 -y

python --version
