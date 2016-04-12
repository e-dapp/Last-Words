from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from page_object import Page
import pandas as pd
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

#	For the moment though, I'm mostly just worried about efficiently 
#	scraping the text from the table. That is proving a challenge

def scrape(table_el):
	'''
	Takes in table_el, a predetermined selenuim table element, 
	returns an array containing text from table. 
	'''

	tempArray = []
	tempRow = []

	for i in range(2, 5):
		tempRow = []
		for j in range(1, colCount + 1):
			toAppend = table_el.find_element_by_xpath('./tbody/tr[' + str(i) + ']/td[' + str(j) + ']').text
		tempRow.append(toAppend)
		tempArray.append(tempRow)
		print 'row appended'
	return tempArray

def get_col(table_el):
	'''
	Takes in table_el, a predetermined selenuim table element, 
	returns list of text in first row.
	Makes assumption first row is column headers.
	'''

	columns = []

	for i in range(colCount):
		i += 1
		colName = table_el.find_element_by_xpath('./tbody/tr[1]/th[' + str(i) + ']').text
		if colName in columns:
			columns.append(colName + str(1))
		else:
			columns.append(colName)
		return columns

if __name__ == '__main__':
	page = Page('http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html')
	table_el = page.find_element_by_locator('class name', 'os')
	rowCount = len(table_el.find_elements_by_xpath('./tbody/tr'))
	colCount = len(table_el.find_elements_by_xpath('./tbody/tr[2]/td'))
	column_heads = get_col(table_el)
	a = scrape(table_el)
	dF = pd.DataFrame(a, columns = column_heads)