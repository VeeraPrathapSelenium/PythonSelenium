from  selenium import  webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


import  os

from pathlib import  Path
path=str(Path(os.getcwd()).parent)+"\\Drivers\\chromedriver.exe"
print(path)
driver=webdriver.Chrome(executable_path=path)
#Explicit wait declaration
wait =WebDriverWait(driver,20,poll_frequency=5)


#Pass URL of the application
url="https://jqueryui.com/"
driver.get(url)

#maximize the browser

driver.maximize_window()

#wait till the element is visible
droppable=driver.find_element_by_xpath("//a[text()='Droppable']")
wait.until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Droppable']")))
#droppable.find_element_by_tag_name("iframe")
actions=ActionChains(driver)


actions.move_to_element(droppable).click()
actions.perform()
wait.until(EC.visibility_of_element_located((By.XPATH,"//iframe")))

frame=driver.find_element_by_xpath("//iframe")
driver.switch_to.frame(frame)


src=driver.find_element_by_xpath("//div[@id='draggable']")
dest=driver.find_element_by_xpath("//div[@id='droppable']")

actions.drag_and_drop(src,dest)

actions.perform()