# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:49:51 2020

@author: charlie's angel
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Google(object):
    def __init__(self):
        self.ls_url = []
    
    def getData(self,driver,query):
        # Process page 1 to 10 only
        for i in range(1,11): 
            # current page
            time.sleep(2)
            print('Page ',i)
            find_urls = driver.find_elements_by_xpath('//div[@class="r"]/a[@href]') # sample HTML nested tags
            filter_urls = [i.get_attribute('href') for i in find_urls if query[5:24] in i.get_attribute('href')] # search_var[5:24] = 'xx.linkedin.com/in/'
            self.ls_url.extend(filter_urls)
            
            # go to next page
            next_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//a[@id="pnnext"]')))
            next_button.click()
            time.sleep(5) 
        return self.ls_url


    
class LinkedIn(object):
    def __init__(self):
        self.df_results = pd.DataFrame()

    def getEmpData(self,driver,ls_url):
        ls_cols = ['Name','Job Title','Company','College','Course','Location','URL']
        self.df_results = self.df_results.reindex(columns=ls_cols)
        for url in ls_url:
            try:
                # current page
                driver.get(url)
                time.sleep(3)
                header1 = driver.find_element_by_xpath('//div[@class="display-flex mt2"]/div[@class="flex-1 mr5"]')
                name = header1.find_element_by_xpath('//*[@class="inline t-24 t-black t-normal break-words"]')
                job = header1.find_element_by_xpath('//*[@class="mt1 t-18 t-black t-normal break-words"]')
                location = header1.find_element_by_xpath('//*[@class="t-16 t-black t-normal inline-block"]')
                header2 = driver.find_element_by_xpath('//div[@class="display-flex mt2"]/div/ul[@class="pv-top-card--experience-list"]')
                company = header2.find_element_by_xpath('//a[@data-control-name="position_see_more"]')

                # scroll page till element found
                while True:
                    try: 
                        edu = driver.find_element_by_id('education-section')
                        driver.execute_script("arguments[0].scrollIntoView();", edu) 
                        break
                    except: 
                        last_height = driver.execute_script("return window.scrollY")
                        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
                        new_height = driver.execute_script("return window.scrollY")
                        if new_height == last_height: # if already reached eof 
                            break

                college = []
                course = []                        
                try:
                    ls_college = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//div[@class="pv-entity__degree-info"]/h3[@class="pv-entity__school-name t-16 t-black t-bold"]')))
                    for i in ls_college:
                        college.append(i.text)
                    ls_course = WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,'//div[@class="pv-entity__degree-info"]/p[@class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"]/span[@class="pv-entity__comma-item"]')))
                    for i in ls_course:
                        course.append(i.text)
                except:
                    college.append('Not Indicated')
                    course.append('Not Indicated')  

                new_row = {
                    'Name':name.text,
                    'Job Title':job.text,
                    'Company':company.text,
                    'College':college,
                    'Course':course,
                    'Location':location.text,
                    'URL':url
                }
                self.df_results = self.df_results.append(new_row,ignore_index=True)
            except:
                pass # do not include pages with issues
        return self.df_results    

    def getCompData(self,driver,ls_url):
        ls_cols = ['Company','Job Position','Seniority Level','Industry','Location','URL']
        self.df_results = self.df_results.reindex(columns=ls_cols)
        for url in ls_url:
            try:
                driver.get(url)
                time.sleep(3)
                see_more_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//button[@aria-label="See more"]')))
                see_more_button.click()
                time.sleep(1)        
                company = driver.find_element_by_xpath('//a[@class="jobs-top-card__company-url ember-view"]')
                jobpos = driver.find_element_by_xpath('//h1[@class="jobs-top-card__job-title t-24"]')

                try: # optional field
                    level = driver.find_element_by_xpath('//p[@class="jobs-box__body js-formatted-exp-body"]')
                    level = level.text
                except:
                    level = 'Not Indicated'

                industry = driver.find_element_by_xpath('//ul[@class="jobs-box__list jobs-description-details__list js-formatted-industries-list"]')
                location = driver.find_element_by_xpath('//span[@class="jobs-top-card__bullet"]')

                new_row = {
                    'Company':company.text,
                    'Job Position':jobpos.text,
                    'Seniority Level':level,
                    'Industry':industry.text,
                    'Location':location.text,
                    'URL':url
                }
                self.df_results = self.df_results.append(new_row,ignore_index=True)                
            except:
                pass # do not include pages with issues
        return self.df_results   
    
    def createCSV(self,site,cat,skill):
        print('\nWriting dataframe to csv file . . .\n')
        filename = 'C:\Desktop\\'+site+'_'+cat+'_'+skill.replace(' ','')+'.csv'
        self.df_results.to_csv(filename,index=False,header=True)        
        print('File successfully saved at '+filename)
