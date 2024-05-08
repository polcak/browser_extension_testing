import sys
import json
from start_visit.start_pet import test_pet 
import concurrent.futures
import time

def start_native_threaded(exp, browsers, pets, server_config, delay):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for browser in browsers:
                test_pet(exp, browser, pets[browser][0], server_config, delay)
                for pet in pets[browser][1:]:
                    futures.append(
                        executor.submit(test_pet, exp, browser, pet, server_config, delay)
                )
                for future in concurrent.futures.as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Thread error: {e}")

def start_native_interactive(exp, browsers, pets, server_config, delay):
            for browser in browsers:
                for pet in pets[browser]:
                    test_pet(exp, browser, pet, server_config, delay)          

def get_experiment_attributes(data):
    exp = data["experiment_name"]
    browsers = data["browsers"]
    pets = data["pets"]
    delay = data["delay"]
    mode = data["mode"]

    return exp, browsers, pets, delay, mode

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Call as follows: python3 start.py experiment_config_file server_config_file")
        sys.exit(0)

    experiment_config = sys.argv[1]
    with open(experiment_config) as f:
        data = json.load(f)
        exp, browsers, pets, delay, mode = get_experiment_attributes(data)

    server_config = sys.argv[2]

    if mode == "threaded":
        try:
            print("Starting the visits in threaded mode.")
            start_native_threaded(exp, browsers, pets, server_config, delay)
        except:
            print("Please give valid json files as input. See vm_all.json and vm_server.json as the template.")
            sys.exit(0)
    if mode == "interactive":
        try:
            print("Starting the visits in interactive mode.")
            start_native_interactive(exp, browsers, pets, server_config, delay)
        except:
            print("Please give valid json files as input. See vm_all.json and vm_server.json as the template.")
            sys.exit(0)


