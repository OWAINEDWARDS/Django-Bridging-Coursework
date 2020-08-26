from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://locahost:8000')

assert 'Django' in browser.title
