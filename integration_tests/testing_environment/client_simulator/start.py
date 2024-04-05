import sys
import json
from start_visit.start_pet import test_pet 

def start_native(exp, os, configs, browsers, pets, repeats, exp_config, server_config):
    for os in oses:
        for config in configs[os]:
            for browser in browsers:
                for pet in pets[browser]:
                    test_pet(exp, os, config, browser, pet, repeats, exp_config, server_config)

def get_experiment_attributes(data):
    exp = data["experiment_name"]
    oses = data["oses"]
    configs = data["configs"]
    browsers = data["browsers"]
    pets = data["pets"]
    repeats = data["repeats"]
    return exp, oses, configs, browsers, pets, repeats

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Call as follows: python start.py experiment_config_file server_config_file")
        print("An example: python start.py example_configs/vm_all.json example_configs/vm_server.json \n Or python start.py example_configs/native_mac.json example_configs/native_server.json")
        sys.exit(0)

    experiment_config = sys.argv[1]
    with open(experiment_config) as f:
        data = json.load(f)
        exp, oses, configs, browsers, pets, repeats = get_experiment_attributes(data)

    server_config = sys.argv[2]

    try:
        start_native(exp, oses, configs, browsers, pets, repeats, experiment_config, server_config)
    except:
        print("Please give valid json files as input. See vm_all.json and vm_server.json as the template.")
        sys.exit(0)

