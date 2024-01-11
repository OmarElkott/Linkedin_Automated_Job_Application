from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "YOUR_LOGIN_EMAIL"
ACCOUNT_PASSWORD = "YOUR_LOGIN_PASSWORD"
PHONE = "YOUR_PHONE_NUMBER"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3759132488&geoId=105149290&keywords="
    "Python%20Developer&location=&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
)

# Click Reject Cookies Button
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, value='button[action-type="DENY"]').click()

# Click Sign in Button
time.sleep(2)
driver.find_element(By.LINK_TEXT, value="Sign in").click()

# Sign in
time.sleep(5)
driver.find_element(By.ID, value="username").send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

# Locate the apply button
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button").click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE)

# Submit the application
driver.find_element(By.CSS_SELECTOR, value="footer button").click()
