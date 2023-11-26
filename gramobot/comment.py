from .browser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def make_comment(post_link, comment):

    # navigate to the post url 
    if driver.current_url != post_link:
        driver.get(post_link)

    # search for comment input
    try:
        comment_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Add a comment…"]')))
    except TimeoutException:
        return f"Unable to comment. Seems like comments are disabled on this post: {post_link}"
    comment_input.click()

    comment_input = driver.find_element(By.XPATH, value = '//textarea[@aria-label="Add a comment…"]')
    comment_input.send_keys(comment)

    # press enter 
    comment_input.send_keys(Keys.ENTER)

    return "Comment posted!"

