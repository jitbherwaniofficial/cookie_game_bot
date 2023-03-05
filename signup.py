from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

signup_url = "https://dribbble.com/signup/new"
signin_url = "https://dribbble.com/session/new"

driver.get(url=signin_url)

###### SIGN IN #######
email = driver.find_element_by_id("login")
email.send_keys("jitbherwani92@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("wipro@123456789")
password.send_keys(Keys.ENTER)

###### SIGN UP #######
# name = driver.find_element_by_id('user_name')
# name.send_keys("Jit Bherwani")

# username = driver.find_element_by_id('user_login')
# username.send_keys("jitbherwani")

# email = driver.find_element_by_id("user_email")
# email.send_keys("jitbherwani92@gmail.com")

# password = driver.find_element_by_id("user_password")
# password.send_keys("wipro@123456789")

# terms = driver.find_element_by_id("user_agree_to_terms")
# terms.click()
# terms.send_keys(Keys.ENTER)


