"""Walks and training actions (target: actions/training/training.py)."""

from actions.care.care_utils import click_button_by_id

# Skill name -> the word the horse page uses in its element ids:
#   label cell:      f"{word}Label"            (e.g. enduranceLabel)
#   training button: f"training-{word}-submit" (e.g. training-endurance-submit)
# The order of this dict is the order in which skills are trained.
SKILLS = {
  "kestävyys": "endurance",
  "nopeus": "vitesse",
  "koulu": "dressage",
  "ravi": "trot",
  "laukka": "galop",
  "este": "saut",
}


def forest_walk(driver):
  click_button_by_id(driver, button_id="boutonBalade-foret")
  click_button_by_id(driver, button_id="boutonBalade-foret-rainbow")


def mountain_walk(driver):
  click_button_by_id(driver, button_id="boutonBalade-montagne")


def beach_walk(driver):
  click_button_by_id(driver, button_id="boutonBalade-plage")


def select_auto_training(driver, training):
  if training not in SKILLS:
    raise ValueError(f"Tuntematon koulutus: {training}")
  click_button_by_id(driver, button_id=f"training-{SKILLS[training]}-submit")