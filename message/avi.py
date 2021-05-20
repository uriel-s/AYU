import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

from selenium.webdriver.remote.webdriver import WebDriver

courseName = "OOP"
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def findButton(Assingment_name):
    a = 0

    text = '//button[text()='+Assingment_name+']'
    driver.find_element_by_xpath(text).click()
    
  
    return a

def register_for_course(Course_name):
    driver.find_element_by_partial_link_text('Public').click()
    driver.find_elements_by_xpath('.//span[@class = '+Course_name).click()
    driver.find_elements_by_xpath('.//span[@class = Ex0 Final test').click()
    driver.find_element_by_class_name("btn blue_enjoy").click


driver.get("http://104.248.40.179/")
print(driver.current_url)
email = driver.find_element_by_name('email')
passw = driver.find_element_by_name('password')
email.send_keys("maccavi2@gmail.com")
passw.send_keys("123456")
btn = driver.find_element_by_id("btnLogin")

btn.send_keys(Keys.RETURN)

driver.implicitly_wait(9)
Assingment_name = 'Solver - B'
Course_name = 'OOP'
a = findButton(Assingment_name)
if(a == 0):
   register_for_course(Course_name)