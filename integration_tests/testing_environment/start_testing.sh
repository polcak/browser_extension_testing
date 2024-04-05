#!/bin/bash
nohup python3 fingerprinting_server/run.py > server.log 2>&1 &  

cd client_simulator

python3 start.py ./example_configs/client.json ./example_configs/server.json

cd ../jshelter_test_suite

python3 start.py