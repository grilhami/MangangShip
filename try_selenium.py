# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# # get the path of ChromeDriverServer
# dir = os.path.dirname(__file__)
# chrome_driver_path = dir + "\chromedriver.exe"
#
# # create a new Chrome session
# driver = webdriver.Chrome(chrome_driver_path)
# driver.implicitly_wait(30)
# driver.maximize_window()
#
# # navigate to the application home page
# driver.get("http://www.google.com")
#
# # get the search textbox
# search_field = driver.find_element_by_name("q")
#
# # enter search keyword and submit
# search_field.send_keys("Selenium WebDriver Interview questions")
# search_field.submit()
#
# # get the list of elements which are displayed after the search
# # currently on result page using find_elements_by_class_name  method
# lists = driver.find_elements_by_class_name("r")
#
# # get the number of elements found
# print("Found " + str(len(lists)) + " searches:")
#
# # iterate through each element and print the text that is
# # name of the search
#
# i=0
# for listitem in lists:
#    print(listitem)
#    i=i+1
#    if(i>10):
#       break
#
# # close the browser window
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start WebDriver
driver = webdriver.Chrome()
# driver.implicitly_wait(30)
driver.maximize_window()
print("Opening Browser...")

# Get Link
driver.get("http://128.199.150.205/#")

# Detect Login and Password textbox
field_name = driver.find_element_by_id("id_username")
field_pass = driver.find_element_by_id("id_password")

# Sign In
field_name.send_keys("admin")
field_pass.send_keys("4321dcba")
field_name.submit()


# Detect String
string = driver.find_element_by_css_selector("h1").get_attribute("innerHTML")
print(string)

# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# time.sleep(5)
# driver.quit()

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()
