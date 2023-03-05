from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

link = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
a = driver.find_element_by_css_selector('#articlecount a')
a.click()
pages = driver.find_element_by_xpath('//*[@id="mw-content-text"]/table/tbody/tr[3]/td[1]/a')
pages.click()
search = driver.find_element_by_xpath('//*[@id="ooui-php-1"]')
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# submit = driver.find_element_by_xpath('//*[@id="ooui-php-7"]/button')
# submit.click()
pages = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[3]/ul/li[1]/a')
pages.click()
python = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[2]/li[1]/a')
python.click()
    
# driver.quit()
