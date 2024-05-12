#!/bin/bash
client_config="./example_configs/client.json"
server_config="./example_configs/server.json"

nohup python3 fingerprinting_server/run.py > server.log 2>&1 &  

cd client_simulator

python3 start.py "$client_config" "$server_config"

integration_testing=$(jq -r '.integration_testing' "$client_config")

if [ "$integration_testing" = "true" ]; then
    cd ../test_data
    python3 start.py
fi