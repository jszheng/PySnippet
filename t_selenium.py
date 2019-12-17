from selenium import webdriver
import urllib.request
from urllib.request import URLError

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)

driver.get('http://sampl.cs.washington.edu/tvmconf/')
urls = driver.find_element_by_xpath("//a")

