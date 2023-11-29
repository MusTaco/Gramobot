from .browser import driver, rest_between_actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def unfollow_user(username):

    # navigate to url
    url = f"https://instagram.com/{username}"

    driver.get(url)

    # click Follow
    try:
        follow_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[div[contains(normalize-space(), 'Follow')]]")))
    except TimeoutException:
        return f"(@{username}) User does not exist or couldn't be reached."
    
    # check if already following
    if follow_btn.text == 'Following':
        follow_btn.click()
        time.sleep(rest_between_actions)
        driver.find_element(By.XPATH, value="//div[span[contains(normalize-space(), 'Unfollow')]]").click()
        return f'(@{username}) Unfollowed.'
    
    # if not following
    return f'(@{username}) You are not currently following.'
    



    

    


