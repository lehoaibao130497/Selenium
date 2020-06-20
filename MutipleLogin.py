from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from random import randint
import  sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import urllib
from lxml import html
import xlsxwriter

url = "https://finance.yahoo.com/"
# List user and pass login 
userlist = [("vnzoomhoaibao@yahoo.com","Apple0167")]
urls=[]
# Loop login each user
for user,pwd in (userlist):
    print(user,pwd)
    # Step 1) Open Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    exec_path = "C:\\Users\\vnzoo\\OneDrive\\Desktop\\Python\\Driver\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path = exec_path,options=chrome_options)

    # Step 2) Navigate to Facebook
    browser.get(url)
    # username = browser.find_element_by_id("login-username")
    # username.send_keys(user)
    # sleep(randint(1,3))
    # btn_login = browser.find_element_by_id('login-signin')
    # btn_login.click()
    # sleep(randint(1,5))
    # password = browser.find_element_by_name("password")
    # password.send_keys(pwd)
    # sleep(randint(2,5))
    # submit = browser.find_element_by_id("login-signin")
    # sleep(randint(1,4))
    # # Step 4) Click Login
    # submit.click()

    # def verify_login():
    #     try:
    #         browser.find_element_by_id("login-username")
    #         browser.find_element_by_id("login-passwd")
    #         return False
    #     except:
    #         return True

    # if verify_login():
    #     print('Login Success')
        
    # else:
    #     print('Login Failed')

    # # page = urllib.request.urlopen(url)
    # # soup = BeautifulSoup(page.read(), "lxml")
    # # target = soup.find("span", attrs={"class":"_50f6"})
    # # print({target})

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    target = soup.find("span", attrs={"class":"Fz(s)"})
    print(target.text)