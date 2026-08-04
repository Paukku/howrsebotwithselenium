import random
from utils.randomTime import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def click_divine_button(driver, button_id):
  try:
    button = WebDriverWait(driver, 10).until(
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

# ultra power forche horses
def boutonMash(driver):
  click_divine_button(driver, "boutonMash")

#Fire horses
def boutonCarotte(driver):
  click_divine_button(driver, "boutonCarotte")

# fairytales horses
def boutonFairyTalesRead(driver):
  click_divine_button(driver, "boutonFairyTalesRead")

# Musketeer horses
def boutonMusketeerAsk(driver):
  click_divine_button(driver, "boutonMusketeerAsk")

# Celtic horses
def boutonDivination(driver):
  click_divine_button(driver, "boutonDivination")

#Tea horses
def boutonBoire(driver):
  click_divine_button(driver, "boutonBoire")

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

  except Exception as e:
    print(f"UFO action failed: {e}")