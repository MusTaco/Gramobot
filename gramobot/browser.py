import random
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(options = chrome_options)
rest_between_actions = random.randint(2,5)
