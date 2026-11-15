from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.random_time import sleep
from utils.waits import try_click


def click_button_by_id(driver, button_id):
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

def click_link_by_text(driver, text, timeout=3):
    locator = (By.XPATH, f"//a[contains(normalize-space(), '{text}')]")
    return try_click(driver, locator, timeout=timeout, use_js=True)

def click_if_enabled(driver, button_id):
  """Click the button unless it is missing or marked as disabled."""
  buttons = driver.find_elements(By.ID, button_id)
  if not buttons:
    return False

  button = buttons[0]
  # The page marks disabled buttons with a CSS class, not the disabled attribute
  if "action-disabled" in (button.get_attribute("class") or ""):
    return False

  driver.execute_script("arguments[0].click();", button)
  sleep()
  return True

def set_automates(driver, automate, enabled):
  title = driver.find_element(By.ID, f"{automate}-head-title")

  button = title.find_element(
    By.CSS_SELECTOR,
    "a.widget-action.config.vip"
  )

  is_enabled = "on" in button.get_attribute("class").split()

  if is_enabled == enabled:
    return

  button.click()
  sleep()

def get_energy(driver):
  energy = driver.find_element(By.ID, "energie").text
  return int(energy)

def change_specialization(driver):

  # 1. Avaa toimintovalikko
  driver.find_element(
    By.CSS_SELECTOR,
    "div.options-button button"
  ).click()

  sleep()

  # 2. Avaa Muokkaa profiilia
  click_link_by_text(
    driver,
    "Muokkaa profiilia"
  )

  sleep()

  # 3. Valitse Lännenratsastus
  click_button_by_id(
    driver,
    "horseNameRespecialisationWestern"
  )

  sleep()

  # 4. Vahvista muutos
  driver.find_element(
    By.CSS_SELECTOR,
    "#horseName button[type='submit']"
  ).click()

  sleep()