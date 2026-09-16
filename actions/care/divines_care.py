from .divines_functions import take_walk, get_energy, take_right_special_walk
from .care_actions import grooming, give_carrot, feeding, give_water, give_mash, stroke
from selenium.webdriver.common.by import By
from .care_utils import set_simple_walks

def solar_system_care(driver, horse, feed):
  walk = horse.get("walk")
  divineslider = "walkvoieLacteeSlider"
  divineSubmit = "voieLactee"
  if not walk:
    return

  set_simple_walks(driver, enabled=True)
  take_right_special_walk(driver)
  default_care(driver, feed, full_oats=True)
  take_right_special_walk(driver)

def nordic_and_space_care(driver, horse, feed ):
  set_simple_walks(driver, enabled=True)
  take_right_special_walk(driver)
  default_care(driver, feed, full_oats=True)
  take_right_special_walk(driver)


def default_care(driver, feed, full_oats=False):
  grooming(driver)
  stroke(driver)
  stroke(driver)
  give_water(driver)
  give_carrot(driver)
  give_mash(driver)
  feeding(driver, feed, full_oats)