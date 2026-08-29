import re
from selenium.webdriver.common.by import By
from actions.care.care_actions import grooming, give_carrot, feeding, give_water, equip_classic_gear
from .blup_days import BLUP_DAYS
from .training import forest_walk, mountain_walk, select_auto_training
from utils.randomTime import short_sleep as sleep
from .competitions import jumping_competition
from actions.care.center import change_to_own_stable, change_to_mountain_stable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_blup(driver, amount, start_horse_id, feed):
  horse_id = start_horse_id
  amount = int(amount)
  driver.get("http://www.howrse.fi/elevage/chevaux/")
  sleep()

  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={horse_id}")
  sleep()

  for i in range(amount):

    print(f"=== BLUP {i + 1}/{amount} ===")
    print(f"Hevonen: {horse_id}")
    sleep()

    blup_horse(driver, horse_id, feed)

    print(f"Hevonen {horse_id} BLUPATTU!")

    breed_horse(driver, horse_id)

    horse_id = get_new_foal_id(driver)

    print(f"Seuraava BLUP-hevonen: {horse_id}")

def breed_horse(driver, horse_id):
  input(f"Astuta ja saa uusi bluppi, mene uuden blupin sivuille ja ikäännytä 1v6kk. Sitten paina enter")

def get_new_foal_id(driver):

  url = driver.current_url
  print(f"Nykyinen URL: {url}")
  match = re.search(r"[?&]id=(\d+)", url)

  if not match:
    raise ValueError(f"Hevosen ID:tä ei löytynyt URL-osoitteesta: {url}")

  horse_id = match.group(1)
  print(f"Löydetty hevosen ID: {horse_id}")

  return horse_id

def prepare_foal(driver):

  while True:

    age = get_horse_age(driver)

    print(f"Varsan ikä: {age}")

    if age == "0y6m":
      print("Varsan alkuvaihe valmis.")
      return

    if age not in ["foal", "0y2m", "0y4m"]:
      return

    grooming(driver)
    age_up(driver)

def blup_horse(driver, horse_id, feed):
  while True:

    age = get_horse_age(driver)

    prepare_foal(driver)

    if age == "10y0m":
      print("Hevonen saavutti 10 vuoden iän.")
      breed_horse(driver, horse_id)
      return

    if age not in BLUP_DAYS:
      print(f"Ikää {age} ei löydy BLUP_DAYS-listasta.")
      return

    if age not in BLUP_DAYS:
      print("BLUP valmis!")
      return

    blup_day(driver, feed)

def blup_day(driver, feed):
  
  age = get_horse_age(driver)

  print(f"Hevosen ikä: {age}")

  if age not in BLUP_DAYS:
    print(f"Ikää {age} ei löydy BLUP_DAYS-listasta.")
    return

  # Hoito tehdään aina ensimmäisenä
  grooming(driver)
 # give_carrot(driver)

  # Päivän tehtävät oikeassa järjestyksessä
  for task in BLUP_DAYS[age]:
    print(f"Tehdään: {task}")

    if task == "metsä":
      forest_walk(driver)

    elif task == "vuori":
      mountain_walk(driver)
    
    elif task == "koulu":
      select_auto_training(driver, "koulu")

    elif task == "laukka":
      select_auto_training(driver, "laukka")

    elif task == "este":
      select_auto_training(driver, "este")

    elif task == "nopeus":
      select_auto_training(driver, "nopeus")

    elif task == "kestävyys":
      select_auto_training(driver, "kestävyys")

    elif task.startswith("estekisat"):
      _, amount = task.split()
      jumping_competition(driver, int(amount))

    elif task == "RAVIKISAT":
      input("Täytä ravikisat käsin ja paina Enter jatkaaksesi...")

    elif task == "metsätalli":
      change_to_own_stable(driver)
      input("Laitettiinko talliin?")

    elif task == "tallinvaihto":
      change_to_mountain_stable(driver)

    elif task == "varusteet":
      equip_classic_gear(driver)

  give_water(driver)
  feeding(driver, feed=feed)

  # Päivä loppuun
  age_up(driver)

def age_up(driver):

  try:
    button = WebDriverWait(driver, 3).until(
      EC.element_to_be_clickable(
        (By.ID, "boutonVieillir")
      )
    )
 
    driver.execute_script(
      "arguments[0].click();",
      button
    )
    sleep()
 
  except Exception as e:
    print(f"Divine action failed boutonVieillir: {e}")


  driver.find_element(
    By.CSS_SELECTOR,
    "form#age button[type='submit']"
  ).click()

  sleep()

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