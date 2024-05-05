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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration import Config


def set_jsr_level_firefox(driver, level):
    driver.get("about:debugging#/runtime/this-firefox")
    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(("xpath", "//span[@title='JShelter']"))
                )

    parent_li = element.find_element("xpath", "./..")

    uuid_element = parent_li.find_element("xpath","./section/dl/div[@class='fieldpair'][2]/dd")
    uuid = uuid_element.text
    driver.get(f"moz-extension://{uuid}/options.html")
    sleep(3)
    select_level = driver.find_element("id", "level-" + str(level))
    select_level.click()

## Set JShelter level in web browser.
def set_jsr_level_chrome(driver, level):
    extension_id = None

    driver.get("chrome://extensions/")
    manager = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(("xpath", "/html/body/extensions-manager"))
                )
    manager_shadow_root = driver.execute_script('return arguments[0].shadowRoot', manager)
    toolbar = manager_shadow_root.find_element("css selector", "#toolbar")
    toggle_shadow_root = driver.execute_script('return arguments[0].shadowRoot', toolbar)
    dev_mode_toggle = toggle_shadow_root.find_element("css selector",'cr-toggle#devMode')
    dev_mode_toggle.click()
    sleep(1)
    container = manager_shadow_root.find_element("css selector", "#container")
    view = container.find_element("css selector", "#viewManager")
    items = view.find_element("css selector", "#items-list")
    items_shadow_root = driver.execute_script('return arguments[0].shadowRoot', items)
    items_container = items_shadow_root.find_element("css selector", "#content-wrapper > div:nth-child(4)")
    extensions_items = items_container.find_elements("tag name","extensions-item")
    for item in extensions_items:
        item_shadow_root = driver.execute_script('return arguments[0].shadowRoot', item)
        item_text_content = item_shadow_root.find_element("css selector", "#name")    
        if item_text_content.get_attribute('innerHTML') == "JShelter":
             extension_id = item.get_attribute("id")
    options_page = f"chrome-extension://{extension_id}/options.html"
    driver.get(options_page)
    select_level = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(("id", "level-" + str(level)))
                    )
    select_level.click()


## Create web browser driver and start web browser.
def create_driver(browser_type, addon_driver):
    browser, *version = browser_type.split('=')
    with_js = False
    tested_extensions = Config._extensions_to_test
    if "chrome" in browser_type:   
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')   
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--enable-javascript")
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
        chrome_options.browserName = 'chrome'
        if version:
            chrome_options.browser_version=str(version[0])
        if addon_driver:
            extension_paths = Config._extensions_dict_chrome
            for extension in tested_extensions:
                print("installed ", Config._extensions_for_chrome_path + extension_paths[extension])
                chrome_options.add_extension(Config._extensions_for_chrome_path + extension_paths[extension])
                if "JS" in extension:
                    with_js = True
        driver = webdriver.Remote(
            command_executor='http://' + Config.grid_server_ip_address + ':4444/wd/hub',
            #desired_capabilities=d,
            options=chrome_options)
                
        if with_js:
            set_jsr_level_chrome(driver, Config.js_level)

    if "firefox" in browser_type:
        fp = webdriver.FirefoxProfile()
        firefox_options = webdriver.FirefoxOptions()
        if version:
                firefox_options.browser_version=str(version[0])
        fp.set_preference("javascript.enabled", True)
        firefox_options.browserName = 'firefox'
        firefox_options.log.level = "TRACE"
        firefox_options.profile = fp
        firefox_options.add_argument("--no-sandbox")

        driver = webdriver.Remote(
        command_executor='http://' + Config.grid_server_ip_address + ':4444/wd/hub',
        #desired_capabilities=d,
        options=firefox_options)

        if addon_driver:
            extension_paths = Config._extensions_dict_firefox
            for extension in tested_extensions:
                print("installed ", Config._extensions_for_firefox_path + extension_paths[extension])
                webdriver.Firefox.install_addon(driver, Config._extensions_for_firefox_path + extension_paths[extension])   
                if "JS" in extension:
                    with_js = True

        if with_js:
            set_jsr_level_firefox(driver, Config.js_level)

    driver.switch_to.window(driver.window_handles[0]) 
    return driver


   
