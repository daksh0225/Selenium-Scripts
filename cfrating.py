	# from selenium import webdriver
	# from selenium.webdriver.common.keys import Keys

	# driver = webdriver.Firefox()
	# driver.get("http://www.python.org")
	# assert "Python" in driver.title
	# elem = driver.find_element_by_name("q")
	# elem.clear()
	# elem.send_keys("pycon")
	# elem.send_keys(Keys.RETURN)
	# assert "No results found." not in driver.page_source
	# driver.close()
import getpass
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

options=Options()
options.add_argument('--headless')

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox(options=options)

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("https://www.codeforces.com")
		elem=driver.find_element_by_class_name('ac_input')
		elem1=driver.find_element_by_xpath("//input[@type='submit' and @value='Find']")
		u=input("Username:")
		elem.send_keys(u)
		elem1.click()
		elem2=driver.find_elements_by_css_selector(".info ul li:nth-child(1)")
		# print(elem2)
		for i in elem2:
			print(i.text)
		# elem1.send_keys("Daksh@0225")

		# cookie = {'name' : 'foo', 'value' : 'bar'}
		# driver.add_cookie(cookie)
		# print(driver.get_cookies())
		# driver.find_element_by_name("submit").click()
		# elem1.send_keys(Keys.RETURN)
		# assert "No results found." not in driver.page_source


	def tearDown(self):
		# pass
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

