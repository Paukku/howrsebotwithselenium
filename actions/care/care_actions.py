from actions.care.feeding import feed_horse, automated_feed
from utils.randomTime import sleep
from selenium.webdriver.common.by import By

def click_care_button(driver, button_id):
    driver.find_element(By.ID, button_id).click()
    sleep()

def grooming(driver):
  click_care_button(driver, "boutonPanser")

def sleeping(driver):
  click_care_button(driver, "boutonCoucher")

def give_water(driver):
  click_care_button(driver, "boutonBoire")

def give_carrot(driver):
  click_care_button(driver, "boutonCarotte")

def stroke(driver):
  click_care_button(driver, "boutonCaresser")

def give_mash(driver):
  click_care_button(driver, "boutonMash")

def feeding(driver, feed, full_oats=False):
  driver.find_element(By.ID, "boutonNourrir").click()
  sleep()
  print(full_oats)

  if full_oats:
    feed_horse(driver, full_oats=True)

  elif feed == "normal":
    feed_horse(driver)

  elif feed == "automated":
    automated_feed(driver)
    

def do_task(driver):
  try:
    driver.find_element(By.ID, "boutonMissionEquus").click()
  except:
    try:
      driver.find_element(By.ID, "boutonMissionForet").click()
    except:
      try:
        driver.find_element(By.ID, "boutonMissionMontagne").click()
      except:
        pass
  sleep()