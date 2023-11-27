from .browser import driver, rest_between_actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

def send_dm(receiver, message):

    # navigate to page 
    dm_url = 'https://www.instagram.com/direct/inbox/'
    if driver.current_url != dm_url:
        driver.get(dm_url)

    # click button
    msg_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81"]')))
    msg_btn.click()

    # type username in query box
    query_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="queryBox"]')))

    # clear query
    query_box.clear()
    
    query_box.send_keys(receiver)

    time.sleep(rest_between_actions)

    # click username
    try:
        username_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]')))
        username_btn.click()
    except TimeoutException:
        return f"Could not send dm to {receiver}."

    time.sleep(rest_between_actions)

    # click chat
    chat = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Chat")]')))
    chat.click()

    # type message 
    textbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-describedby="Message"]')))
    textbox.send_keys(message)

    time.sleep(rest_between_actions)

    textbox.send_keys(Keys.ENTER)

    return f"Dm sent successfully to {receiver}!"

    