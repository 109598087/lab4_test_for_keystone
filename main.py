from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.fullscreen_window()
driver.get('http://127.0.0.1:3000/')
