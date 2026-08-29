from selenium.webdriver.common.by import By
from utils.randomTime import sleep
from actions.care.care_actions import element_exists

def jumping_competition(driver, amount):
  for i in range(amount):
    print(f"Estekisa {i + 1}/{amount}")

    driver.find_element(
      By.CSS_SELECTOR,
      "a.competition-saut"
    ).click()
    sleep()

def dressage_competition(driver, amount):
  for i in range(amount):
    print(f"koulukisa {i + 1}/{amount}")

    if element_exists(
      driver,
      By.CSS_SELECTOR,
      "a.competition-dressage-rainbow"
    ):
      driver.find_element(
        By.CSS_SELECTOR,
        "a.competition-dressage-rainbow"
      ).click()
    else:
      driver.find_element(
        By.CSS_SELECTOR,
        "a.competition-dressage"
      ).click()

    sleep()