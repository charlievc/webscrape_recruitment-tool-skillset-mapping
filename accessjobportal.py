# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:45:14 2020

@author: charlie's angel
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LinkedIn(object):
    def __init__(self,userid,userpass):
        self.site_url = 'https://www.linkedin.com/login'
        self.userid = userid
        self.userpass = userpass
        
    def getSite(self):
        return self.site_url      
       
    def setLogin(self,driver):
        time.sleep(1)
        temp_user = driver.find_element_by_id('username')
        temp_user.send_keys(self.userid)
        time.sleep(1)
        temp_pass = driver.find_element_by_id('password')
        temp_pass.send_keys(self.userpass)
        time.sleep(1)
        button = '//button[@class="btn__primary--large from__button--floating"]'
        signin_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,button)))
        if signin_button.get_attribute('data-litms-control-urn') == 'login-submit':
            signin_button.send_keys(Keys.RETURN)
        time.sleep(2)


class Google(object):
    def __init__(self,query):
        self.site_url = 'https:www.google.com'
        self.query = query
    
    def getSite(self):
        return self.site_url
    
    def getSearch(self,driver):
        time.sleep(5)
        search_bar = driver.find_element_by_name('q')
        search_bar.send_keys(self.query)
        time.sleep(5)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)
