import unittest, csv
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *

browser = webdriver.Firefox(executable_path='/root/bin/geckodriver')
#wait = WebDriverWait(browser, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH,"//div")))
url = "http://havoc.aricentcoe.com:9876/portal"
class Havoc_automation_test(unittest.TestCase):

    # LOGIN to HAVOc !!!

    def test_01(self):
        browser.get(url+'/login')
        browser.find_element_by_id('userName').send_keys("admin@aricent.com")
        #email.clear()
        #email.send_keys('admin@aricent.com')
        browser.find_element_by_id('password').send_keys('bewareadmin')
        #password.clear()
        #password.send_keys('bewareadmin')
        browser.find_element_by_id('logIn').click()
        browser.implicitly_wait(30)
        #browser.close() 
    
    # Creating new Tool Instance
     
    def test_02(self):
        browser.get(url + '/create_tools')
        browser.find_element_by_xpath(".//*[@id='s2id_platform']").click()
        browser.implicitly_wait(30)
        #wait = WebDriverWait(browser, 10)
        #element = wait.until(lambda browser: browser.find_element_by_xpath(".//*[@id='select2-result-label-8']"))
        #browser.switch_to.frame(browser.find_element_by_name("platform"))
        #browser.find_element_by_xpath(".//*[@id='select2-result-label-8']").click()
        #browser.switch_to.default_content()
        browser.find_element_by_id("select2-result-label-8").click()
        browser.find_element_by_xpath(".//*[@id='s2id_tool']").click()
        browser.find_element_by_xpath(".//*[@id='select2-result-label-14']").click()
        #platform.select_by_value("1")
        #platform = Select(find_element_by_xpath(".//*[@id='select2-chosen-4']")).select_by_index(0)
        #tool = Select(browser.find_element_by_id("s2id_tool"))
        #tool.select_by_visible_text("NMap").click()
        
        browser.find_element_by_xpath(".//*[@id='name']").send_keys("Tool1")
        browser.find_element_by_xpath(".//*[@id='steps-uid-0']/div[3]/ul/li[2]/a").click()  #Navigating to next page
         
        #Creating the lists
        host = []
        host_user = []
        host_password = []
        arguments = []

        # Reading Data from CSV file
        with open("/root/nelanjli/Selenium/tools_csv.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                host.append(row[0])
                host_user.append(row[1])
                host_password.append(row[2])
                arguments.append(row[3])
       
        host = browser.find_element_by_id("host")
        host.send_keys(host[0])
        host_user = browser.find_element_by_id("host_user")
        host_user.send_keys(host_user[0])
        host_password = browser.find_element_by_id("host_password")
        host_password.send_keys(host_password[0])
        
        browser.find_elements_by_partial_link_text("Next").click()   #Navigating to next page

        arguments = browser.find_element_by_id("arguments")
        arguments.send_keys(arguments[0])
        browser.find_elements_by_partial_link_text("Next").click()   #Navigating to next page

        #browser.implicitly_wait(30)

if __name__=='__main__':
    unittest.main()

