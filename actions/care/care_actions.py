from actions.care.feeding import feed_horse, automated_feed
from utils.randomTime import short_sleep as sleep
from selenium.webdriver.common.by import By
from .care_utils import click_button_by_id
from utils.waits import click_when_ready, try_click

def grooming(driver):
  click_button_by_id(driver, "boutonPanser")

def sleeping(driver):
  click_button_by_id(driver, "boutonCoucher")

def give_water(driver):
  click_button_by_id(driver, "boutonBoire")

def give_carrot(driver):
  click_button_by_id(driver, "boutonCarotte")

def stroke(driver):
  click_button_by_id(driver, "boutonCaresser")

def give_mash(driver):
  click_button_by_id(driver, "boutonMash")

def feeding(driver, feed, full_oats=False, skip_feeding=False):
  if skip_feeding:
    return
  click_button_by_id(driver, "boutonNourrir")
  sleep()


  if full_oats:
    feed_horse(driver, full_oats=True)

  elif feed == "normal":
    feed_horse(driver)

  elif feed == "automated":
    automated_feed(driver)

def element_exists(driver, by, value):
  return len(driver.find_elements(by, value)) > 0

# Locators (put these near the top of care_actions.py)
SPECIALISATION_SUBMIT = (
    By.CSS_SELECTOR,
    "#specialisationClassique button[type='submit']",
)
EQUIP_LINK = (By.XPATH, "//a[.//span[normalize-space()='Varusta hevonen']]")
SADDLE_TAB = (By.XPATH, "//div[contains(@class, 'type')][normalize-space()='Satula']")
BRIDLE_TAB = (By.XPATH, "//div[contains(@class, 'type')][normalize-space()='Suitset']")
CONFIRM_GEAR = (By.XPATH, "//button[normalize-space()='Vahvista varusteet']")

def equip_classic_gear(driver):
  # Optional step: only present for some horses
  try_click(driver, SPECIALISATION_SUBMIT)

  # If the link never appears, the horse is probably already equipped
  if not try_click(driver, EQUIP_LINK):
    print("Hevonen on mahdollisesti jo varustettu.")
    return

  # From here on every step is required: a missing element raises
  # TimeoutException instead of confirming incomplete gear.
  click_when_ready(driver, (By.ID, "modele-tapis-classique-1x"), use_js=True)

  click_when_ready(driver, SADDLE_TAB)
  click_when_ready(driver, (By.ID, "modele-selle-classique-3x"), use_js=True)

  click_when_ready(driver, BRIDLE_TAB)
  click_when_ready(driver, (By.ID, "modele-bride-classique-3x"), use_js=True)

  click_when_ready(driver, CONFIRM_GEAR)


def get_specialization(driver):
  western = driver.find_elements(
    By.CSS_SELECTOR,
    "#competition a.competition-barrel"
  )

  classic = driver.find_elements(
    By.CSS_SELECTOR,
    "#competition a.competition-trot"
  )

  if western:
    return "western"

  if classic:
    return "classic"

  return None

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