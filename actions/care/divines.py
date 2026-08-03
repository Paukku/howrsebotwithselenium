from utils.randomTime import sleep
from selenium.webdriver.common.by import By

# forche horses
def boutonMash(driver):
  driver.find_element(By.ID, "boutonMash").click()
  sleep()

#Fire horses
def boutonCarotte(driver):
  driver.find_element(By.ID, "boutonCarotte").click()
  sleep()

# fairytales horses
def boutonFairyTalesRead(driver):
  driver.find_element(By.ID, "boutonFairyTalesRead").click()
  sleep()

# Musketeer horses
def boutonMusketeerAsk(driver):
  driver.find_element(By.ID, "boutonMusketeerAsk").click()
  sleep()

# Celtic horses
def boutonDivination(driver):
  driver.find_element(By.ID, "boutonDivination").click()
  sleep()