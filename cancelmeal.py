import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass
from selenium.webdriver.firefox.options import Options

month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
options=Options()
options.add_argument('--headless')

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/home/daksh0225/selenium/')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
profile.set_preference("pdfjs.disabled",True)

driver = webdriver.Firefox(firefox_profile=profile,options=options)
driver.get("https://login.iiit.ac.in/cas/login?service=https%3A%2F%2Fmess.iiit.ac.in%2Fmess%2Fweb%2Findex.php")
elem=driver.find_element_by_id('username')
elem1=driver.find_element_by_id('password')
elem2=driver.find_element_by_name("submit")
u=input("Username:")
p=getpass.getpass(prompt="Password:")
elem.send_keys(u)
elem1.send_keys(p)
elem2.click()
elem3=driver.find_element_by_link_text("Cancel Meals")
elem3.click()
selectm=Select(driver.find_element_by_id("startdate_Month_ID"))
selectm1=Select(driver.find_element_by_id("enddate_Month_ID"))
selectd1=Select(driver.find_element_by_id("startdate_Day_ID"))
selectd2=Select(driver.find_element_by_id("enddate_Day_ID"))
m=int(input("Enter month number: "))
if(m):
	try:
		selectm.select_by_visible_text(month[m])
		selectm1.select_by_visible_text(month[m])
	except:
		print("invalid month")
d1=input("Start date: ")
d2=input("End date: ")
if(d1):
	try:
		selectd1.select_by_visible_text(d1)
	except:
		print("invalid date")
if(d2):
	try:
		selectd2.select_by_visible_text(d2)
	except:
		print("invalid date")
b=input("breakfast (y/n): ")
if b=='y':
	driver.find_element_by_name('breakfast[]').click()
l=input("lunch (y/n): ")
if l=='y':
	driver.find_element_by_name('lunch[]').click()
d=input("dinner (y/n): ")
if d=='y':
	driver.find_element_by_name('dinner[]').click()
un=input('want to uncancel above selected meals (y/n): ')
if un=='y':
	driver.find_element_by_name('uncancel[]').click()

elem5=driver.find_element_by_xpath("//input[@type='submit' and @value='Submit']")
elem5.click()
driver.close()
