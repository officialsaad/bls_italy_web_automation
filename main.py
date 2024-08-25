from library import *


chrome_driver_path = "chromedriver-win64/chromedriver.exe"
web_login_link = "https://blsitalypakistan.com/account/login"
url = "https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment"
appointment_page_url = "https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment"

# User credentials
ayaz_bhai_ka_email = "Enter Email"
ayaz_bhai_ka_password = "Enter Password"

options = webdriver.ChromeOptions()
# options.add_argument("--disable-popup-blocking")
# options.add_argument("--disable-notifications")
# options.set_capability('unhandledPromptBehavior', 'dismiss')


options.binary_location = 'chrome-win64/chrome.exe'
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
driver.maximize_window()
stat_time = time.time()
driver.get(web_login_link)

title = driver.title
print(title)


# WebDriverWait(driver, 1).until(lambda x: 'BLS Login Your Account for Italian Visa from Pakistan' == title)

# driver.find_element(By.NAME, '332789bd2494c8f6161e065a87ab688351a3bb7e3f1ffa1dd75d4e6a682c76a6baa7e47ff2fe3d8c585a7003a923e6b0adc46d17f34c4ee1253518a0e469c98fVT5ZKPnuIbTwxwqIlXGOvioMFwDFmmvYiFY9zU3ytDs=')
# email = driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
# password = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
#
# email.send_keys(ayaz_bhai_ka_email)
# password.send_keys(ayaz_bhai_ka_password)

def download_image(url, save_as='capta_folder/image.jpg'):

    response = requests.get(url)
    if response.status_code == 200:
        with open(save_as, 'wb') as f:
            f.write(response.content)

    # download_image(image_url, save_as)
    else:
        print("Response not found of img")


def login_ka_fun():
    time.sleep(1)

    # driver.find_element(By.NAME, '332789bd2494c8f6161e065a87ab688351a3bb7e3f1ffa1dd75d4e6a682c76a6baa7e47ff2fe3d8c585a7003a923e6b0adc46d17f34c4ee1253518a0e469c98fVT5ZKPnuIbTwxwqIlXGOvioMFwDFmmvYiFY9zU3ytDs=')
    email = driver.find_element(
        By.XPATH, "//input[@placeholder='Enter Email']")
    password = driver.find_element(
        By.XPATH, "//input[@placeholder='Enter Password']")

    email.send_keys(ayaz_bhai_ka_email)
    password.send_keys(ayaz_bhai_ka_password)

    inputcapta = driver.find_element(By.ID, "captcha_code_reg")
    inputcapta.click()
    # Define the WebDriverWait with a timeout and polling frequency
    # 30 seconds timeout, 1 second polling interval

    imagecapta = driver.find_element(By.ID, "Imageid")
    img_src = imagecapta.get_attribute("src")
    print(img_src)

    download_image(img_src)

    # send for solve captcha

    # urllib.request.urlretrieve(url, save_as)
    # image_url = str(img_src)
    #  save_as = 'capta_folder/image.jpg'

    wait = WebDriverWait(driver, 12, poll_frequency=1)

    # Use WebDriverWait with a lambda function to wait until the length of the input field value is 5
    wait.until(lambda driver: len(inputcapta.get_attribute('value')) == 5)

    login_button = driver.find_element(
        By.XPATH, "//button[@name='submitLogin']")

    cookies = driver.get_cookies()
    print("Before login Coookies /n", cookies)
    login_button.click()


refresh_login = True

while refresh_login:

    try:
        driver.refresh()
        login_ka_fun()
        time.sleep(2)
        if driver.current_url != web_login_link:
            refresh_login = False
            break

    except Exception as e:
        continue


# title = driver.title

# WebDriverWait(driver, 10).until(lambda x: 'Italy in Pakistan' == title)


# WebDriverWait(driver, 3, 0.2).until(EC.presence_of_element_located((By.XPATH,"//div[@class='content pdb0']//li[4]"))).click()


# driver.execute_script('window.open("https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment");')
#


def click_element_by_xpth(xpath="//img[@alt='Close']"):
    # Wait for the element to be clickable and click it
    try:
        close_button = WebDriverWait(driver, 15, 1).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        close_button.click()
        print("Close button clicked successfully.")
    except Exception as e:
        print("Exception occurred:", str(e))

# Function to monitor and change the display property of the element


def monitor_and_hide_element(css_selector=".disablebg1"):
    while True:
        # Continuously check the display property of the element
        try:
            # element = WebDriverWait(driver, 10, 0.8).until(EC.presence_of_element_located((By.CSS_SELECTOR,css_selector)))

            # Check if the element is present in the DOM
            element = driver.find_element(By.CSS_SELECTOR, css_selector)
            display_property = driver.execute_script(
                "return window.getComputedStyle(arguments[0]).display;", element)

            # If the display property is 'block', change it to 'none'
            if display_property == 'block':
                driver.execute_script(
                    "arguments[0].style.display = 'none';", element)
                print("Element with class '.disablebg1' found and hidden.")
                break

            # Wait for a short duration before checking again
            time.sleep(1)
        except Exception as e:
            continue
            print(f"Error: {e}")


# # "(//img[@alt='Close'])[1]" xpath for close btn.
# click_element_by_xpth("(//img[@alt='Close'])[1]")

refresh_appointment_page = True

while refresh_appointment_page:
    try:

        # cookies = driver.get_cookies()
        # print("after login appoint ment page cookies ", cookies)

        # btn_appointment = driver.find_element(
        #     By.XPATH, "//div[@class='content pdb0']//li[4]")
        # btn_appointment.click()

        # if appointment_page_url == driver.current_url:
        #     refresh_appointment_page = False
        #     break
        # else:
        #     driver.get(appointment_page_url)
        #     break

        driver.get(appointment_page_url)
        time.sleep(1)

        if appointment_page_url == driver.current_url:
            break
        else:
            continue

    except Exception as e:
        continue


# islamabad = "Islamabad (Pakistan)"
# lahore = "Lahore (Pakistan)"
# karachi = "Karachi (Pakistan)"
# faislabad = "Faisalabad (Pakistan)"
# multan = "Multan (Pakistan)"
# queta = "Quetta (Pakistan)"

application_center = {"islamabad": "Islamabad (Pakistan)", "lahore": "Lahore (Pakistan)",
                      "karachi": "Karachi (Pakistan)", "faislabad": "Faisalabad (Pakistan)", "multan": "Multan (Pakistan)", "queta": "Quetta (Pakistan)"}

# # Optional: Selecting an option from dropdown

application_page_url = driver.current_url
print("appointment page url", application_page_url)

refrest_to_application_page_url = True


while refrest_to_application_page_url:

    try:

        # Call the function to monitor and hide the element
        click_element_by_xpth("(//img[@alt='Close'])[1]")

        appplication_center_dropdown = driver.find_element(
            By.ID, 'valCenterLocationId')
        time.sleep(0.5)
        select = Select(appplication_center_dropdown)
        select.select_by_visible_text(application_center["queta"])
        time.sleep(0.5)
        cookies = driver.get_cookies()

        if appointment_page_url != driver.current_url:
            cookies = driver.get_cookies()
            print("after select appointment center cookies", cookies)
            break

        else:
            driver.refresh()
            time.sleep(2)
            continue

        # if

        # dropdown.click()
        # dropdown.select_by_visible_text("Quetta (Pakistan)")
    except Exception as e:
        # driver.get(application_page_url)
        driver.refresh()
        time.sleep(2)
        continue
        print("Exception occurred:", str(e))


current_url = None

service_type = {"SchengenTourism": "Schengen - Tourism", "SchengenBusiness": "Schengen - Business", "NationalWork": "National - Work",
                "NationalStudy": "National - Study", "NationalFamilyReunion": "National - Family Reunion", "legalisation": "Legalisation"}
time.sleep(0.5)
service_type_dropdown = driver.find_element(By.ID, "valCenterLocationTypeId")
Select(service_type_dropdown).select_by_visible_text(
    service_type["NationalFamilyReunion"])

time.sleep(1)


# Call the function to monitor and hide the element
monitor_and_hide_element()
monitor_and_hide_element(css_selector=".bloggerform1")


type_of_appointment_dic = {"Individual": "Individual", "Group/Family2members": "Group/Family: 2 members", "Group/Family3members": "Group/Family: 3 members", "Group/Family4members":
                           "Group/Family: 4 members", "Group/Family5members": "Group/Family: 5 members", "Group/Family6members": "Group/Family: 6 members", "Group/Family7members": "Group/Family: 7 members"}

type_of_appointment_dropdown = WebDriverWait(driver, 10, 0.2).until(
    EC.visibility_of_element_located((By.ID, "valAppointmentForMembers")))
Select(type_of_appointment_dropdown).select_by_visible_text(
    type_of_appointment_dic["Group/Family2members"])
time.sleep(0.3)
current_url = driver.current_url


# monitor_and_hide_element()
# monitor_and_hide_element(css_selector=".bloggerform1")

print('ss')

# driver.refresh()


# monitor_and_hide_element()
# monitor_and_hide_element(css_selector=".bloggerform1")


# time.sleep(2)
# driver.refresh()

# monitor_and_hide_element()
# monitor_and_hide_element(css_selector=".bloggerform1")


# driver.refresh()

# monitor_and_hide_element()
# monitor_and_hide_element(css_selector=".bloggerform1")

# //input[@id= 'captcha_code_reg']

# input_captcha = driver.find_element(By.ID, "captcha_code_reg")

# WebDriverWait(driver, 10, 0.5).until(
#     lambda driver: (len(input_captcha.get_attribute('value')== 5) or (len(input_captcha.get_attribute('value')== 6)) )
# )


while True:

    try:

        monitor_and_hide_element()
        monitor_and_hide_element(css_selector=".bloggerform1")

        inputcapta = driver.find_element(By.ID, "captcha_code_reg")

        wait = WebDriverWait(driver, 12, 1)
        wait.until(lambda driver: len(
            inputcapta.get_attribute('value')) in [5, 6])
        cookies = driver.get_cookies()
        print("cookies are ", cookies)

        print("asdsdadasdad")
        # //input[@id= 'valAppointmentDate']

        # time.sleep(2)

        # if len(available_dates) > 0:
        #     if play_audio == True:
        #         media = vlc.MediaPlayer('sound/Amazing.mp3')
        #         media.play()
        #         play_audio = False

        # else:
        #     pass

        # selected_date = random.choice(reversed_order_dates)
        # selected_date.click()

        if current_url == driver.current_url:

            input = driver.find_element(By.ID, "valAppointmentDate")
            input.click()

            # Wait until the datepicker is visible
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'datepicker-days')))

            # Get all available dates by title
            available_dates = driver.find_elements(
                By.XPATH, '//*[@title="Available"]')
            print("avialable_dates", available_dates)

            reversed_order_dates = available_dates[::-1]

            print("reverse__dates", available_dates)

            selected_date = random.choice(reversed_order_dates)
            selected_date.click()

            # if current_url == driver.current_url:
            #     pass
            # else:
            #     break

            # driver.refresh()
            # time.sleep(2)
            # monitor_and_hide_element()
            # monitor_and_hide_element(css_selector=".bloggerform1")

        else:
            break

    except Exception as e:
        print(str)
        driver.refresh()
        time.sleep(3)
        continue

        # Call the function to monitor and hide the element
        # monitor_and_hide_element()
        # monitor_and_hide_element(css_selector=".bloggerform1")

        # print(driver.current_url)

        # # //input[@id= 'captcha_code_reg']

        


WebDriverWait(driver, 10, 0.4).until(
    EC.visibility_of_element_located((By.ID, 'valAppointmentType')))


# url = "https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment"

# driver.get(url=url)
# time.sleep(3)
# if url == driver.current_url:
#     print("URL is correct")
# else:
#     print("URL is incorrect")

# Close the WebDriver


# //select[@id= 'valAppointmentType']


# # select appointment slot

# //select[@name ='valApplicant


# # First Name
# // input[@placeholder = 'Enter First Name']


# # last name

# // input[@placeholder = 'Enter Last Name']


# # i agree form button
# // input[@placeholder = 'Enter Last Name']


# # recaptcha click


# try:

#     WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located(
#         (By.XAPTH, "// div[@class = 'g-recaptcha']"))).click()
# except Exception as e:
#     pass
# print(str(e))


#
# # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//img[@alt='Close'])[1]")))
# # #
# # # #
# # # close =  driver.find_element(By.XPATH, "(//img[@alt='Close'])[1]")
# # # close.click()
# # # #
# # print("your start time is:",stat_time,"/n", "Total_time is: ",stat_time - time.time())
# # # send_post_request(url='https://www.imgocr.com/api/imgocr_get_text', file_path)
# #
# # disablebg = driver.find_element(By.XPATH,"//div[@class='disablebg']")
# # blogger_form = driver.find_element(By.XPATH, "//div[@class='bloggerform']")
# # #
# # # # driver.implicitly_wait(2)
# # #
# # # # Use JavaScript to set the elements' display to 'none'
# # # driver.execute_script("arguments[0].style.display = 'none';", disablebg)
# # # driver.execute_script("arguments[0].style.display = 'none';", blogger_form)
# #
# #
# # # select Lahore in drop down
# # dropdown = Select(driver.findElementById('valCenterLocationId'))
# #
# # # Select an option by visible text
# # dropdown.selectByVisibleText('Lahore (Pakistan)')
# #
# #
# # # appoint = "https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment"
# #
# # # Open new tab
# # # driver.execute_script('window.open("https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment");')
# # # Switch between tabs
# # # driver.switch_to.window(driver.window_handles[1])
