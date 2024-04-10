import time                                 # for sleeping for a given duration
import sys                                  # some prints, exit
import os                                   # for running  os
from selenium import webdriver              # for running the driver on websites

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

from .client_side_tests.domain_level_settings_test import *
from .client_side_tests.NBS_settings_test import *


"""
In case Selenium Manager times out, try to downlaod the browser driver again.
"""
def create_webdriver(firefox_options):
    try:
        driver = webdriver.Firefox(options=firefox_options)
        return driver
    except WebDriverException as e:
        print("Failed to fetch driver:", e.msg)
        print("Retrying in 5 seconds...")
        time.sleep(5) 
        return create_webdriver(firefox_options)

"""
Names and locations of extensions are configured through this class. 
If you'd like to add another extension to the program, you have to add it to the dictionary here.

"""
class PetConfig:
    def __init__(self):
        print("configuring")

        #These two dictionaries represent key-value pairs of extension abbreviation-extension name. Each dictionary represents one possible browser to set up.
        #In order to add a new extension you must create a new key-value pair in both dictionaries. 
        #The key will be used to recognize the extension inside the client configuration file, the value represents the extension name.

        self.petfco={
                "uo": "uBlock_Origin_f",
                "PB": "Privacy_Badger_f",
                "NS": "NoScript_f",
                "DDGPE": "DuckDuckGoPE_f",
                "Gh": "Ghostery_f",
                "NC": "NetCraft_f",
                "DE": "Decentraleyes_f",
                "JS": "JShelter_f"}

        self.petcco={
                "uo": "uBlock_Origin_c",
                "PB": "Privacy_Badger_c",
                "NS": "NoScript_c",
                "DDGPE": "DuckDuckGoPE_c",
                "Gh": "Ghostery_c",
                "NC": "NetCraft_c",
                "DE": "Decentraleyes_c",
                "JS": "JShelter_c"}

        #These two dictionaries represent key-value pairs of extension name-extension file. Each dictionary represents one possible browser to set up.
        ##In order to add a new extension you must create a new key-value pair in both dictionaries. 
        #The key will be used to recognize the extension name from the previous dictionaries, the value will represent the extension file.

        self.petf = {"None":"", 
                "uBlock_Origin_f": "uBlock0@raymondhill.net.xpi",
                "Privacy_Badger_f": "PrivacyBadger@jetpack.xpi",
                "NoScript_f": "NoScript.xpi",
                "DuckDuckGoPE_f": "DuckDuckGoPE.xpi",
                "Ghostery_f": "firefox@ghostery.com.xpi", 
                "NetCraft_f": "Net_Craft.xpi",
                "Decentraleyes_f": "Decentraleyes.xpi",
                "JShelter_f": "jsr@javascriptrestrictor.xpi"}

        self.petc = {"None":"", 
                "do_not_track":"", 
                "uBlock_Origin_c": "uBlockOrigin.crx",
                "Privacy_Badger_c": "PrivacyBadger.crx",
                "NoScript_c": "NoScript.crx",
                "DuckDuckGoPE_c": "DuckDuckGoPE.crx",
                "Ghostery_c": "Ghostery.crx", 
                "NetCraft_c": "Netcraft.crx",
                "Decentraleyes_c": "Decentraleyes.crx",
                "JShelter_c": "JShelter.crx"}

        self.pet = {"firefox":self.petf,"chrome":self.petc}
        self.petco = {"firefox":self.petfco,"chrome":self.petcco}

        self.addons_path = {"firefox" : os.path.join("addons","firefox"),
                            "chrome" : os.path.join("addons","chrome") }
                         

    """
    Retrieve the extension files so they could be installed. Also check if JShelter is being tested, so it could be set up later. This could be configured
    by developers to activate their own extension settings.
    """
    def getExtensionsPath(self,my_pets,my_browser):

        cwd = os.path.dirname(os.path.abspath(__file__))

        pets_to_test = []   
        my_browser, *version = my_browser.split('=')

        JSlevel = None

        for oneAddon in my_pets:
            oneAddon, *testing_level = oneAddon.split('_')
            #If you'd like to configure you extension, you can save the settings variable here. The variable will be saved as anything after _.
            #For example in case of JShelter - either JS_0, JS_1, JS_2, JS_3 or JS_userSettings can be tested.
            if testing_level: JSlevel = testing_level[0]
            if oneAddon in self.petco[my_browser].keys(): 
                pets_to_test.append(self.petco[my_browser][oneAddon])
        
        pathList = []
 
        for oneAddon in pets_to_test:
            pathList.append(self.pet[my_browser][oneAddon])

        totalPaths = []

        for oA in pathList:      
                if oA != "":  totalPaths.append(os.path.join(cwd, self.addons_path[my_browser], oA))
        
        if JSlevel:
                print("JSlevel being tested is " + JSlevel)
                return totalPaths, None, JSlevel
        else:
            return totalPaths, None 

    
class Browser:
    
    def __init__(self, browser, pet, proxy_setting):

        """
        If given valid proxy settings, this function will configure socks5 proxy properly on chrome and firefox.
        """
        def setup_socks5_proxy(browser, profile, proxy_setting):
            if proxy_setting is not None:
                address = proxy_setting["address"]
                port = proxy_setting["port"]
                bypass_list = proxy_setting["bypass-list"]

                if "chrome" in browser.lower():
                    # https://sordidfellow.wordpress.com/2015/05/21/ssh-tunnel-for-chrome/
                    profile.add_argument("--proxy-server=socks5://%s:%s" % (address, port))
                    profile.add_argument("--proxy-bypass-list=%s" % bypass_list)
                    print("socks5 proxy configured on chrome")

                elif "firefox" in browser.lower():
                    # https://developer.mozilla.org/en-US/docs/Mozilla/Preferences/Mozilla_networking_preferences
                    profile.set_preference("network.proxy.type", 1)
                    profile.set_preference("network.proxy.socks", address)
                    profile.set_preference("network.proxy.socks_port", port)
                    profile.set_preference("network.proxy.socks_version", 5)
                    profile.set_preference("network.proxy.socks_remote_dns", "true")
                    profile.set_preference("network.proxy.no_proxies_on", bypass_list)
                    print("socks5 proxy configured on firefox")


        print("Browser:", browser, "PET:", pet)
        pet_config = PetConfig()

        print("--------------------------------------------------------------------------------------------------------------------------")

        #The set up for individual extensions on individual browsers can vary immensely, it's not really possible to create a uniform function.
        #This is due to the set up being executed client-side, different set up pages can have different DOM model on different browsers. 
        #Also the way browsers name installed extensions is inconsistent. 
        #So its up to the developer to do his own set up.

        totalPaths, config, *JSlevel = pet_config.getExtensionsPath(pet,browser)
        
        ghostery_tested = False

        if "firefox" in browser.lower():
            browser_type, *version = browser.split('=')
            fp = webdriver.FirefoxProfile()
            firefox_options = webdriver.FirefoxOptions()
            setup_socks5_proxy("firefox", fp, proxy_setting)
            if version:
                firefox_options.browser_version=str(version[0])
            
            fp.set_preference("geo.enabled", True)
            fp.set_preference('geo.prompt.testing', True)
            fp.set_preference('geo.prompt.testing.allow', True)
            fp.set_preference("geo.provider.testing", True)
            fp.set_preference("geo.provider.network.url", "https://location.services.mozilla.com/v1/geolocate?key=test")
            fp.set_preference("accept_insecure_certs", True)
            firefox_options.profile = fp
            firefox_options.add_argument("--no-sandbox")


            self.driver = create_webdriver(firefox_options)


            if (totalPaths != "No addons to install"):
                for addon in totalPaths:     
                    if "ghostery" in addon.lower():      
                        ghostery_tested = True    
                    self.driver.install_addon(addon)   
                    print("addon located at" + addon + " installed")  

            #At this point all listed extensions are installed. If you wish to configure them you can do so from this point on till the end of the 
            #object class.

            if ghostery_tested:
                time.sleep(0.5)
                for window_handle in self.driver.window_handles:
                    self.driver.switch_to.window(window_handle)
                    if self.driver.title == "Welcome to Ghostery":
                        try:
                            element = self.driver.find_element("xpath", "/html/body/ui-onboarding-short/ui-onboarding-layout/ui-onboarding-short-main-view/ui-onboarding-card/div[2]/div[2]/ui-button")
                            element.click()
                            self.driver.close()
                            self.driver.switch_to.window(self.driver.window_handles[0])
                            break
                        except Exception as e:
                            print("error ", e)

            if JSlevel:
                print("JSlevel to test is " + JSlevel[0])
                self.driver.get("about:debugging#/runtime/this-firefox")
                time.sleep(0.5)
                element = self.driver.find_element("xpath", "//span[@title='JShelter']")
                parent_li = element.find_element("xpath", "./..")
                uuid_element = parent_li.find_element("xpath","./section/dl/div[@class='fieldpair'][2]/dd")
                uuid = uuid_element.text
                options_page = f"moz-extension://{uuid}/options.html"

                if JSlevel[0] == "userSettings":
                    test_setting_domain_level(self.driver, options_page)
                    test_change_domain_level(self.driver, options_page)
                    test_switching_NBS(self.driver, options_page, browser_type)
                    return

                self.driver.get(options_page)
                time.sleep(0.5)
                select_level = self.driver.find_element("id", "level-" + str(JSlevel[0]))
                select_level.click()
                print("selected JSlevel: " + JSlevel[0])

        elif "chrome" in browser.lower():
            browser_type, *version = browser.split('=')
            chrome_options = webdriver.ChromeOptions()
            setup_socks5_proxy("chrome", chrome_options, proxy_setting)

            if (totalPaths):
                for addon in totalPaths:
                    if "ghostery" in addon.lower():      
                        ghostery_tested = True    
                    chrome_options.add_extension(addon)
                    print("addon located at" + addon + " installed")

            if version:
                chrome_options.browser_version=str(version[0])

            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument('--disable-dev-shm-usage')   
            chrome_options.add_argument('--ignore-certificate-errors')   
            chrome_options.add_argument("--dns-prefetch-disable")
            chrome_options.add_argument("enable-automation")
            self.driver = webdriver.Chrome(options=chrome_options)

            #At this point all listed extensions are installed. If you wish to configure them you can do so from this point on till the end of the 
            #object class.

            if ghostery_tested:
                time.sleep(0.5)
                for window_handle in self.driver.window_handles:
                    self.driver.switch_to.window(window_handle)
                    if self.driver.title == "Welcome to Ghostery":
                        try:
                            element = self.driver.find_element("xpath", "/html/body/ui-onboarding/ui-onboarding-layout/ui-onboarding-main-view/ui-onboarding-card/div[2]/div[2]/ui-button[1]")
                            element.click()
                            self.driver.close()
                            self.driver.switch_to.window(self.driver.window_handles[0])
                            break
                        except Exception as e:
                            print("error ", e)

            if JSlevel:
                print("JSlevel to test is " + JSlevel[0])
                options_page = "chrome-extension://ammoloihpcbognfddfjcljgembpibcmb/options.html"
                if JSlevel[0] == "userSettings":
                    test_setting_domain_level(self.driver, options_page)
                    test_change_domain_level(self.driver, options_page)
                    test_switching_NBS(self.driver, options_page, browser_type)
                    return
                self.driver.get(options_page)
                time.sleep(0.5)
                select_level = self.driver.find_element("id", "level-" + str(JSlevel[0]))
                select_level.click()
                print("selected JSlevel: " + JSlevel[0])


        else:
            print("Unsupported Browser")
            sys.exit(0)

    def quit(self):
        try:
            self.driver.quit()
        except:
            self.driver.close() 


    def visit_sites(self, site_list, delay=30): 
        """Visits all pages in site_list with delay"""
        for site in site_list:
            self.driver.set_page_load_timeout(30)
            sys.stdout.write(".")
            sys.stdout.flush()
            try:              
                self.driver.get(site)
                time.sleep(2)
                self.driver.find_element("id", "play").click()

                time.sleep(delay)
            except TimeoutException:
                 print("Page load timed out, retrying.")
                 self.driver.switch_to.new_window('window')
                 self.visit_sites((site_list[(site_list.index(site)):]), delay=30)

            except KeyboardInterrupt:
                print("Interrupted by keyboard, shutting down.")
                exit(0)
            except:
                print("Unexpected error:", sys.exc_info())
