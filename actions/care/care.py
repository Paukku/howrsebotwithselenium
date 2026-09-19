from utils.randomTime import sleep, random_wait
from actions.care.center import center_not_automated
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from pathlib import Path
from .divines_actions import DIVINE_ACTIONS, REWARD_BUTTONS, DIVINE_CARE, NO_COMPETITION_DIVINES
from .divines_functions import close_popup_if_present, divine_competition
from .care_actions import grooming, feeding, sleeping, do_task
from actions.blup.training import select_auto_training


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
    if divine_type not in NO_COMPETITION_DIVINES:
      divine_competition(driver)

  handle_random_ufo(driver)
  center_not_automated(driver)
  do_task(driver)
  grooming(driver)
  sleeping(driver)
  feeding(driver, feed, skip_feeding=skip_feeding)
  
def train_horse(driver):
  if not is_training_finished(driver, "kestävyys"):
    select_auto_training("kestävyys")
    return

  if not is_training_finished(driver, "nopeus"):
    select_auto_training("nopeus")
    return

  if not is_training_finished(driver, "koulu"):
    select_auto_training("koulu")
    return

  if not is_training_finished(driver, "ravi"):
    select_auto_training("ravi")
    return

  if not is_training_finished(driver, "laukka"):
    select_auto_training("laukka")
    return

  if not is_training_finished(driver, "este"):
    select_auto_training("este")
    return

  return

def is_training_finished(driver, skill):
  rows = driver.find_elements(
    By.CSS_SELECTOR,
    "tr.dashed"
  )

  for row in rows:
    name = row.find_element(
      By.CSS_SELECTOR,
      "td.first"
    ).text.strip().lower()

    if name != skill.lower():
      continue

    tooltip = row.find_element(
      By.CSS_SELECTOR,
      "td:nth-child(2)"
    ).get_attribute("_tooltip")

    return tooltip == "Koulutus on päättynyt!"

  return False

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
    # Odotetaan hetki ilmestyykö UFO
    ufo = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
          (By.CSS_SELECTOR, ".ufo--moving_classic-ufo")
        )
      )

    print("Random UFO löytyi.")

    driver.execute_script("arguments[0].click();", ufo)
    print("UFO klikattu. Odotetaan popupia.")

    # Odotetaan että popup ilmestyy
    WebDriverWait(driver, 3).until(
      EC.visibility_of_element_located((By.ID, "ufoBoxPopup"))
    )
    print("UFO-popup löytyi. Suljetaan.")

    # Suljetaan popup ruksista
    driver.execute_script("""
      const btn = document.querySelector("#ufoBoxPopup .popupview__close");
      if (btn) btn.click();
    """)
    print("Popupin sulkemista odotetaan.")

    WebDriverWait(driver, 3).until(
      EC.invisibility_of_element_located((By.ID, "ufoBoxPopup"))
    )

    print("Random UFO käsitelty.")

  except TimeoutException:
    # UFOa ei tullut, jatketaan normaalisti
    pass
  except Exception as e:
    print(f"Random UFO epäonnistui: {e}")