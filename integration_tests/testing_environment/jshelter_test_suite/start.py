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

from store_values import create_browser_data
from shared_set import set_shared_noaddon, set_shared_addonRun, set_shared_level, set_shared_browser, set_shared_addonsInstalled, get_shared_addonsInstalled

## Main module - it starts and control testing.
#
#  To start testing call this module from PowerShell, CommandPrompt, Terminal or Bash: python start.py
#  For every browser and for every jsr_level defined in configuration.py set of all tests is run.
def main():
    browser_data = create_browser_data()  

    if not browser_data:
        print("Integration testing skipped.")
        exit(0)

    print("Integration testing for JShelter starting.")
    print("===============================================================================================================================================================================================================================================================================")

    for browser, values in browser_data.items():
        no_addon = values[0]
        set_shared_browser(browser)
        set_shared_noaddon(no_addon)
        
        
        for value in values[1:]:
            print("Browser currently tested:", browser)
            set_shared_addonsInstalled(value.addons)
            
            if "JS" in value.addons:
                js_level = re.search(r'\d+', value.addons).group(0)
                print("JShelter level tested:", js_level)
                set_shared_level(js_level)
                
            set_shared_addonRun(value)
            
            
            print(get_shared_addonsInstalled())
            pytest.main(['-s'])


if __name__ == "__main__":
    main()
    print("===============================================================================================================================================================================================================================================================================")
    print("Integration testing for JShelter ended.")
