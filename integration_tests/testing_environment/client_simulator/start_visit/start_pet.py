from .start_browser import Browser
import sys                  # for command line arguments
import time                 # for sleeping for some duration
import json
import ast
import os as oslib
from time import localtime, strftime


def test_pet(exp, browser, pet, server_config):

    try:
        def get_server_attributes(data):
            fp_sites = data["fp_sites"]
            use_socks5 = data["socks5_proxy"]
            proxy_setting = None
            if use_socks5:
                proxy_setting = data["proxy_setting"]

            return fp_sites, proxy_setting

        cwd = oslib.path.dirname(oslib.path.abspath(__file__))

        with open(oslib.path.join(cwd, "../", server_config)) as f:
            data = json.load(f)
            fp_sites, proxy_setting = get_server_attributes(data)

        print("configure the browser")
        unit = sim_browser(browser, pet, proxy_setting)

        if "userSettings" in pet[0]:
            sys.stdout.write("\n")
            sys.stdout.flush()
            print("exit")
            cleanup_browser(unit)
            return

        time.sleep(5)
        print("visit sites")
        html_args = "?exp="+exp+"&browser="+browser+"&pet="+'_'.join(pet)
        fp_site = fp_sites[0] + html_args
        unit.visit_sites([fp_site])
        sys.stdout.write("\n")
        sys.stdout.flush()

        print("exit")
        cleanup_browser(unit)
    except Exception as e:
        if pet == "tor":
            print("If native, first launch Tor application locally before running the script.\n This is to get SOCKS host running on port 9150.")
        print(e)

def sim_browser(browser, pet, proxy_setting):
    b = Browser(browser, pet, proxy_setting)
    return b

def check(unit, fp_list):
    unit.visit_sites(fp_list)

def cleanup_browser(unit):
    unit.quit()

if __name__ == '__main__':
    if(len(sys.argv) != 9):
        print("Call as follows: python start_pet.py <exp> <browser> <pet> <server_config>")
        sys.exit(0)
    EXP = sys.argv[1]
    BROWSER = sys.argv[2] # "firefox" or "chrome"
    PET = sys.argv[3]
    SERVER_CONFIG = sys.argv[4] # "vm_server.json" etc

    test_pet(EXP, BROWSER, PET, SERVER_CONFIG)
