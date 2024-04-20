import sys
import json
from start_visit.start_pet import test_pet 

def start_native(exp, browsers, pets, server_config):
            for browser in browsers:
                for pet in pets[browser]:
                    test_pet(exp, browser, pet, server_config)

def get_experiment_attributes(data):
    exp = data["experiment_name"]
    browsers = data["browsers"]
    pets = data["pets"]

    return exp, browsers, pets

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Call as follows: python3 start.py experiment_config_file server_config_file")
        sys.exit(0)

    experiment_config = sys.argv[1]
    with open(experiment_config) as f:
        data = json.load(f)
        exp, browsers, pets = get_experiment_attributes(data)

    server_config = sys.argv[2]

    try:
        start_native(exp, browsers, pets, server_config)
    except:
        print("Please give valid json files as input. See vm_all.json and vm_server.json as the template.")
        sys.exit(0)

