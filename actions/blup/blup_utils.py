import re
from selenium.webdriver.common.by import By
from .blup_days.blup_days import BLUP_DAYS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_horse_age(driver):

  age_cell = driver.find_element(
    By.XPATH,
    "//strong[text()='Ikä:']/parent::td"
  )

  age_text = age_cell.text

  if "muutama tunti" in age_text:
    return "foal"

  # Esim. "1 vuosi 6 kuukautta" tai "2 vuotta"
  match = re.search(
    r"(\d+)\s+vu(?:osi|otta)(?:\s+(\d+)\s+kuukautta)?",
    age_text
  )

  if match:
    years = int(match.group(1))
    months = int(match.group(2)) if match.group(2) else 0
    return f"{years}y{months}m"

  # Esim. "6 kuukautta"
  match = re.search(
    r"(\d+)\s+kuukautta",
    age_text
  )

  if match:
    months = int(match.group(1))
    return f"0y{months}m"

  raise ValueError(f"Ikää ei voitu lukea: {age_text}")

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