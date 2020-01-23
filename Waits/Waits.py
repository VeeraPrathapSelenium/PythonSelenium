from  selenium import  webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import  os

from pathlib import  Path
path=str(Path(os.getcwd()).parent)+"\\Drivers\\chromedriver.exe"
print(path)
driver=webdriver.Chrome(executable_path=path)
#Explicit wait declaration
wait =WebDriverWait(driver,50,poll_frequency=5)


#Pass URL of the application
url="https://in.yahoo.com/?p=us"
driver.get(url)

#maximize the browser

driver.maximize_window()
wait.until(EC.visibility_of_element_located((By.ID,"uh-search-box")))


driver.find_element_by_xpath("//input[@id='uh-search-box']").send_keys("Hello")

wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@id='uh-search-box']/following-sibling::div//li")))
ajaxElements=driver.find_elements_by_xpath("//input[@id='uh-search-box']/following-sibling::div//li")

print((len(ajaxElements)))