from actions.care.feeding import feed_horse, automated_feed
from utils.randomTime import short_sleep as sleep
from actions.care.divines_functions import click_divine_button
from selenium.webdriver.common.by import By

def click_care_button(driver, button_id):
    driver.find_element(By.ID, button_id).click()
    sleep()

def grooming(driver):
  click_care_button(driver, "boutonPanser")

def sleeping(driver):
  click_care_button(driver, "boutonCoucher")

def give_water(driver):
  click_care_button(driver, "boutonBoire")

def give_carrot(driver):
  click_care_button(driver, "boutonCarotte")

def stroke(driver):
  click_care_button(driver, "boutonCaresser")

def give_mash(driver):
  click_care_button(driver, "boutonMash")

def feeding(driver, feed, full_oats=False):
  driver.find_element(By.ID, "boutonNourrir").click()
  sleep()


  if full_oats:
    feed_horse(driver, full_oats=True)

  elif feed == "normal":
    feed_horse(driver)

  elif feed == "automated":
    automated_feed(driver)

def element_exists(driver, by, value):
  return len(driver.find_elements(by, value)) > 0

def equip_classic_gear(driver):
  if element_exists(
    driver,
    By.CSS_SELECTOR,
    "#specialisationClassique button[type='submit']"
):
    driver.find_element(
      By.CSS_SELECTOR,
      "#specialisationClassique button[type='submit']"
    ).click()

    sleep()

  if element_exists(
    driver,
    By.XPATH,
    "//a[.//span[normalize-space()='Varusta hevonen']]"
  ):
    driver.find_element(
        By.XPATH,
        "//a[.//span[normalize-space()='Varusta hevonen']]"
    ).click()

    sleep()
  else:
    # Jos nappia ei ole, hevonen saattaa olla jo varustettu.
    print("Hevonen on mahdollisesti jo varustettu.")
    return


  click_divine_button(driver, "modele-tapis-classique-1x")

  # Satula
  driver.find_element(
    By.XPATH,
    "//div[contains(@class, 'type')][normalize-space()='Satula']"
  ).click()
  sleep()

  click_divine_button(driver, "modele-selle-classique-3x")
  sleep()

  # Suitset
  driver.find_element(
      By.XPATH,
      "//div[contains(@class, 'type')][normalize-space()='Suitset']"
  ).click()
  sleep()

  click_divine_button(driver, "modele-bride-classique-3x")
  sleep()

  driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Vahvista varusteet']"
  ).click()
  sleep()




def do_task(driver):
  try:
    driver.find_element(By.ID, "boutonMissionEquus").click()
  except:
    try:
      driver.find_element(By.ID, "boutonMissionForet").click()
    except:
      try:
        driver.find_element(By.ID, "boutonMissionMontagne").click()
      except:
        pass
  sleep()