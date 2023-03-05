from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')

chrome_driver = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver,options=options)
url = "https://www.amazon.in/dp/B09SZTXHC4"
python_url="https://www.python.org/"
driver.get(url=python_url)
# search_bar = driver.find_element_by_name("q")
# logo = driver.find_element_by_class_name("python-logo")
# print(search_bar.get_attribute("placeholder"))
# print(logo.size)

# link = driver.find_element_by_css_selector(".documentation-widget a")
# print(link.text)

# price = driver.find_element_by_xpath("//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[1]")
# print(price.get_attribute("textContent"))

event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in event_names:
#     print(name.text)

# dictionary comprehension
# myDict = { k:v for (k,v) in zip(keys, values)} 

events = {n:{"time":event_times[n].text,"name":event_names[n].text} for n in range(len(event_times))}
# events={}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }

print(events)


driver.quit()
