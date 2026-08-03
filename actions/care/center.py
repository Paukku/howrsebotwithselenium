from utils.randomTime import sleep, task_sleep
from selenium.webdriver.common.by import By
from utils.items import has_item

def center_automated(driver):
  if(has_item(driver, "hypnosin peite")):
     print("Älä laita keskukseen")
  else:
    try:
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[5]/div/div/div/div/div/div/div[@id='cheval-inscription']/a").click()
      task_sleep()
      task_sleep()
      driver.find_element(By.ID, "tab-box-reserve").click()
      task_sleep()
      task_sleep()
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='boxContent']/table/tbody/tr[7]/td[9]/button").click()
      task_sleep()
      driver.find_element(By.ID, "boutonCoucher").click()
      sleep()
    except:
      pass

def center_not_automated(driver):
  if(has_item(driver, "hypnosin peite")):
    print("Älä laita keskukseen")
  else:
    try:
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div/div/div/div/div/div/div[@id='cheval-inscription']/a").click()
      task_sleep()
      task_sleep()
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/ul/li[@id='tab-box-reserve']/div/a").click()
      task_sleep()
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='boxContent']/table/tbody/tr[3]/td[10]/button").click()
      task_sleep()
    except:
      pass

