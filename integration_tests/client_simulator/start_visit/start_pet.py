from .start_browser import Browser
import sys                  # for command line arguments
import time                 # for sleeping for some duration
import json
import os as oslib


def test_pet(exp, browser, pet, server_config, delay):

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

        unit = sim_browser(browser, pet, proxy_setting)

        if "NBS" in pet[0] or "DLS" in pet[0]:
            sys.stdout.write("\n")
            sys.stdout.flush()
            cleanup_browser(unit)
            return

        time.sleep(5)
        print("visit sites")
        html_args = "?exp="+exp+"&browser="+browser+"&pet="+'-'.join(pet)
        fp_site = fp_sites[0] + html_args
        unit.visit_sites([fp_site], delay)
        sys.stdout.write("\n")
        sys.stdout.flush()

        cleanup_browser(unit)
    except Exception as e:
        print(e)

def sim_browser(browser, pet, proxy_setting):
    b = Browser(browser, pet, proxy_setting)
    return b

def check(unit, fp_list):
    unit.visit_sites(fp_list)

def cleanup_browser(unit):
    unit.quit()

if __name__ == '__main__':
    EXP = sys.argv[1]
    BROWSER = sys.argv[2]
    PET = sys.argv[3]
    SERVER_CONFIG = sys.argv[4] 

    test_pet(EXP, BROWSER, PET, SERVER_CONFIG)
