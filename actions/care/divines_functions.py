import random
from random import choice

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from actions.care.care_actions import get_specialization
from actions.competitions.competitions import (
  barrel_competition,
  cross_competition,
  cutting_competition,
  dressage_competition,
  galop_competition,
  jumping_competition,
  reining_competition,
  trail_competition,
  trot_competition,
  western_pleasure_competition,
)
from utils.random_time import sleep

from .care_utils import (
  click_button_by_id,
  click_button_by_text,
)
from utils.waits import try_click

POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "#popupSpecialActionBox .popupview__close")
SCRATCH_CARD = "[id^='divine-scratch-animation-']"
CLAIM_BUTTON = (By.CSS_SELECTOR, ".divine-scratch-background button")


def close_popup_if_present(driver):
  try:
    close_button = WebDriverWait(driver, 2).until(
      EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#popupSpecialActionBox .popupview__close")
      )
    )

    driver.execute_script("arguments[0].click();", close_button)
    return True

  except TimeoutException:
    return False

#shark horses and egyptian
def scratch_divine(driver):
    """Scratch the divine's scratch card if there is one, then claim the reward."""
    cards = driver.find_elements(By.CSS_SELECTOR, SCRATCH_CARD)
    if cards:
        driver.execute_script("arguments[0].click();", cards[0])
        sleep()

    # After scratching the claim button takes a moment to appear. If nothing
    # was scratched, only check briefly for a reward left over from earlier.
    try_click(driver, CLAIM_BUTTON, timeout=10 if cards else 2)

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

def take_walk(driver, divineslider, divineSubmit, walk, hours):
  click_button_by_id(driver, f"boutonBalade-{walk}")
  select_walk_duration(driver, divineslider, divineSubmit, hours)

def select_walk_duration(driver, divineslider, divineSubmit, hours):
  slider = driver.find_element(
    By.ID,
    divineslider
  )
  sleep()
  print(f"slider id: {slider.get_attribute('id')}")

  value = hours * 2
  print(f"divineslider: {divineslider}")
  print(f"slider id: {slider.get_attribute('id')}")
  print(f"divineSubmit: {divineSubmit}")
  print(f"value: {value}")
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

  click_button_by_id(driver, button_id=f"walk-{divineSubmit}-submit")
  sleep()

def take_right_special_walk(driver):
  walk = find_right_special_walk(driver)

  if not walk:
    return False

  driver.execute_script(
    "arguments[0].click();",
    walk
  )

  sleep()
  return True

def find_right_special_walk(driver):
  walks = driver.find_elements(
    By.CSS_SELECTOR,
    "a[baladespeciale='1']"
  )

  for walk in walks:
    tooltip = walk.get_attribute("_tooltip")

    if "<b>+</b>" in tooltip:
      return walk

  print("Oikeaa erikoislenkkiä ei löytynyt.")
  return False

def check_right_special_walk(driver):

  walks = driver.find_elements(
    By.CSS_SELECTOR,
    "a[baladespeciale='1']"
  )

  for walk in walks:
    tooltip = walk.get_attribute("_tooltip")

    if "<b>+</b>" in tooltip:
      walk_id = walk.get_attribute("id")
      return walk_id.removeprefix("boutonBalade-")

  print("Oikeaa erikoislenkkiä ei löytynyt.")
  return False

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
      trot_competition,
      dressage_competition,
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