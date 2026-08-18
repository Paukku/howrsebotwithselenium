from functools import partial
from .divines_functions import (
  click_divine_action,
  click_if_enabled,
  scratch_divine,
  take_japanese_ufo,
  spice_horse,
  click_button_by_text
)
from .divines_care import solar_system_care


DIVINE_ACTIONS = {
  "UltraPowerForce": partial(click_divine_action, button_id="boutonMash"),
  "Fire": partial(click_divine_action, button_id="boutonCarotte"),
  "Fairy Tales": partial(click_divine_action, button_id="boutonFairyTalesRead"),
  "Musketeers": partial(click_divine_action, button_id="boutonMusketeerAsk"),
  "Celtic": partial(click_divine_action, button_id="boutonDivination"),
  "Tea": partial(click_divine_action, button_id="boutonBoire"),
  "Maori": partial(click_button_by_text, text="Tarkkaile"),

  "Egyptian": scratch_divine,
  "Shark": scratch_divine,
  "Japanese": take_japanese_ufo,
  "Spice": spice_horse,
  
}

REWARD_BUTTONS = {
  "Fire": partial(click_if_enabled,  button_id="boutonFireKdow"),
  "Tea": partial(click_if_enabled, button_id="boutonTeaKdow"),
  "Spice": partial(click_if_enabled, button_id="boutonSpiceKdow"),
  "Marble": partial(click_if_enabled, button_id="boutonRocksKdow"),
  "Hrim": partial(click_if_enabled, button_id="doRosee" ),
  "Celtic": partial(click_button_by_text, text="Hae palkinto"),
  "Fairy Tales": partial(click_button_by_text, text="Hae palkinto"),
  "Art": partial(click_button_by_text, text="Lunasta"),
  "Mystic": partial(click_button_by_text, text="Hanki"),
  "Metallic": partial(click_if_enabled, button_id="boutonMetalsKdow"),
  }

DIVINE_CARE = {
  "Solar System": solar_system_care,
  #"Nordic": nordic_care,
  #"Space": space_care,
  #"Reindeer": reindeer_care,
}