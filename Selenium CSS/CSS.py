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

xpath="//a[starts-with(text(),'Register')]"
driver.find_element_by_xpath(xpath).click()

#Click on the Computers
#driver.find_element_by_xpath("(//a[normalize-space(text())='Computers'])[1]").click()
driver.find_element_by_css_selector("input[id='FirstName']").send_keys("Hello")
