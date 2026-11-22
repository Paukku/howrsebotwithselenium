import re

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.random_time import short_sleep
from utils.waits import click_when_ready
from actions.care.care_utils import get_horse_age

from .blup_days.blup_days import BLUP_DAYS




def age_up(driver):
  old_age = get_horse_age(driver)
  click_when_ready(driver, (By.ID, "boutonVieillir"), timeout=3, use_js=True, pause=short_sleep)
  click_when_ready(driver, (By.CSS_SELECTOR, "form#age button[type='submit']"), pause=short_sleep)
  # Fails with TimeoutException if the age does not change
  WebDriverWait(driver, 15, ignored_exceptions=(StaleElementReferenceException,)).until(
    lambda d: get_horse_age(d) != old_age
  )

def get_blup_days(driver):
  breed = get_horse_breed(driver)
  print(breed)

  if breed not in BLUP_DAYS:
    raise ValueError(f"Tuntematon rotu: {breed}")

  return BLUP_DAYS[breed]

def get_horse_breed(driver):
  return driver.find_element(
    By.XPATH,
    "//td[.//strong[normalize-space()='Rotu:']]//a"
  ).text.strip()

def get_new_foal_id(driver):

  url = driver.current_url
  print(f"Nykyinen URL: {url}")
  match = re.search(r"[?&]id=(\d+)", url)

  if not match:
    raise ValueError(f"Hevosen ID:tä ei löytynyt URL-osoitteesta: {url}")

  horse_id = match.group(1)
  print(f"Löydetty hevosen ID: {horse_id}")

  return horse_id