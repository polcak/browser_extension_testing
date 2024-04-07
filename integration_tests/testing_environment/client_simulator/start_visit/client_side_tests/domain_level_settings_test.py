import random 
from selenium.webdriver.support.select import Select

domains = ["www.fsf.org", "gnu.org", "jshelter.org", "www.fit.vutbr.cz"]
levels = ['0', '2', '3', 'Experiment']

def set_domain_level(driver, options_page, domain, level):
    driver.get(options_page.replace("/options.html", "/options_domains.html"))
    driver.find_elements('id', 'domain-text')[0].send_keys(domain)
    select = Select(driver.find_elements('id', 'domain-level')[0])
    select.select_by_value(level)
    driver.find_elements('id', 'add_domain')[0].click()

	
def unset_domain_level(driver, options_page, domain):
    driver.get(options_page.replace("/options.html", "/options_domains.html"))
    driver.find_elements('id', 'delete-dl-' + domain)[0].click()
 
	
def change_domain_level(driver, options_page, domain, level):
    driver.get(options_page.replace("/options.html", "/options_domains.html"))
    select = Select(driver.find_elements('id', 'dl-change-' + domain)[0])
    select.select_by_value(level)
    driver.find_elements('id', 'overwrite-dl-' + domain)[0].click()

	
def get_domain_level(driver, options_page, domain):
    driver.get(options_page.replace("/options.html", "/options_domains.html"))
    select = Select(driver.find_elements('id', 'dl-change-' + domain)[0])
    selected_option = select.first_selected_option
    return selected_option.get_attribute("value")


	
def test_setting_domain_level(driver, options_page):
    for i in range(len(domains)):
        domain = domains[i]
        level = random.choice(levels)
        set_domain_level(driver, options_page, domain, level)
        if get_domain_level(driver, options_page, domain) == level:
            print("Domain level set correctly, test has passed.")
        else:
            print("Failed to set the correct domain level.")
	
def test_change_domain_level(driver, options_page):
    for i in range(len(domains)):
        domain = domains[i]
        level = random.choice(levels)
        change_domain_level(driver, options_page, domain, level)
        if get_domain_level(driver, options_page, domain) == level:
            print("Domain level set correctly, test has passed.")
        else:
            print("Failed to set the correct domain level.")
        
        # Tear down.
        unset_domain_level(driver, options_page, domain)