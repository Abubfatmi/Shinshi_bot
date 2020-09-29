from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time

driverpth = "C:\\Program Files (x86)\\chromedriver.exe"
options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
    
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
   
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(executable_path=driverpth,options=options)
driver.get('https://www.wikipedia.org/')
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/form/fieldset/div/input").send_keys("naruto")
driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button/i').click()
title = driver.find_elements_by_class_name("mf-section-1 collapsible-block open-block")
for post in title:
    name = post.text

print(name)
