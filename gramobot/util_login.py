from util_constants import driver, rest_between_actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import json

#Login function    
def login(username, password):

    try:
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        self.skip_not_now()
    except FileNotFoundError:

        #Enter username
        uname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        uname.send_keys(username)
        time.sleep(rest_between_actions)

        #Enter password
        passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        passw.send_keys(password)
        time.sleep(rest_between_actions)

        #Login
        passw.send_keys(Keys.ENTER)

        self.skip_not_now()
        try:
            link_btns = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@role="link"]')))
            self.get_cookies()
        except NoSuchElementException:
            print("couldn't log in")
    except Exception as e:
        print(f'Error occured: {e}')

def skip_not_now(self):
    try:
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    except Exception:
        pass

#Get cookies
def get_cookies(self):
    driver = self.driver
    with open('cookies.json', 'w') as f:
        json.dump(driver.get_cookies(), f)