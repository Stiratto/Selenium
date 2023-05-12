import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class use_unittest(unittest.TestCase):
	
	def setUp(self):
		browser_choose = input("1 if firefox, 2 if Chrome, 3 if Opera: ")
		if browser_choose == "1":
			self.driver = webdriver.Firefox()
		elif browser_choose == "2":
			self.driver = webdriver.Chrome()
		elif browser_choose == "3":
			self.driver = webdriver.Opera()
		else: 
			print("That's not a valid option.")			
		
	def test_autologin(self):
		driver = self.driver
		user_email = input("Enter your email: ")
		user_password = input("Enter your password: ")
		driver.get("https://www.facebook.com/")	
		try:
			email_button = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "email")))
			email_button.send_keys(user_email)
		except:
			print("Couldn't type email address!")
		
		try:
			pwd_button = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "pass")))
			pwd_button.send_keys(user_password)
		except:
			print("Couldn't type password!")	
		
		login_button = driver.find_element(By.NAME, 'login')
		login_button.click()
		assert "Couldn't find the element" not in driver.page_source, "The element was found on the page"
			


if __name__ == '__main__':
	unittest.main()
