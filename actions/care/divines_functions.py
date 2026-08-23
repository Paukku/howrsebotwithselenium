import random
from utils.randomTime import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def click_divine_button(driver, button_id):
  try:
    button = WebDriverWait(driver, 3).until(
      EC.element_to_be_clickable(
        (By.ID, button_id)
      )
    )

    driver.execute_script(
      "arguments[0].click();",
      button
    )
    sleep()

  except Exception as e:
    print(f"Divine action failed {button_id}: {e}")

def click_button_by_text(driver, text):
  try:
    button = driver.find_element(
      By.XPATH,
      f"//button[.//span[contains(normalize-space(), '{text}')]]"
    )

    driver.execute_script("arguments[0].click();", button)
    sleep()
    return True

  except NoSuchElementException:
    return False

def click_if_enabled(driver, button_id):
  try:
    button = driver.find_element(By.ID, button_id)

    if "action-disabled" in button.get_attribute("class"):
      return False

    driver.execute_script("arguments[0].click();", button)
    sleep()
    return True

  except:
    return False

def click_divine_action(driver, button_id):
  click_divine_button(driver, button_id)

def close_popup_if_present(driver):
  try:
    popup = WebDriverWait(driver, 3).until(
      EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".popupview")
      )
    )

    close_button = popup.find_element(
      By.CSS_SELECTOR,
      ".popupview__close"
    )

    driver.execute_script(
      "arguments[0].click();",
      close_button
    )

    sleep()
    return True

  except:
    return False

#shark horses and egyptian
def scratch_divine(driver):
  try:
    scratch = driver.find_element(
      By.CSS_SELECTOR,
      "[id^='divine-scratch-animation-']"
    )

    driver.execute_script(
      "arguments[0].click();",
      scratch
    )
  except:
    pass

  sleep()
  try:
    claim_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
      (By.CSS_SELECTOR, ".divine-scratch-background button")
      )
    )
    claim_button.click()
  except:
    pass

#Spice horses
def spice_horse(driver):
  for _ in range(2):
    if not click_button_by_text(driver, "Jatka"):
      break

  click_button_by_text(driver, "Hanki")

# Japanese horses
def take_japanese_ufo(driver):
  ufo_number = random.randint(0, 4)

  ufo_id = f"Ufo_{ufo_number}"

  try:
    ufo = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable(
        (By.ID, ufo_id)
      )
    )

    ufo.click()

    WebDriverWait(driver, 10).until(
      EC.invisibility_of_element_located(
        (By.ID, ufo_id)
      )
    )

    sleep()
    sleep()

  except Exception as e:
    print(f"UFO action failed: {e}")

def take_walk(driver, walk, hours):
  click_divine_button(driver, f"boutonBalade-{walk}")
  select_walk_duration(driver, walk, hours)
  click_divine_button(driver, f"walk-{walk}-submit")

def select_walk_duration(driver, walk, hours):
  slider = driver.find_element(
    By.ID,
    f"walkvoieLacteeSlider"
  )
  sleep()

  value = hours * 2
  element = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable(
      (
        By.CSS_SELECTOR,
        f"#{slider.get_attribute('id')} li[data-number='{value}']"
      )
    )
  )
  element.click()
  sleep()

  click_divine_button(driver, button_id="walk-voieLactee-submit")
  sleep()

def get_energy(driver):
  energy = driver.find_element(By.ID, "energie").text
  return int(energy)