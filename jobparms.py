# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:49:06 2020

@author: charlie's angel
"""

class LoginDetails(object):
    def __init__(self):
        self.user_id = 'sample@gmail.com'
        self.user_pass = 'samplepassword'
    
    def setId(self):
        self.user_id = input('\nEmail ID : ')
    
    def setPass(self):
        self.user_pass = input('Passcode : ')
    
    def getId(self):
        return self.user_id
    
    def getPass(self):
        return self.user_pass

    
class SearchCriteria(object):
    def __init__(self):
        self.site_platform = ''
        self.cap_skill = ''
        self.curr_loc = ''
        self.org_cat = ''
        self.ctry_iso_list = {
            'Philippines':'ph',
            'Singapore':'sg',
            'Malaysia':'my',
            'Vietnam':'vn',
            'Thailand':'th',
            'Indonesia':'id'
        }
    
    def setSite(self):
        print('\n** Please note that characters are CASE SENSITIVE for all the following questions **')
        self.site_platform = input('Enter platform website to be searched ("LinkedIn") : ')
    
    def setSkill(self):
        self.cap_skill = input('Enter capability / skillset to be searched : ')
    
    def setLocation(self):
        print('\nCountry Options:')
        print([i for i in self.ctry_iso_list.keys()])
        self.curr_loc = input('Enter country to be searched : ')
    
    def setCategory(self):
        while True: 
            temp_var = input('Enter category type ("Company" / "Employee") : ')
            if temp_var == 'Company' or temp_var == 'Employee':
                self.org_cat = temp_var
                break
            else:
                print('Invalid option. Please try again.')

    def getSite(self):
        return self.site_platform 
    
    def getSkill(self):
        return self.cap_skill
    
    def getLocation(self):
        return self.curr_loc
    
    def getCategory(self):
        return self.org_cat
    
    def getCountryList(self):
        return self.ctry_iso_list
    