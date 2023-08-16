###EXTRACTING THE DATA FROM THE HOME PAGE

#--------------Signatories List From First Page-------------#
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

#importing
#from docx import Document

chrome_options = ChromeOptions()
chrome_options.add_argument("executable_path=C:/Users/CHARAN/Documents/KGiSL/cd/chromedriver-win64/chromedriver.exe")

driver = Chrome(options=chrome_options)
driver.get("https://www.iosco.org/about/?subSection=mmou&subSection1=signatories")

# Locate the elements that contain the signatory names using XPath
signatory_list = driver.find_elements(By.XPATH, '//tr//td[1]')
signatory_lists = driver.find_elements(By.XPATH, '//tr//td[2]')
signatory_list3 = driver.find_elements(By.XPATH, '//tr//td[3]')

# Extract the names and print them
for signatory in signatory_list:
    print(signatory.text)

# Extract the names and print them
for signatory in signatory_lists:
    print(signatory.text)

# Extract the names and print them
for signatory in signatory_list3:
    print(signatory.text)

# Extract the texts and concatenate them
all_columns_text = ""
for i in range(len(signatory_list)):
    all_columns_text += signatory_list[i].text + " - " + signatory_lists[i].text + " - " + signatory_list3[i].text + "\n"

# Print all the columns together
print(all_columns_text)

# Close the web browser
#driver.quit()

### TO OBTAIN THE ARTICLES, REPORT AND MEETINGS GIVEN BY THE WEBSITE

#--------------Articles----------------------#

from selenium import webdriver
import time
from selenium.webdriver.common. keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

web = webdriver.Chrome()

# Open the URL
web.get("https://www.iosco.org/media_room/?subsection=articles")
time.sleep(5)
# wait = WebDriverWait(web, 10)
# mediaroom_headline = web.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/ul/li[2]/a')
# article_search = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/ul/li[2]/ul/li[2]/a')))
search = web.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/form/input[2]')
search.send_keys("2022")
search.send_keys(Keys.ENTER)
time.sleep(5)

final= web.find_element(By.LINK_TEXT,'OR01/2021 IOSCO Board Priorities - Work Program 2021-2022').click()

# Close the browser
#web.quit()

#SEARCHING THE PUBLIC REPORTS FROM THE YEAR 2022 AND ALSO ACCESSING A SPECIFIC FILE AUTOMATICALLY

#-----------------Public Reports----------------#

from selenium import webdriver
import time
from selenium.webdriver.common. keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

web = webdriver.Chrome()

# Open the URL
web.get("https://www.iosco.org/publications/?subsection=public_reports")
time.sleep(5)

search_public_reports = web.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/form/input[2]')
search_public_reports.send_keys("Public report 2022")
search_public_reports.send_keys(Keys.ENTER)
time.sleep(5)

public_report= web.find_element(By.LINK_TEXT,'OR01/2022 IOSCO Decentralized Finance Report').click()

# Close the browser
#web.quit()

#DISPLAYING THE ANNUAL REPORTS OF ALL THE YEARS

from selenium import webdriver
import time
from selenium.webdriver.common. keys import Keys

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

web = webdriver.Chrome()

# Open the URL
web.get("https://www.iosco.org/publications/?subsection=annual_reports")
time.sleep(5)


# EXTRACING THE ANNUAL MEETING'S LOCATION AND DATE WHICH HAVE BEEN DONE BEFORE

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

#importing
#from docx import Document

chrome_options = ChromeOptions()
chrome_options.add_argument("executable_path=C:/Users/CHARAN/Documents/KGiSL/cd/chromedriver-win64/chromedriver.exe")

driver = Chrome(options=chrome_options)
driver.get("https://www.iosco.org/events/?subsection=annual_conferences")

# Locate the elements that contain the signatory names using XPath
annual_meeting = driver.find_elements(By.XPATH, '//tr//td[1]')
location = driver.find_elements(By.XPATH, '//tr//td[2]')
date = driver.find_elements(By.XPATH, '//tr//td[3]')


# Extract the names and print them
for data in annual_meeting:
    print(data.text)

# Extract the names and print them
for data in location:
    print(data.text)

# Extract the names and print them
for data in date:
    print(data.text)

# Extract the texts and concatenate them
annual_meetings = ""
for i in range(len(annual_meeting)):
    annual_meetings += annual_meeting[i].text + " - " + location[i].text + " - " + date[i].text + "\n"

# Print all the columns together
print(annual_meetings)

# Close the web browser
driver.quit()
# for data in annual_meeting:
#     print(data.text)
# for data in location:
#     print