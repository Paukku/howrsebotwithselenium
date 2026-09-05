from actions.care.feeding import feed_horse, automated_feed
from utils.randomTime import short_sleep as sleep
from selenium.webdriver.common.by import By
from .care_utils import click_button_by_id

def grooming(driver):
  click_button_by_id(driver, "boutonPanser")

def sleeping(driver):
  click_button_by_id(driver, "boutonCoucher")

def give_water(driver):
  click_button_by_id(driver, "boutonBoire")

def give_carrot(driver):
  click_button_by_id(driver, "boutonCarotte")

def stroke(driver):
  click_button_by_id(driver, "boutonCaresser")

def give_mash(driver):
  click_button_by_id(driver, "boutonMash")

def feeding(driver, feed, full_oats=False, skip_feeding=False):
  print(skip_feeding)
  if skip_feeding:
    return
  click_button_by_id(driver, "boutonNourrir")
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


  click_button_by_id(driver, "modele-tapis-classique-1x")

  # Satula
  driver.find_element(
    By.XPATH,
    "//div[contains(@class, 'type')][normalize-space()='Satula']"
  ).click()
  sleep()

  click_button_by_id(driver, "modele-selle-classique-3x")
  sleep()

  # Suitset
  driver.find_element(
      By.XPATH,
      "//div[contains(@class, 'type')][normalize-space()='Suitset']"
  ).click()
  sleep()

  click_button_by_id(driver, "modele-bride-classique-3x")
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