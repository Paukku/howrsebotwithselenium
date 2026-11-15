import re

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.random_time import short_sleep
from utils.waits import click_when_ready

from .blup_days.blup_days import BLUP_DAYS

AGE_CELL = (By.XPATH, "//strong[text()='Ikä:']/parent::td")


def parse_age(text):
    """'1 vuosi 6 kuukautta' -> '1y6m', '6 kuukautta' -> '0y6m', 'muutama tunti' -> 'foal'."""
    if "muutama tunti" in text:
        return "foal"
    years = re.search(r"(\d+)\s+vu(?:osi|otta)", text)
    months = re.search(r"(\d+)\s+kuukau(?:si|tta)", text)
    if not (years or months):
        raise ValueError(f"Ikää ei voitu lukea: {text}")
    return f"{int(years[1]) if years else 0}y{int(months[1]) if months else 0}m"


def get_horse_age(driver):
    cell = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AGE_CELL))
    return parse_age(cell.text)


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