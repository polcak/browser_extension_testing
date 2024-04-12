#
#  JShelter is a browser extension which increases level
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

from time import sleep

from selenium import webdriver

from web_browser_type import BrowserType
from configuration import Config


## Find URL of JShelter option page after JShelter was installed to browser.
#def find_options_jsr_page_url(driver, browser_type):
#    sleep(1)
    # KNOWN ISSUE: Tab in browser is sometimes not switched by this command.
    # And it leads to error and stopping execution of script. It is driver's issue.
    # Workaround for this issue is wait a while before and after tabs switching.
#    driver.switch_to.window(driver.window_handles[-1])
#    sleep(1)
#    if browser_type == BrowserType.CHROME:
        #driver.get('chrome://system/')
#        driver.get("chrome-extension://ammoloihpcbognfddfjcljgembpibcmb/options.html")
        #WebDriverWait(driver, 60).until(
        #    ec.presence_of_element_located((By.ID, 'extensions-value-btn'))
        #)
#        driver.find_element_by_id('extensions-value-btn').click()
#        for elem in driver.find_element_by_id('extensions-value').text.splitlines():
#            if 'JavaScript Restrictor' in elem:
#                return "chrome-extension://" + elem.split(':')[0][:-1] + "/options.html"

def set_jsr_level_firefox(driver, level):
    driver.get("about:debugging#/runtime/this-firefox")
    sleep(3)
    element = driver.find_element("xpath", "//span[@title='JShelter']")

    parent_li = element.find_element("xpath", "./..")

    uuid_element = parent_li.find_element("xpath","./section/dl/div[@class='fieldpair'][2]/dd")
    uuid = uuid_element.text
    driver.get(f"moz-extension://{uuid}/options.html")
    sleep(3)
    select_level = driver.find_element("id", "level-" + str(level))
    select_level.click()

## Set JShelter level in web browser.
def set_jsr_level_chrome(driver, level):
    #options_page = find_options_jsr_page_url(driver, browser_type)
    driver.get("chrome-extension://ammoloihpcbognfddfjcljgembpibcmb/options.html")
    sleep(5)
    driver.find_element("id", "level-" + str(level))


## Create web browser driver and start web browser.
def create_driver(browser_type, with_jsr, jsr_level):
    tested_extensions = Config._extensions_to_test
    if browser_type == BrowserType.CHROME:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')   
        chrome_options.add_argument('--ignore-certificate-errors')   
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--enable-javascript")
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
        chrome_options.browserName = 'chrome'
        #d = DesiredCapabilities.CHROME
        #d['browserName'] = 'chrome'
        #d['javascriptEnabled'] = True
        #d['loggingPreferences'] = {'browser': 'ALL'}

    if with_jsr:
        if browser_type == BrowserType.CHROME:
            extension_paths = Config._extensions_dict_chrome
            for extension in tested_extensions:
                print("installed ", Config._extensions_for_chrome_path + extension_paths[extension])
                chrome_options.add_extension(Config._extensions_for_chrome_path + extension_paths[extension])
                

    driver = webdriver.Remote(
        command_executor='http://' + Config.grid_server_ip_address + ':4444/wd/hub',
        #desired_capabilities=d,
        options=chrome_options)

    if with_jsr:
        set_jsr_level_chrome(driver, jsr_level)

    return driver
