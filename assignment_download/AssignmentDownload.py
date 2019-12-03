import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass
from selenium.webdriver.firefox.options import Options

options=Options()
options.add_argument('--headless')

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/home/daksh0225/selenium/')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
profile.set_preference("pdfjs.disabled",True)

driver = webdriver.Firefox(firefox_profile=profile,options=options)
driver.get("https://moodle.iiit.ac.in/login/index.php?authCAS=CAS")
elem=driver.find_element_by_id('username')
elem1=driver.find_element_by_id('password')
elem2=driver.find_element_by_name("submit")
u=input("Username:")
p=getpass.getpass(prompt="Password:")
elem.send_keys(u)
elem1.send_keys(p)
elem2.click()
assigns=driver.find_elements_by_partial_link_text("Assignment")
for elemx in assigns:
	elemx.click()
	elem4=driver.find_element_by_partial_link_text(".pdf")
	elem4.click()
	driver.back()
driver.close()


