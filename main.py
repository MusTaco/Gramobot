
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tkinter.filedialog import askopenfilename
import time
import random
import json

#wait between actions(higher and random is preffered)
rest_between_actions = random.randint(2,5)

class bot:

    def __init__(self):
        self.driver = webdriver.Chrome()

    #Login function    
    def login(self, username, password):
        driver = self.driver
        driver.get('https://instagram.com')

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


    def instagram_post(self, post, caption):
        driver = self.driver
                     
        #get all side bar buttons
        link_btns = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@role="link"]')))

        #run loop to find Create button, then click
        for elem in link_btns:
            try:
                
                elem.find_element(By.XPATH, ".//span[contains(text(), 'Create')]")
                elem.click()
                break
            except NoSuchElementException:
                pass
        time.sleep(rest_between_actions)
        #actions required to post
        post = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime"]'))).send_keys(post)
        time.sleep(rest_between_actions)

        for _ in range(2):
            Next = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Next')]"))).click()
            time.sleep(rest_between_actions)

        caption = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Write a caption..."]'))).send_keys(caption)
        time.sleep(rest_between_actions)

        Share = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Share')]"))).click()
        time.sleep(5)



    
    
if __name__ == '__main__':
    file_path = askopenfilename()
    caption = 'test post'
    Bot = bot()
    Bot.login('your-username', 'your-password')
    Bot.instagram_post(file_path, caption)
