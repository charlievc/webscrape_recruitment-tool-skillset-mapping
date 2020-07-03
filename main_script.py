# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:50:31 2020

@author: charlie's angel
"""

import jobscraper
from datetime import datetime
from jobparms import LoginDetails, SearchCriteria
from accessjobportal import LinkedIn, Google
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def oneLinerSearch(skill,location,category,ctry_iso):
    currentYear = datetime.now().year
    string = 'site:'+ctry_iso[location]+'.'+search.getSite().lower()
    if category == 'Company':
        search_criteria = string+'.com/jobs/view/ '+'\"'+search.getSkill()+'\" '+str(currentYear)
    else: # 'Employee'
        search_criteria = string+'.com/in/ AND '+'\"'+search.getSkill()+'\" '
    return search_criteria



# Set search criteria
search = SearchCriteria()
search.setSite()
search.setSkill()
search.setLocation()
search.setCategory()
search_query = oneLinerSearch(
    search.getSkill(),
    search.getLocation(),
    search.getCategory(),
    search.getCountryList()
    )


# Set login details
login = LoginDetails()
login.setId()
login.setPass()


# Launch Selenium Webdriver
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe',options=chrome_options)
driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')


# Google search relevant items
google_stuff = Google(search_query)
driver.get(google_stuff.getSite())
google_stuff.getSearch(driver)



###
# Scrape google search results
ls_url = jobscraper.Google().getData(driver,search_query) 


# Instantiate job website object.
if search.getSite() == 'LinkedIn':
    jobsite = LinkedIn(login.getId(),login.getPass())
else: 
    pass # TBD (indeed/ monster/ jobstreet)


# Access Job portal website
driver.get(jobsite.getSite())
jobsite.setLogin(driver)



###
# Scrape Job portal results
if search.getSite() == 'LinkedIn':
    obj = jobscraper.LinkedIn()
    if search.getCategory() == 'Company':
        df = obj.getCompData(driver,ls_url) 
    else: # 'Employee'
        df = obj.getEmpData(driver,ls_url) 
else: 
    pass # TBD (indeed/ monster/ jobstreet)


# Close the driver browser window 
driver.close()


# Write dataframe to output file
obj.createCSV(search.getSite(),search.getCategory(),search.getSkill())
