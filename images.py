from bs4 import *
import requests as rq 
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import autoit
import time
driverpth = "C:\\Program Files (x86)\\chromedriver.exe"
GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
data = "naruto"
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(executable_path=driverpth,options=options)
driver.get("https://myanimelist.net")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[10]/div/div/div/div[2]/button").click()

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/span[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/span[3]").send_keys('naruto')
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/span[3]").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/a[1]").click()
time.sleep(2)
source = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[1]/a/img")
action = ActionChains(driver)
action.context_click(source).perform()
