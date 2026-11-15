from actions.care.care_actions import (
  equip_classic_gear,
  feeding,
  give_carrot,
  give_mash,
  give_water,
  grooming,
  stroke,
)
from actions.care.care_utils import change_specialization
from actions.care.center import change_to_mountain_stable, change_to_own_stable
from utils.random_time import short_sleep as sleep

from ..competitions.competitions import (
  cross_competition,
  dressage_competition,
  jumping_competition,
)
from ..training.training import (
  beach_walk,
  forest_walk,
  mountain_walk,
  select_auto_training,
)
from .blup_utils import age_up, get_blup_days, get_horse_age, get_new_foal_id


def run_blup(driver, amount, start_horse_id, feed):
  horse_id = start_horse_id
  amount = int(amount)
  driver.get("https://www.howrse.fi/elevage/chevaux/")
  sleep()
  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={horse_id}")

  for i in range(amount):

    print(f"=== BLUP {i + 1}/{amount} ===")
    print(f"Hevonen: {horse_id}")

    blup_horse(driver, horse_id, feed)

    print(f"Hevonen {horse_id} BLUPATTU!")

    breed_horse(driver, horse_id)

    horse_id = get_new_foal_id(driver)

    print(f"Seuraava BLUP-hevonen: {horse_id}")

def breed_horse(driver, horse_id):
  input("Astuta ja saa uusi bluppi, mene uuden blupin sivuille ja ikäännytä 1v6kk. Sitten paina enter")

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
  prepare_foal(driver)
  while True:
    age = get_horse_age(driver) 
    
    blup_days = get_blup_days(driver)

    if age == "10y0m":
      print("Hevonen saavutti 10 vuoden iän.")
      breed_horse(driver, horse_id)
      return

    if age not in blup_days:
      print(f"Ikää {age} ei löydy BLUP_DAYS-listasta.")
      return    

    blup_day(driver, blup_days, feed)

def blup_day(driver, blup_days, feed):
  age = get_horse_age(driver) 

  if age not in blup_days:
    print(f"Ikää {age} ei löydy BLUP_DAYS-listasta.")
    return

  # Hoito tehdään aina ensimmäisenä
  grooming(driver)
  give_carrot(driver)

  # Päivän tehtävät oikeassa järjestyksessä
  for task in blup_days[age]:
    print(f"Tehdään: {task}")

    if task == "metsä":
      forest_walk(driver)

    elif task == "vuori":
      mountain_walk(driver)
    
    elif task == "koulu":
      select_auto_training(driver, "koulu")

    elif task == "ranta":
      beach_walk(driver)

    elif task == "laukka":
      select_auto_training(driver, "laukka")

    elif task == "este":
      select_auto_training(driver, "este")

    elif task == "ravi":
      select_auto_training(driver, "ravi")

    elif task == "nopeus":
      select_auto_training(driver, "nopeus")

    elif task == "kestävyys":
      select_auto_training(driver, "kestävyys")

    elif task.startswith("estekisat"):
      _, amount = task.split()
      jumping_competition(driver, int(amount))

    elif task.startswith("koulukisat"):
      _, amount = task.split()
      dressage_competition(driver, int(amount))
    
    elif task.startswith("maastokisat"):
      _, amount = task.split()
      cross_competition(driver, int(amount))

    elif task == "RAVIKISAT" or task == "MAASTOKISAT":
      input("Täytä kisat käsin ja paina Enter jatkaaksesi...")

    elif task == "metsätalli":
      change_to_own_stable(driver)

    elif task == "tallinvaihto":
      change_to_mountain_stable(driver)

    elif task == "varusteet":
      equip_classic_gear(driver)

    elif task == "lajinvaihto":
      change_specialization(driver)

    elif task == "silitä":
      stroke(driver)

    elif task == "ape":
      give_mash(driver)

  #stroke(driver)
  give_water(driver)
  feeding(driver, feed=feed)
  sleep()

  # Päivä loppuun
  age_up(driver)