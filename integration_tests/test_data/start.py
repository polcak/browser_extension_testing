#
#  JavaScript Restrictor is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
#  Copyright (C) 2020  Martin Bednar
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import pytest
import re
import os
import datetime
import sys
import logging

from store_values import create_browser_data
from shared_set import set_shared_noaddon, set_shared_addonRun, set_shared_level, set_shared_browser, set_shared_addonsInstalled, get_shared_addonsInstalled

def sort_extensions(addonsTested):
    extensions = addonsTested.split("-")
    sorted_extensions = sorted(extensions)
    sorted_addonsTested = '_'.join(sorted_extensions)
    return sorted_addonsTested

## Main module - it starts and control testing.
#
#  To start testing call this module from PowerShell, CommandPrompt, Terminal or Bash: python start.py
#  For every browser and for every jsr_level defined in configuration.py set of all tests is run.
def main():

    generated_t = str(datetime.datetime.now(datetime.timezone.utc))
    test_start = generated_t.replace(" ", "--").replace(":", "-").replace(".", "-")
    test_date = r"\d{4}-\d{2}-\d{2}"
    test_date_timestamp = re.search(test_date, test_start).group(0)

    subfolders = [f for f in os.listdir("/usr/app/src/fingerprinting_server/outputs/" + test_date_timestamp) if os.path.isdir(os.path.join("/usr/app/src/fingerprinting_server/outputs/" + test_date_timestamp, f))]
    
    for subfolder in subfolders:
        print('=' * os.get_terminal_size().columns)

        browser_name = subfolder.split('_')[-1]
        browser_data = create_browser_data(test_date_timestamp + "/" + subfolder)  

        if not browser_data:
            print("Integration testing skipped.")
            exit(0)

        print("Integration testing for JShelter starting.")
        print("Testing log files in directory: ", test_date_timestamp + "/" + subfolder)
        print('=' * os.get_terminal_size().columns)
        print("Browser currently tested:", browser_name)

        if "special" in browser_name:
            browser_name = "special"
        else:
            browser_name = browser_name.split("=")[0]
    
        no_addon = browser_data[0]
        set_shared_browser(browser_name)
        set_shared_noaddon(no_addon)


        for value in browser_data[1:]:     
                sorted_addonsTested = sort_extensions(value.addons)      
                set_shared_addonsInstalled(sorted_addonsTested)           
                if "JS" in sorted_addonsTested:
                    js_level = re.search(r'\d+', sorted_addonsTested).group(0)
                    print("JShelter level tested:", js_level)
                    set_shared_level(js_level)
                else:
                    set_shared_level(0)               
                set_shared_addonRun(value)     
                print("Addons installed this run: ", get_shared_addonsInstalled())
                      
                pytest.main(args=['--capture=tee-sys' ])                  



if __name__ == "__main__":
    main()
    print('=' * os.get_terminal_size().columns)
    print("Integration testing ended.")
