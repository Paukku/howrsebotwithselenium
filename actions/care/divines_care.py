from .divines_functions import take_walk, get_energy, take_right_special_walk, check_right_special_walk, click_button_by_text
from .care_actions import grooming, give_carrot, feeding, give_water, give_mash, stroke
from selenium.webdriver.common.by import By
from .care_utils import set_simple_walks

def solar_system_care(driver, horse, feed):
  walk = horse.get("walk")
  if not walk:
    return

  set_simple_walks(driver, enabled=True)
  take_right_special_walk(driver)
  default_care(driver, feed, full_oats=True)
  take_right_special_walk(driver)

def nordic_and_space_care(driver, horse, feed ):
  special_walk_round(driver, horse)
  default_care(driver, feed, full_oats=True)
  special_walk_round(driver, horse)

def special_walk_round(driver, horse):
  divine_type = horse.get("group")
  if divine_type == "Nordic":
    gauge_id = "block-mondes-nordiques"

  elif divine_type == "Space":
    gauge_id = "block-alien-gauge"

  points_needed = get_points_needed(driver, gauge_id)
  print(f"Points needed for {divine_type} divine: {points_needed}")
  set_simple_walks(driver, enabled=True)

  if points_needed < 9:
    walk = check_right_special_walk(driver)

    set_simple_walks(driver, enabled=False)
    divineslider = f"walk{walk}Slider"
    divineSubmit = walk

    if points_needed <= 3:
      take_walk(driver, divineslider, divineSubmit, walk, 1)
    else:
      take_walk(driver, divineslider, divineSubmit, walk, 2)
  else:
      take_right_special_walk(driver)

  click_button_by_text(driver, text="Hae palkinto")

def default_care(driver, feed, full_oats=False):
  grooming(driver)
  stroke(driver)
  stroke(driver)
  give_water(driver)
  give_carrot(driver)
  give_mash(driver)
  feeding(driver, feed, full_oats)

def get_points_needed(driver, gauge_id):
  gauge = driver.find_element(
    By.ID,
    gauge_id
  )

  current = int(
    gauge.get_attribute("data-progression")
  )

  goal_text = driver.find_element(
    By.CSS_SELECTOR,
    f"#{gauge_id}-goal span"
  ).text

  goal = int(goal_text.split()[0])

  return goal - current