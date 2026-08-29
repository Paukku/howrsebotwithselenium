from actions.care.divines_functions import click_divine_action

def forest_walk(driver):
  # Metsän valinta
  click_divine_action(driver, button_id="boutonBalade-foret")

def mountain_walk(driver):
  # Metsän valinta
  click_divine_action(driver, button_id="boutonBalade-montagne")

def select_auto_training(driver, training):

  if training == "nopeus":
    click_divine_action(
      driver,
      button_id="training-vitesse-submit"
    )

  elif training == "koulu":
    click_divine_action(
      driver,
      button_id="training-dressage-submit"
    )

  elif training == "este":
    click_divine_action(
      driver,
      button_id="training-saut-submit"
    )

  elif training == "kestävyys":
    click_divine_action(
      driver,
      button_id="training-endurance-submit"
    )

  elif training == "laukka":
    click_divine_action(
      driver,
      button_id="training-galop-submit"
      )
    
  elif training == "ravi":
    click_divine_action(
      driver,
      button_id="training-trot-submit"
    )

  else:
    raise ValueError(f"Tuntematon koulutus: {training}")