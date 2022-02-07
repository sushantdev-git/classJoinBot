from logging import exception
import time
from speak import speak
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

#zoom link must contain wc else it will ask to open zoom app and selenium can't handle that.
#this works in web.
classLink = 

PATH = "C:\Program Files (x86)\chromedriver.exe"

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
})



def joinClass(endtime, className):
    #this is fxn is specific to zoom
    print(endtime)
    driver = webdriver.Chrome(executable_path=PATH, chrome_options=opt)
    driver.get(classLink)
    speak(className)
    try:
        time.sleep(6)
        camera = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[5]/div[2]/button')
        camera.click()

        mic = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[5]/div[1]/button[1]')
        mic.click()

        joinButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div/div[4]/div/button')
        joinButton.click()

        print("class started..")
        time.sleep(endtime-60) #sleep the program till class ends

    except exception:
        print("some error occured.")
