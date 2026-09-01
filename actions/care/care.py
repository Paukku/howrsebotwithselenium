from utils.randomTime import sleep, random_wait
from actions.care.center import center_not_automated
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from pathlib import Path
from .divines_actions import DIVINE_ACTIONS, REWARD_BUTTONS, DIVINE_CARE
from .divines_functions import close_popup_if_present
from .care_actions import grooming, feeding, sleeping, do_task

BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(BASE_DIR / "data" / "divines.json", encoding="utf-8") as f:
    DIVINES = json.load(f)

def take_care_horses(driver, feeding, horse, skip_feeding):
  sleep()
  count = 0
  is_it_break = 0
  break_after = randomNumberOfHorses()
  driver.get("http://www.howrse.fi/elevage/chevaux/")
  sleep()

  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={horse['id']}")
  sleep()

  while(count < horse["amount"]):   
    take_care_one_horse(driver, feeding, skip_feeding)
    
    count += 1
    is_it_break += 1
    print(count)
    break_after = check_break(break_after, is_it_break)
    driver.find_element(By.ID, "nav-next").click()
    sleep()

def take_care_one_horse(driver, feed, skip_feeding):
  horse_name = get_horse_name(driver)

  horse = DIVINES.get(horse_name)

  if horse:
    divine_type = horse["group"]
    do_divine_action(driver, divine_type)

    rules = horse.get("rules", [])

    if "skip_normal_care" in rules:
      if "skip_divine_care" not in rules:
        care_divine = DIVINE_CARE.get(divine_type)

        if care_divine:
          care_divine(driver, horse, feed)
        return

  handle_random_ufo(driver)
  center_not_automated(driver)
  do_task(driver)
  grooming(driver)
  sleeping(driver)
  print(skip_feeding)
  feeding(driver, feed, skip_feeding=skip_feeding)
  
def do_divine_action(driver, divine_type):
  print(divine_type)
  action = DIVINE_ACTIONS.get(divine_type)
  reward = REWARD_BUTTONS.get(divine_type)

  if action:
    action(driver)
  if reward:
    claimed = reward(driver)

    if claimed:
      close_popup_if_present(driver)

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

def get_horse_name(driver):
  horse_name = driver.find_element(By.CSS_SELECTOR, "h1.horse-name a").text
  return horse_name

def get_divine_type(horse_name):
  return DIVINES.get(horse_name)

def handle_random_ufo(driver):
  try:
    ufo = WebDriverWait(driver, 2).until(
      EC.element_to_be_clickable(
        (By.ID, "Ufo_0")
      )
    )

    ufo.click()

    close_popup_if_present(driver)

  except TimeoutException:
    pass