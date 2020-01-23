from  selenium import  webdriver

from selenium.webdriver.common.keys import Keys


import  os

from pathlib import  Path
path=str(Path(os.getcwd()).parent)+"\\Drivers\\chromedriver.exe"
print(path)
driver=webdriver.Chrome(executable_path=path)

driver.implicitly_wait(35)

#Pass URL of the application
url="https://in.yahoo.com/?p=us"
driver.get(url)

#maximize the browser

driver.maximize_window()

driver.find_element_by_xpath("//input[@id='uh-search-box']").send_keys("Hello")
ajaxElements=driver.find_elements_by_xpath("//input[@id='uh-search-box']/following-sibling::div//li")

for x in ajaxElements:

    print(x.text)

