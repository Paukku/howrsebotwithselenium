from .divines_functions import take_walk, get_energy
from .care_actions import grooming, give_carrot, feeding, give_water, give_mash, stroke


def solar_system_care(driver, horse, feed):
  walk = horse.get("walk")
  if not walk:
    return

  take_walk(driver, walk, 5)
  default_care(driver, feed, full_oats=True)
  take_walk(driver, walk, 5)

def nordic_care(driver, horse, feed ):
  walk = horse.get("walk")
  if not walk:
    return
  
  energy = get_energy(driver)
  if energy >= 95:
    take_walk(driver, walk, 3)
  else:
    take_walk(driver, walk, 2)

  default_care(driver, full_oats=True)

  if energy >= 95:
    take_walk(driver, walk, 3)
  else:
    take_walk(driver, walk, 2)

def default_care(driver, feed, full_oats=False):
  grooming(driver)
  stroke(driver)
  stroke(driver)
  give_water(driver)
  give_carrot(driver)
  give_mash(driver)
  feeding(driver, feed, full_oats)