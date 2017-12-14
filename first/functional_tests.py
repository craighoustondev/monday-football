from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

assert 'Monday Night Indoor Football' in browser.title

browser.quit()
