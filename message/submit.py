from socket import getaddrinfo
from  selenium import webdriver
import selenium
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webdriver import WebDriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

# def  main(user_email ,user_password, user_link , badkan_link, course_name, assignment_name):
#     is_entered =  Login(user_email , user_password) 



def Assign_my_code(gitHub,IDs):
    try:
        git_address = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "githubUrl")))
        git_address.send_keys(gitHub)
        if(len(IDs)==2):
            col1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "collab1")))
            col1.send_keys(IDs[0])
            col2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "collab2")))
            col2.send_keys(IDs[1])
        if(len(IDs)==1):
            print("submission one col")
            col1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "collab1")))
            col1.send_keys(IDs[0])
    except:
            print("fillin colbs faild")
    try:
        x = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "saveGrade")))
        x.send_keys(Keys.RETURN)
        #needs to change from sleep(40) to wait until submission is complete! 
        #do not ignore!!!
        time.sleep(40)
        text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "white_square_2"))).text
        return text
    except:
        print("submission faild")
        return 0



# register to new curse     
def register_for_course(Course_name):
    try:
        driver.find_element_by_partial_link_text('Public').click()
        print("public btn sucses")
        driver.implicitly_wait(2)
        btn = driver.find_element_by_xpath("//*[contains(text(), '"+Course_name +"')]").click()
    except:
        print("public btn failed")
    
    try:
        btn = driver.find_element_by_xpath("//*[contains(text(), '"+Course_name +"')]").click()
    except:
        print("curse btn failed")       
    try:
        btn =  driver.find_element_by_xpath("//li[@class='active']/div/button").click()
    except:
        print("assigment btn failed") 
    try:
        btn =  driver.find_element_by_xpath("//button[@class='collapsible active' ]/../div/div/button"  ).click()
    except:
        print("register btn failed")     

#Enter to a curse page that contain all his assignment or register to new curse if needed
def getCursePage(Course_name):
    try:
        driver.find_element_by_partial_link_text('My Courses').click()
        print("login sucses")
    except:
        print("login failed")
    driver.implicitly_wait(10)

    try:
        path = "//*[contains(text(), '"+Course_name +"')]"
        # btn = driver.find_element_by_xpath(path)
        # driver.implicitly_wait(2)
        # btn.click()
        btn= WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, path)))
        btn.click()
    except: 
        print("course was not found")
        register_for_course(Course_name)


# enter  to the assignment page
def  Locate_the_assignment_page(assignment):    
    try :
        path = "//*[contains(text(), '"+assignment+"')]"
        # btn = driver.find_element_by_xpath(path)
        # driver.implicitly_wait(2)
        # print("assigmnet  found")
        btn= WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, path)))
        btn.click()
    except:
        print("assigmnet was not  found")
    
    try :
        #driver.implicitly_wait(5)
        #btn =  driver.find_element_by_xpath("//button[@class='collapsible active' ]/../div/div/button"  )
        #driver.implicitly_wait(10)
        path = "//button[@class='collapsible active' ]/../div/div/button" 
        btn= WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, path)))
        btn.send_keys(Keys.RETURN)
    except:
        print("error")


def fill_assignment_page():
    x=0

course = "C++ 5780"
assignment ="Solver - A"
userEmail = "maccavi2@gmail.com"
password = "123456"
gitHubUrl = "https://github.com/uriel-s/War_game.git"
IDs={"312251846"}

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://104.248.40.179/")
email = driver.find_element_by_name('email')
passw = driver.find_element_by_name('password')
driver.current_url
email.send_keys(userEmail)
passw.send_keys(password)
btn = driver.find_element_by_id("btnLogin")
btn.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
getCursePage(course)
Locate_the_assignment_page(assignment)
result =  Assign_my_code (gitHubUrl,IDs)
print("ok ok ok")#Enter to 'my curses' page and check if the user is registered for the course

  

