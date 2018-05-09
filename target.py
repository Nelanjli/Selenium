#target_creation
import os_
import unittest, csv
import HtmlTestRunner
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox(executable_path='/root/bin/geckodriver')
url = "http://havoc.aricentcoe.com:9876/portal"
class Havoc_automation_test(unittest.TestCase):

#------------------------------------ LOGIN to HAVOc !!!-----------------------------------------#
    
    def test_01(self):
        user = []    #Creating the lists           
        password = []
        
        browser.get(url+'/login')    #Opening the Login Page
        with open("/root/nelanjli/Selenium/csv/login_credentials.csv", 'r') as f:     #Reading the csv file 
            reader = csv.reader(f)
            for row in reader:           
                user.append(row[0])
                password.append(row[1])
        browser.find_element_by_id('userName').send_keys(user[0])
        browser.find_element_by_id('password').send_keys(password[0])
        browser.find_element_by_id('logIn').click()
        browser.implicitly_wait(30)
    
#------------------------------------ Creating new Target-----------------------------------------#
     
    def test_02(self):
        target = []
        host = []
        browser.get(url + '/create_assets')
        with open("/root/nelanjli/Selenium/csv/target_name.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                target.append(row[0])
                host.append(row[1])
        #for i in range (0,len(target)):
        #    print(target[i])
        browser.find_element_by_xpath(".//*[@id='s2id_platform']").click()  #selecting the category
        browser.find_element_by_xpath(".//*[@id='select2-result-label-9']").click()  #choosing Target in the Category
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[4]/div[1]/div/input").send_keys(target[0])
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[4]/div[2]/div/div").click()
        browser.find_element_by_xpath("html/body/div[5]/ul/li[3]/div").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[6]/div/label/input").send_keys(host[0])
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[3]/div/div[2]/div[1]/div/div[1]/ul/li[1]").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[3]/a").click()

#------------------------------------ Creating new Version ---------------------------------------#

    def test_03(self):
        target = []
        version = []
        browser.get(url + '/create_assets')
        with open("/root/nelanjli/Selenium/csv/target_name.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                target.append(row[0])
        with open("/root/nelanjli/Selenium/csv/version.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                version.append(row[0])
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[1]/div").click()  #selecting the category
        browser.find_element_by_xpath("html/body/div[4]/ul/li[3]/div").click()  #choosing Version in the Category
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[3]/div/div/input").send_keys(version[0])
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[2]/div/div[2]/div/div[1]/input").send_keys(target[0])  #Searching the target 
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a").click()  #Navigating to next page  
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[3]/div/div[2]/div[1]/div/div[1]/input").send_keys("User 1")    #Sharing
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[3]/a").click()  #Navigating to next page  

#------------------------------------- Creating new Asset --------------------------------------------#

    def test_04(self):
        target = []
        version = []
        asset = []
        description = []
        browser.get(url + '/create_assets')
        with open("/root/nelanjli/Selenium/csv/target_name.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                target.append(row[0])
        with open("/root/nelanjli/Selenium/csv/version.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                version.append(row[0])
      
        with open("/root/nelanjli/Selenium/csv/asset.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                asset.append(row[0])
                description.append(row[1])
      
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[1]/div").click()  #selecting the category
        browser.find_element_by_xpath("html/body/div[4]/ul/li[2]/div").click()  #choosing Asset in the Category
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[2]/div[1]/div/input").send_keys(asset[0])  #Filling up the UID field
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[2]/div[2]/div/textarea").send_keys(description[0])   #filling up the Description field
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[2]/div[3]/div/div").click()  
        browser.find_element_by_xpath("html/body/div[5]/ul/li[1]/div").click()  #Searching the criticality as Low 
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a").click()  #Navigating to next page  
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[2]/div/div[1]/div/div[1]/input").send_keys("2.0")    #Selecting the version
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[2]/div/div[2]/div/div[1]/input").send_keys("vzw-nec2-nova")    #Selecting the target
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a").click()  #Navigating to next page  
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[3]/div/div[2]/div[1]/div/div[1]/input").send_keys("User 1")    #Sharing
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[3]/a").click()  #Navigating to next page  


if __name__=='__main__':
   # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
