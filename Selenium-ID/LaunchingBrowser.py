from  selenium import  webdriver

from selenium.webdriver.common.keys import Keys

import  os

from pathlib import  Path
path=str(Path(os.getcwd()).parent)+"\\Drivers\\chromedriver.exe"
print(path)
driver=webdriver.Chrome(executable_path=path)

#Pass URL of the application
url="https://demo.nopcommerce.com"
driver.get(url)

#maximize the browser

driver.maximize_window()

driver.find_element_by_link_text("Register").click()

# identify Gender as Male

driver.find_element_by_id("gender-male").click()

# identify the firstname

driver.find_element_by_xpath("//input[@id='FirstName']").send_keys("FirstName")

#Collect all the childern under a parent

childerns=driver.find_elements_by_xpath("//select[@name='DateOfBirthDay']/child::*")
print(childerns)

for element in childerns:

    print(element.text)


print("********************************************")

months=driver.find_elements_by_xpath("//select[@name='DateOfBirthMonth']/option[@value='0']/following-sibling::*")

for month in months:
    print(month.text)
