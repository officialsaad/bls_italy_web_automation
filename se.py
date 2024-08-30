from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

chrome_driver_path = "chromedriver-win64/chromedriver.exe"
web_login_link = "https://blsitalypakistan.com/account/login"

# User credentials
ayaz_bhai_ka_email = "*"
ayaz_bhai_ka_password = "*"

options = webdriver.ChromeOptions()
options.binary_location = 'chrome-win64/chrome.exe'
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
driver.maximize_window()
stat_time = time.time()
driver.get(web_login_link)

title = driver.title
print(title)

WebDriverWait(driver, 10).until(lambda x: 'BLS Login Your Account for Italian Visa from Pakistan' in driver.title)

email = driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
password = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")

email.send_keys(ayaz_bhai_ka_email)
password.send_keys(ayaz_bhai_ka_password)

inputcapta = driver.find_element(By.ID, "captcha_code_reg")

# Define the WebDriverWait with a timeout and polling frequency
wait = WebDriverWait(driver, 30, poll_frequency=1)  # 30 seconds timeout, 1 second polling interval

# Use WebDriverWait with a lambda function to wait until the length of the input field value is 5
wait.until(lambda driver: len(inputcapta.get_attribute('value')) == 5)

login_button = driver.find_element(By.XPATH, "//button[@name='submitLogin']")
login_button.click()

# Wait for the new page to load and open a new tab
WebDriverWait(driver, 10).until(EC.new_window_is_opened(driver.window_handles))
driver.execute_script('window.open("https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment");')

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Wait for the element to be visible
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//img[@alt='Close'])[1]"))
    )
    close_button.click()
    print("Close button clicked successfully.")
except TimeoutException:
    print("TimeoutException: Close button was not found.")

# Hide elements after they become visible
try:
    disablebg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='disablebg']"))
    )
    driver.execute_script("arguments[0].style.display = 'none';", disablebg)
    print("disablebg element hidden successfully.")
except TimeoutException:
    print("TimeoutException: disablebg element was not found.")

try:
    blogger_form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='bloggerform']"))
    )
    driver.execute_script("arguments[0].style.display = 'none';", blogger_form)
    print("blogger_form element hidden successfully.")
except TimeoutException:
    print("TimeoutException: blogger_form element was not found.")

# Select Lahore in dropdown
dropdown = Select(driver.find_element(By.ID, 'valCenterLocationId'))
dropdown.select_by_visible_text('Lahore (Pakistan)')
print("Dropdown option selected successfully.")

# Print total execution time
end_time = time.time()
print("Start time:", stat_time, "\nTotal time:", end_time - stat_time)

# Close the browser (optional)
# driver.quit()
