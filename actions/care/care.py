from utils.randomTime import sleep, random_wait
from actions.care.center import center_not_automated
from actions.care.feeding import feed_horse
import random
from selenium.webdriver.common.by import By


def take_care_horses(driver, horse):
  sleep()
  count = 0
  is_it_break = 0
  break_after = randomNumberOfHorses()
  driver.get("http://www.howrse.fi/elevage/chevaux/")
  sleep()

  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={horse['id']}")
  sleep()

  while(count < horse["amount"]):
    sleep()
    take_care_one_horse(driver)
    
    count += 1
    is_it_break += 1
    print(count)
    break_after = check_break(break_after, is_it_break)
    driver.find_element(By.ID, "nav-next").click()
    sleep()

def take_care_one_horse(driver):
    center_not_automated(driver)
    do_task(driver)
    grooming(driver)
    sleeping(driver)
    feeding(driver)

def randomNumberOfHorses():
  horse = random.randint(18, 170)
  return horse

def check_break(break_after, is_it_break):
  if is_it_break == break_after:
    print("tauko 5-50 sekuntia")
    random_wait()
    break_after = randomNumberOfHorses()
    return break_after
  else:
    return break_after

def grooming(driver):
  driver.find_element(By.ID, "boutonPanser").click()
  sleep()

def sleeping(driver):
  driver.find_element(By.ID, "boutonCoucher").click()
  sleep()

def feeding(driver):
  driver.find_element(By.ID, "boutonNourrir").click()
  sleep()
  try:
    feed_horse(driver)
    sleep()

  except:
    pass
    sleep()

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