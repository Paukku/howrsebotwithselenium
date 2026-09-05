from utils.randomTime import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


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

def click_link_by_text(driver, text):
  try:
    link = driver.find_element(
      By.XPATH,
      f"//a[contains(normalize-space(), '{text}')]"
    )

    driver.execute_script("arguments[0].click();", link)
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
