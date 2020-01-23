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
url="https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose"
driver.get(url)

wait.until(EC.visibility_of_element_located((By.XPATH,"//th[text()='Company']")))

rowcount=driver.find_elements_by_xpath("//th[text()='Company']/ancestor::table/tbody/tr")

for r in range(1,len(rowcount)):

    colcount=driver.find_elements_by_xpath("//th[text()='Company']/ancestor::table/tbody/tr[{0}]/td".format(r))
    for c in range(1,len(colcount)):
       celldata=driver.find_element_by_xpath("//th[text()='Company']/ancestor::table/tbody/tr[{row}]/td[{col}]".format(row=r,col=c))

       print(celldata.text)