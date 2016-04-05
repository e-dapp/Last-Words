from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class Page(object):
	'''First step to abstracting web automation'''

	def __init__(self, url = 'http://www.google.com'):
		self.browser = webdriver.Firefox()
		self.browser.get(url)

	def find_element_by_locator(self, locator = '', locatee = ''):
		'''
		Wraps up a number of Selenium's element finding functions
		into one useful abstraction.
		'''

		# To include later:
		#	enhance with "find_elements" so greater generalize function

		if locator == 'id':
			return self.browser.find_element_by_id(locatee)
		elif locator == 'name':
			return self.browser.find_element_by_name(locatee)
		elif locator == 'class name':
			return self.browser.find_element_by_class_name(locatee)
		elif locator == 'xpath':
			return self.browser.find_element_by_xpath(locatee)

	def wait_for_clickable(self, web_element, timeout = 10):
		'''
		Adds custom wait functionality to Selenium's built-in
		click function. Defaulting to 10 second timeout.

		Note: function assumes click should advance browser page,
		ie. change the url.
		'''

		base_url = self.browser.current_url
		print "Waiting for element to be clickable"
		for i in range(timeout):
			if base_url == self.browser.current_url:
				web_element.click()
				print 'clicked'
				time.sleep(1)
			else:
				pass
		if base_url != self.browser.current_url:
			print "Element clicked, browser page progressed."
		else:
			raise Exception('Wait for clickable, timeout')


	def wait_for_findable(self, locator, locatee, timeout = 10):
		'''
		Adds custom wait functionality to find_element_by_locator,
		defaulting to a 10 second timeout.
		'''

		to_return = None
		for i in range(timeout):
			try:
				to_return = self.find_element_by_locator(locator, locatee)
			except:
				time.sleep(1)
		if to_return != None:
			return to_return
		else:
			raise Exception('Wait for findable, timout')