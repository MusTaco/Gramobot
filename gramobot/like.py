from .browser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

def like_post(post_link):

    # navigate to page
    if driver.current_url != post_link:
        driver.get(post_link)

    # find elements and click like
    try:
        btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81"]')))
        like_btn = btn.find_element(By.XPATH, value = "//*[name()='svg' and @aria-label='Like']")

    except TimeoutException:
        return f"Unable to like post: {post_link}"
    
    except NoSuchElementException:
        return f"Post already liked: {post_link}"
    
    btn.click()
    return f"Liked post: {post_link}"
    