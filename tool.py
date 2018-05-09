import unittest, csv, time
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *

browser = webdriver.Firefox(executable_path='/root/bin/geckodriver')
url = "http://havoc.aricentcoe.com:9876/portal"
class Havoc_automation_test(unittest.TestCase):

#---------------------------------------- LOGIN to HAVOc !!! ------------------------------------------#

    def test_01(self):
        browser.get(url+'/login')
        browser.find_element_by_id('userName').send_keys("admin@aricent.com")
        browser.find_element_by_id('password').send_keys('bewareadmin')
        browser.find_element_by_id('logIn').click()
        browser.implicitly_wait(30)
    
#-------------------------------------- Creating new Tool Instance ------------------------------------#
     
    def test_02(self):
        #Creating the lists
        host = []
        host_user = []
        host_password = []
        arguments = []

        browser.get(url + '/create_tools')
         
        # Reading Data from CSV file
        with open("/root/nelanjli/Selenium/csv/tools_csv.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                host.append(row[0])
                host_user.append(row[1])
                host_password.append(row[2])
                arguments.append(row[3])
        
        browser.find_element_by_xpath(".//*[@id='s2id_platform']").click()
        browser.find_element_by_xpath(".//*[@id='s2id_platform']").click()
        #browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[1]/div").click()
        browser.find_element_by_xpath("html/body/div[4]/ul/li[3]/div").click()
        #browser.find_element_by_xpath(".//*[@id='s2id_tool']").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[2]/div").click()
        browser.find_element_by_xpath("html/body/div[5]/ul/li[4]/div").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[1]/div[4]/input").send_keys("Nmap_test")
        #browser.find_element_by_xpath(".//*[@id='select2-result-label-14']").click()
        #browser.find_element_by_xpath(".//*[@id='name']").send_keys("Tool1")
        browser.find_element_by_xpath(".//*[@id='steps-uid-0']/div[3]/ul/li[2]/a").click()  #Navigating to next page
        browser.find_element_by_id("host").send_keys(host[0])
        browser.find_element_by_id("host_user").send_keys(host_user[0])
        browser.find_element_by_id("host_password").send_keys(host_password[0])
        browser.find_elements_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a")[0].click()   #Navigating to next page
        browser.find_element_by_id("arguments").send_keys(arguments[0])
        browser.find_elements_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[2]/a")[0].click()   #Navigating to next page
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[2]/section[4]/div/div[2]/div[1]/div/div[1]/ul/li[1]").click()
        browser.find_element_by_xpath("html/body/div[1]/div[3]/div/div[1]/div[3]/div/div/form/div/div[3]/ul/li[3]/a").click()


#--------------------------------------- Main function -------------------------------------------------#

if __name__=='__main__':
    unittest.main()
