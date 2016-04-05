from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from page_object import Page
import time

#	The idea here will be to scrape the information from
#	http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html
#	which is Texas state records on last words of those executed by 
#	the state fince 1984. Note that there were 2 last month.
#
#	Oh Texas.

#	I'll be using Selenium webdriver and my Page Object to run through 
#	and pick up all the necessary text. The first iteration will likely
#	not run super fast as each person's last words and conviction information
#	are on separate pages. So if there are N people, we have at least 2N
#	pages to go through and scrape from. Should be fun.
