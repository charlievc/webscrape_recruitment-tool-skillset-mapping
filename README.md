# webscrape_recruitment-tool-skillset-mapping
 Webscraping Job Portal via Skillset

## Introduction
This serves as a tool for finding companies or people with a specific skillset in mind. It runs on a web browser, conducts filtered search on the indicated job portal, and prints out search results to a csv file -- all done automatically. Though I must say, it is prone to CAPTCHAs as we are technically webcrawling. :)

The creation of this project is as requested by a technical recruiter.

## Project Status
* Initial requirement: Scrape LinkedIn website - Complete
* Scrape Indeed/ Jobstreet/ etc - TBD

## Technologies
* Python 3.7.3
* Selenium Webdriver (ChromeDriver)

## Setup
* Python installed
* Selenium Webdriver installed (the module uses Chrome version)
* Webdriver location: 'C:\Program Files (x86)\chromedriver.exe'

## Getting Started
1. Execute the main script : `$ python main_script.py`
2. Enter the job portal to be searched. For input values, refer to the items inside the parenthesis (For now, the only option is LinkedIn)
```
$ ** Please note that characters are CASE SENSITIVE for all the following questions **
$ Enter platform website to be searched ("LinkedIn") : LinkedIn

```
3. Enter the skill/ tool/ designation to be searched. (ie. 'Data Scientist')
```
$ Enter capability / skillset to be searched : Data Scientist
```
4. Enter the desired country location. For input values, refer to the options displayed on screen. (ie. 'Philippines')
```
$ Country Options:
$ ['Philippines', 'Singapore', 'Malaysia', 'Vietnam', 'Thailand', 'Indonesia']
$ Enter country to be searched : Philippines
```
5. For category type, enter 'Company' (to search for company job posts) or 'Employee' (to search for people), both containing the indicated skillset.
```
$ Enter category type ("Company" / "Employee") : Company
```
6. You will then be asked to enter your username and password to login on the indicated website at item # 2. 
```
$ Email ID : sampleuser@gmail.com
$ Passcode : samplepassword
```

## Sample Output
* Below is a sample CSV output file.

![Alt text](https://github.com/charlievc/webscrape_recruitment-tool-skillset-mapping/blob/master/img_sample/file_csv.jpg)

* Right click the CSV file, select 'Open with', then choose 'Microsoft Office Excel'. 

![Alt text](https://github.com/charlievc/webscrape_recruitment-tool-skillset-mapping/blob/master/img_sample/file_xls.jpg)

* Here's another sample output having 'Java Developer', 'Singapore', and 'Employee' as the filter criteria.

![Alt text](https://github.com/charlievc/webscrape_recruitment-tool-skillset-mapping/blob/master/img_sample/file_emp_xls.jpg)


Aaand we're done! So whether we want to obtain a list of contacts for headhunting purposes, or for mere curiosity regarding skillset analytics, I reckon this tool does the trick. 

Gracias.
