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
        browser.get(url + '/create_feeds')
        browser.find_element_by_xpath(".//*[@id='s2id_job_component']").click()
        browser.implicitly_wait(30)
        browser.find_element_by_xpath(".//*[@id='select2-result-label-5']").click()  #Selecting the NVD job component
        browser.find_element_by_xpath(".//*[@id='name']").send_keys("Job1")
        browser.find_element_by_xpath(".//*[@id='steps-uid-0']/div[3]/ul/li[2]/a").click()  #Navigating to next page
        browser.find_element_by_xpath(".//*[@id='s2id_time_scale']").click()  #Selecting 'weekly'
        browser.find_element_by_xpath(".//*[@id='steps-uid-0']/div[3]/ul/li[3]/a").click)   #clicking on Finish

if __name__=='__main__':
    unittest.main()

