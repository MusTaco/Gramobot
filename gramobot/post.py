from .browser import driver, rest_between_actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import json

def insta_post(post, caption):
                    
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
    
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Your post has been shared.')]")))
        print('Shared!')
    except TimeoutException:
        print('Could not share the post.')