from utils.randomTime import sleep, random_wait
from actions.care.center import center_not_automated
from actions.care.feeding import feed_horse, automated_feed
import random
from selenium.webdriver.common.by import By
import json
from pathlib import Path
from .divines_functions import DIVINE_ACTIONS

BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(BASE_DIR / "data" / "divines.json", encoding="utf-8") as f:
    DIVINES = json.load(f)

def take_care_horses(driver, feeding, horse):
  sleep()
  count = 0
  is_it_break = 0
  break_after = randomNumberOfHorses()
  driver.get("http://www.howrse.fi/elevage/chevaux/")
  sleep()

  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={horse['id']}")
  sleep()

  while(count < horse["amount"]):   
    take_care_one_horse(driver, feeding)
    
    count += 1
    is_it_break += 1
    print(count)
    break_after = check_break(break_after, is_it_break)
    driver.find_element(By.ID, "nav-next").click()
    sleep()

def take_care_one_horse(driver, feed):
  horse_name = get_horse_name(driver)

  horse = DIVINES.get(horse_name)

  if horse:
    divine_type = horse["group"]
    do_divine_action(driver, divine_type)

    rules = horse.get("rules", [])

    if "skip_normal_care" in rules:
      return

  center_not_automated(driver)
  do_task(driver)
  grooming(driver)
  sleeping(driver)
  feeding(driver, feed)
  

def do_divine_action(driver, divine_type):
  print(divine_type)
  action = DIVINE_ACTIONS.get(divine_type)

  if action:
    action(driver)

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

def feeding(driver, feed):
  driver.find_element(By.ID, "boutonNourrir").click()
  sleep()
  if feed == 'normal':
    try:
      feed_horse(driver)
      sleep()

    except:
      pass
      sleep()

  if feed == "automated":
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

def get_horse_name(driver):
  horse_name = driver.find_element(By.CSS_SELECTOR, "h1.horse-name a").text
  return horse_name

def get_divine_type(horse_name):
  return DIVINES.get(horse_name)