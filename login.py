from selenium import webdriver
from utils.randomTime import sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('howrse_username')
password = os.getenv('howrse_password')

def log_in():
  driver = webdriver.Chrome()
  driver.get("https://www.howrse.fi")
  driver.maximize_window()
  sleep()
  driver.find_element(By.ID, "onetrust-reject-all-handler").click()
  sleep()
  driver.find_element(By.ID, "header-login-label").click()
  sleep()
  username_input = driver.find_element(By.ID, "login")
  username_input.send_keys(username)
  sleep()
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys(password)
  sleep()

  driver.find_element(By.ID, "authentificationSubmit").click()

  return driver


if __name__ == "__main__":
  log_in()
  exit()