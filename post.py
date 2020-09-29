from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time
from dk import photo
def post():
    z = photo()
    tags = "#anime #manga #otaku #art #animeart #animegirl #cosplay #naruto #kawaii #animeedits #fanart #drawing #animememes #memes #animeedit #cute #love #meme #animes #japan #onepiece #digitalart #animelover #edit #weeb #artist #animelove #like #cosplayer #bot"
    username = ""
    passwd = ""
    driverpth = "C:\\Program Files (x86)\\chromedriver.exe"
    photopath = "C:\\Users\\abuba\\OneDrive\\Desktop\\otakukamisama\\1.jpg"
    phototext = "Anime: "+z[0]+"-""Synopsis: "+z[1]+"\n.\n.\n.\n.\n.\n.\n.\n.Tags: \n"+tags

    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(executable_path=driverpth,options=options)
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input").send_keys(username)
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(passwd)
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    time.sleep(1.5)
    autoit.win_active("Open") #open can change by your os language if not open change that
    time.sleep(2)
    autoit.control_send("Open", "Edit1", photopath)
    time.sleep(1.5)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(2)
    i = 0

    while i<2:  
        #for scrolling page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        
        i+=1
    driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div[2]/div/div/div/button[1]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(phototext)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(4)
    driver.close()

post()
