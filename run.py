from selenium import webdriver
from common import common
from data import data

username = data.dict['username']
password = data.dict['password']
url = data.dict['url']
number = data.dict['number']

driver = webdriver.Edge('e://python/msedgedriver.exe')
driver.implicitly_wait(10)

result=common.find_func(driver, number, url, username, password)
print(result)


