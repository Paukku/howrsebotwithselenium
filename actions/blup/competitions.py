from selenium.webdriver.common.by import By
from utils.randomTime import sleep

def jumping_competition(driver, amount):
  for i in range(amount):
    print(f"Estekisa {i + 1}/{amount}")

    driver.find_element(
      By.CSS_SELECTOR,
      "a.competition-saut"
    ).click()
    sleep()