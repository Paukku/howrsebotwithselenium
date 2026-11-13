from selenium.webdriver.common.by import By
from actions.care.center import select_right_stable
from actions.care.care_actions import grooming, feeding, sleeping, give_carrot, give_water, stroke, give_mash, equip_classic_gear
from actions.training.training import select_auto_training
from actions.care.care_utils import get_energy, set_automates
from utils.randomTime import short_sleep as sleep

def run_training(driver, amount, horse_id, feed):
  amount = int(amount)
  driver.get("http://www.howrse.fi/elevage/chevaux/")
  sleep()

  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={horse_id}")
  sleep()
  set_automates(driver, "walk", enabled=True)
  set_automates(driver, "training", enabled=True)
  set_automates(driver, "competition", enabled=True)

  for i in range(amount):
    print(f"=== Koulutus {i + 1}/{amount} ===")
  
    select_right_stable(driver)
    grooming(driver)
    train_horse(driver)
    give_water(driver)
    feeding(driver, feed=feed)
    check_energy(driver)
    driver.find_element(By.ID, "nav-next").click()

def train_horse(driver):
  if not is_training_finished(driver, "kestävyys"):
    select_auto_training(driver, "kestävyys")
    return

  if not is_training_finished(driver, "nopeus"):
    select_auto_training(driver, "nopeus")
    return

  if not is_training_finished(driver, "koulu"):
    select_auto_training(driver, "koulu")
    return

  if not is_training_finished(driver, "ravi"):
    check_need_carrot(driver)
    select_auto_training(driver, "ravi")
    return

  if not is_training_finished(driver, "laukka"):
    check_need_carrot(driver)
    select_auto_training(driver, "laukka")
    return

  if not is_training_finished(driver, "este"):
    check_need_carrot(driver)
    select_auto_training(driver, "este")
    return
  
  return

def check_need_carrot(driver):
  energy = get_energy(driver)
  if energy < 99:
    give_carrot(driver)

def check_energy(driver):
  energy = get_energy(driver)
  if energy < 20:
    stroke(driver)

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