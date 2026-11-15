import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.randomTime import sleep

BASE_URL = "https://www.howrse.fi"


def get_credentials():
  load_dotenv()
  username = os.getenv("howrse_username")
  password = os.getenv("howrse_password")
  if not username or not password:
    raise RuntimeError(
      "Missing credentials: set howrse_username and howrse_password in .env"
    )
  return username, password


def reject_cookies(driver):
  # The banner is not always shown, so a missing banner is not an error
  try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))
    ).click()
  except TimeoutException:
    pass


def log_in():
  username, password = get_credentials()

  driver = webdriver.Chrome()
  try:
    driver.get(BASE_URL)
    driver.maximize_window()
    sleep()
    reject_cookies(driver)
    sleep()
    driver.find_element(By.ID, "header-login-label").click()
    sleep()
    driver.find_element(By.ID, "login").send_keys(username)
    sleep()
    driver.find_element(By.ID, "password").send_keys(password)
    sleep()
    driver.find_element(By.ID, "authentificationSubmit").click()
  except Exception:
    driver.quit()  # do not leave a browser window open if login fails
    raise

  return driver