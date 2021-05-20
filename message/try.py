from socket import getaddrinfo
from  selenium import webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webdriver import WebDriver

def  main(user_email ,user_password, user_link , badkan_link, course_name, assignment_name):
    is_entered =  Login(user_email , user_password) 
    

def getHomePage():
    try:
        driver.find_element_by_partial_link_text('My Courses').click()
        print("login sucses")
    except:
        print("login failed")
    driver.implicitly_wait(10)
    
    try:
        btn = driver.find_element_by_xpath("//*[contains(text(), 'C++ 5780')]")
        driver.implicitly_wait(2)
        btn.click()
    except:
        print("course was not found")
    # call to register to the curse function  !!!!



def  Locate_the_assignment_page():    # enter  to the assignment page
    try :
        btn = driver.find_element_by_xpath("//*[contains(text(), 'Physical Number - b')]")
        driver.implicitly_wait(2)
        print("assigmnet  found")
        btn.click()
    except:
        print("assigmnet was not  found")
    
    try :
    
        driver.implicitly_wait(5)
        btn =  driver.find_element_by_xpath("//button[@class='collapsible active' ]/../div/div/button"  )
        driver.implicitly_wait(10)
        btn.send_keys(Keys.RETURN)
    except:
        print("error")




PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://104.248.40.179/")
email = driver.find_element_by_name('email')
passw = driver.find_element_by_name('password')
driver.current_url
email.send_keys("maccavi2@gmail.com")
passw.send_keys("123456")
btn = driver.find_element_by_id("btnLogin")
btn.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
getHomePage()
Locate_the_assignment_page()

#Enter to 'my curses' page and check if the user is registered for the course

    

# OPP/EX0  path = /html/body/div[3]/div/div[2]/div/div/div[2]/ul/li[3]/div/div/div/button
# CPP/bash path = /html/body/div[3]/div/div[2]/div/div/div[2]/ul/li[1]/div[1]/div/div/button
# cpp/physical =  /html/body/div[3]/div/div[2]/div/div/div[2]/ul/li[1]/div[2]/div/div/button

