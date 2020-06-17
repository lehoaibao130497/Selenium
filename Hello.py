from selenium import webdriver
from time import sleep
import os
import re
import pyautogui
from bs4 import BeautifulSoup
 

class HelloSelenium:
    def __init__(self, url):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito ") #--headless
        self.exec_path = "C:\\Users\\vnzoo\\OneDrive\\Desktop\\Python\\Driver\\chromedriver.exe" 
        self.driver = webdriver.Chrome(executable_path = self.exec_path,options= self.chrome_options)
        self.driver.get(url)

    def get_site_info(self):
        print('URL:', self.driver.current_url)
        # print('Title:', self.driver.title)
        print('Title:', self.driver.title.encode('utf8'))
        sleep(0.5)
        self.driver.save_screenshot(r"C:\Users\vnzoo\OneDrive\Desktop\Python\PyautoGUI\Selenium\Capture\ssss.png")
        # elements = self.driver.find_elements_by_xpath('//*[@id="slingstoneStream-0-Stream"]/ul/li[2]/div/div/div[1]/h3/a/u')
        # content = "".join([element.text for element in elements])
        # text= self.driver.find_element_by_class_name("Trsdu(0.3s) Fw(500)").text
        self.soup = BeautifulSoup(features="html.parser")
        text = self.soup.find('h2', {'class':'page-title'})
        print(text)

        # part = {}
        # i =0
        # for i in range(len(part)):
        #     part[i] = part[i]+1
        # file_name = "part_{}.png".format(part[i])
        # print("Capturing {} ...".format(file_name))

        # self.driver.get_screenshot_as_file(file_name)
        
  
 
if __name__ == '__main__':
    hello = HelloSelenium('https://pypi.org/project/beautifulsoup4/')
    hello.get_site_info()

    # Close driver
    hello.driver.close()