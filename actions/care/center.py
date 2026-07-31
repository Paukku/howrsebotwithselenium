from utils.randomTime import sleep, task_sleep
from selenium.webdriver.common.by import By

def center_automated(driver):
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

  try:
    hoito = driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[5]/div/div/div/div/div/div/div[@id='cheval-inscription']/a")
    hoito.click()
    sleep()
    hoito = driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='centresContent']/table/thead/tr/td[6]/span[2]/span/span[5]/a")
    hoito.click()
    task_sleep()
    task_sleep()
    hoito = driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='centresContent']/table/tbody/tr/td[8]/button")
    hoito.click()
    task_sleep()
    hoito = driver.find_element(By.ID, "boutonCoucher")
    hoito.click()
    sleep()
  except:
    pass


def center_not_automated(driver):

  try:
    klik = driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div/div/div/div/div/div/div[@id='cheval-inscription']/a")
    klik.click()
    task_sleep()
    task_sleep()
    klik = driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/ul/li[@id='tab-box-reserve']/div/a")
    klik.click()
    task_sleep()
    klik = driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='boxContent']/table/tbody/tr[3]/td[10]/button")
    klik.click()
    task_sleep()
  except:
    pass

