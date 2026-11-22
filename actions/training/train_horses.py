"""Training run for many horses (target: actions/training/train_horses.py)."""

from selenium.webdriver.common.by import By

from actions.care.care_actions import (
    do_task,
    feeding,
    give_carrot,
    give_water,
    grooming,
    sleeping,
    stroke,
)
from actions.care.care_utils import get_energy, set_automates, get_horse_age
from actions.care.center import move_to_stable
from actions.training.horse_decision import (
    Action,
    HorseState,
    age_in_months,
    plan_horse,
)
from actions.training.state_readers import (
    get_incomplete_skills,
    get_stable,
    walks_left,
)
from actions.training.training import forest_walk, mountain_walk, select_auto_training
from utils.random_time import short_sleep as sleep
from utils.waits import click_when_ready

# These trainings need a full energy bar, so the horse gets a carrot first
CARROT_SKILLS = {"ravi", "laukka", "este"}
NEXT_HORSE_BUTTON = (By.ID, "nav-next")


def run_training(driver, amount, horse_id, feed, pizkunen_owner):
  """Train `amount` horses, one action per horse, starting from horse_id.

  The horses are expected to be in age order (youngest first), so the run
  ends at the first horse that is 24y10m or older.
  Returns the number of horses that were processed.
  """
  amount = int(amount)
  driver.get("http://www.howrse.fi/elevage/chevaux/")
  sleep()

  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={horse_id}")
  sleep()
  set_automates(driver, "walk", enabled=True)
  set_automates(driver, "training", enabled=True)
  set_automates(driver, "competition", enabled=True)

  for i in range(amount):
    print(f"=== Koulutus {i + 1}/{amount} ===")
    plan = plan_horse(read_state(driver))
    print(f"Suunnitelma: {plan.action.value}, talli: {plan.move_to}, taito: {plan.skill}")

    if plan.action == Action.STOP:
      print(f"Koulutus päättyi hevoseen {i + 1}/{amount} (24y10m): käsiteltiin {i} hevosta")
      return i

    if plan.move_to:
      move_to_stable(driver, plan.move_to, pizkunen_owner)

    grooming(driver)
    run_action(driver, plan)
    give_water(driver)
    feeding(driver, feed=feed)
    check_energy(driver)
    sleeping(driver)

    if i < amount - 1:
      click_when_ready(driver, NEXT_HORSE_BUTTON)

  return amount


def read_state(driver):
  """Read everything plan_horse needs from the horse page."""
  # get_horse_age waits for the page, so the other readers can run right after it
  age = get_horse_age(driver)
  stable = get_stable(driver)
  return HorseState(
    age_months=age_in_months(age),
    in_center=stable is not None,
    stable=stable,
    forest_walks_left=walks_left(driver, "forest"),
    mountain_walks_left=walks_left(driver, "mountain"),
    incomplete_skills=get_incomplete_skills(driver),
    # TODO: read can_compete_for_skills when the competition phase exists.
    # Until then horses walk instead of being sent to a missing action.
    can_compete_for_skills=False,
  )


def run_action(driver, plan):
  if plan.action == Action.FOREST_WALKS:
    forest_walk(driver)
  elif plan.action == Action.MOUNTAIN_WALKS:
    mountain_walk(driver)
  elif plan.action == Action.TRAIN_SKILL:
    train_skill(driver, plan.skill)
  elif plan.action == Action.COMPETE:
    # TODO: specialise, equip and compete. Until then use the flow's fallback.
    print("Kisavaihetta ei ole vielä toteutettu: tehdään tehtävä.")
    do_task(driver)
  else:
    raise ValueError(f"Tuntematon toiminto: {plan.action}")


def train_skill(driver, skill):
  if skill in CARROT_SKILLS:
    check_need_carrot(driver)
  select_auto_training(driver, skill)


def check_need_carrot(driver):
  if get_energy(driver) < 99:
    give_carrot(driver)


def check_energy(driver):
  if get_energy(driver) < 20:
    stroke(driver)