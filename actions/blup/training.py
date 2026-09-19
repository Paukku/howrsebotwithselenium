from actions.care.divines_functions import click_button_by_id

def forest_walk(driver):
  # Metsän valinta
  click_button_by_id(driver, button_id="boutonBalade-foret")
  click_button_by_id(driver, button_id="boutonBalade-foret-rainbow")

def mountain_walk(driver):
  # Metsän valinta
  click_button_by_id(driver, button_id="boutonBalade-montagne")

def beach_walk(driver):
  click_button_by_id(driver, button_id="boutonBalade-plage")

def select_auto_training(driver, training):

  if training == "nopeus":
    click_button_by_id(
      driver,
      button_id="training-vitesse-submit"
    )

  elif training == "koulu":
    click_button_by_id(
      driver,
      button_id="training-dressage-submit"
    )

  elif training == "este":
    click_button_by_id(
      driver,
      button_id="training-saut-submit"
    )

  elif training == "kestävyys":
    click_button_by_id(
      driver,
      button_id="training-endurance-submit"
    )

  elif training == "laukka":
    click_button_by_id(
      driver,
      button_id="training-galop-submit"
      )
    
  elif training == "ravi":
    click_button_by_id(
      driver,
      button_id="training-trot-submit"
    )

  else:
    raise ValueError(f"Tuntematon koulutus: {training}")