from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = "YOUR_TINDER_EMAIL"
password = "YOUR_TINDER_PASSWORD"

chrome_driver_path = "YOUR_CHROMEDRIVER_PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

sing_up = driver.find_element_by_css_selector(".button")
sing_up.click()

time.sleep(2)
button = driver.find_element_by_css_selector(".button--outline")
button.click()

time.sleep(2)
facebook = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()

time.sleep(3)
base_window = driver.window_handles[0]
fb_long_window = driver.window_handles[1]
driver.switch_to_window(fb_long_window)

facebook_email = driver.find_element_by_css_selector("#email")
facebook_email.send_keys(email)
facebook_password = driver.find_element_by_css_selector("#pass")
facebook_password.send_keys(password)
facebook_password.send_keys(Keys.ENTER)

driver.switch_to_window(base_window)
time.sleep(7)
allow = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow.click()
time.sleep(1)
allow1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
allow1.click()
time.sleep(1)
try:
    allow2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
    allow2.click()
except:
    pass

while True:
    try:
        time.sleep(3)
        like = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like.click()
    except:
        pass
    try:
        popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]')
        popup.click()
        print("Pop-up Closed!")
    except:
        pass
    try:
        popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
        popup.click()
        print("Pop-up Closed!")
    except:
        pass
    try:
        popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]')
        popup.click()
        print("Pop-up Closed!")
    except:
        pass
