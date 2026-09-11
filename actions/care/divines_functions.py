import random
from utils.randomTime import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .care_utils import click_button_by_id, click_button_by_text, click_link_by_text, click_if_enabled
from random import choice
from actions.blup.competitions import (
  jumping_competition,
  cross_competition,
  dressage_competition,
  trot_competition,
  galop_competition,
  barrel_competition,
  cutting_competition,
  trail_competition,
  reining_competition,
  western_pleasure_competition
)
from actions.care.care_actions import get_specialization
from selenium.webdriver.common.action_chains import ActionChains

def close_popup_if_present(driver):
  try:
    close_button = WebDriverWait(driver, 2).until(
      EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#popupSpecialActionBox .popupview__close")
      )
    )

    driver.execute_script("arguments[0].click();", close_button)
    return True

  except:
    return False

#shark horses and egyptian
def scratch_divine(driver):
  try:
    scratch = driver.find_element(
      By.CSS_SELECTOR,
      "[id^='divine-scratch-animation-']"
    )

    driver.execute_script(
      "arguments[0].click();",
      scratch
    )
  except:
    pass

  sleep()
  try:
    claim_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
      (By.CSS_SELECTOR, ".divine-scratch-background button")
      )
    )
    claim_button.click()
    sleep()
  except:
    pass

#Spice horses
def spice_horse(driver):
  for _ in range(2):
    if not click_button_by_text(driver, "Jatka"):
      break

  click_button_by_text(driver, "Hanki")

# Japanese horses
def take_japanese_ufo(driver):
  ufo_number = random.randint(0, 4)

  ufo_id = f"Ufo_{ufo_number}"

  try:
    ufo = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable(
        (By.ID, ufo_id)
      )
    )

    driver.execute_script(
      "arguments[0].click();",
      ufo
    )

    WebDriverWait(driver, 10).until(
      EC.invisibility_of_element_located(
        (By.ID, ufo_id)
      )
    )
    sleep()
    click_outside_popup(driver)
    sleep()

  except Exception as e:
    print(f"UFO action failed: {e}")

def take_walk(driver, walk, hours):
  click_button_by_id(driver, f"boutonBalade-{walk}")
  select_walk_duration(driver, walk, hours)
  click_button_by_id(driver, f"walk-{walk}-submit")

def select_walk_duration(driver, walk, hours):
  slider = driver.find_element(
    By.ID,
    f"walkvoieLacteeSlider"
  )
  sleep()

  value = hours * 2
  element = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable(
      (
        By.CSS_SELECTOR,
        f"#{slider.get_attribute('id')} li[data-number='{value}']"
      )
    )
  )
  element.click()
  sleep()

  click_button_by_id(driver, button_id="walk-voieLactee-submit")
  sleep()

def get_energy(driver):
  energy = driver.find_element(By.ID, "energie").text
  return int(energy)

def click_outside_popup(driver):
  try:
    ActionChains(driver) \
      .move_by_offset(150, 90) \
      .click() \
      .perform()

    sleep()
    return True
  except Exception as e:
    print(f"Popupin sulkeminen epäonnistui: {e}")

  sleep()

def divine_competition(driver):
  specialization = get_specialization(driver)
  print(f"Divine kilpailu: {specialization}")

  if specialization == "classic":
    competitions = [
      jumping_competition,
      cross_competition,
      dressage_competition,
      trot_competition,
      galop_competition,
    ]

  elif specialization == "western":
    competitions = [
      barrel_competition,
      cutting_competition,
      trail_competition,
      reining_competition,
      western_pleasure_competition,
    ]

  else:
    print("Ei erikoistumista → ei kisata")
    return

  competition = choice(competitions)
  print(f"Suoritetaan divine kilpailu: {competition.__name__}")
  competition(driver, 6)