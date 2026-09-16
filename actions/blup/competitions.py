from selenium.webdriver.common.by import By
from utils.randomTime import sleep
from actions.care.care_actions import element_exists
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

def close_error_popup(driver):
  try:
    popup = WebDriverWait(driver, 2).until(
      EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "td.errorContent")
      )
    )

    print("Howrse-virheilmoitus löytyi.")

    close_button = popup.find_element(
      By.XPATH,
      "./ancestor::*[contains(@class, 'popupview')][1]//button[contains(@class, 'popupview__close')]"
    )

    driver.execute_script(
      "arguments[0].click();",
      close_button
    )

    WebDriverWait(driver, 2).until(
      EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, "td.errorContent")
      )
    )

    print("Howrse-virheilmoitus suljettu.")
    return True

  except TimeoutException:
      return False
    
def competition(driver, amount, selectors, name, retry=True):
  for i in range(amount):
    print(f"{name} {i + 1}/{amount}")

    while True:
      clicked = False

      for selector in selectors:
        print(f"Testataan selector: {selector}")

        try:
          button = driver.find_element(
            By.CSS_SELECTOR,
            selector
          )

          try:
            button.click()

          except ElementClickInterceptedException:
            print("Klikkaus estyi overlayn vuoksi")

            close_error_popup(driver)
            sleep()

            button = driver.find_element(
              By.CSS_SELECTOR,
              selector
            )

            button.click()

          clicked = True
          break

        except NoSuchElementException:
            print(f"Ei löytynyt: {selector}")

        except StaleElementReferenceException:
            print("Elementti vanheni → yritetään uudelleen")

      # Kaikki selectorit käytiin läpi
      if clicked:
          sleep()
          break

      # Yhtäkään nappia ei löytynyt
      if retry:
          print(f"{name}-kilpailua ei vielä löytynyt → odotetaan")
          sleep()
      else:
          print(f"{name}-kilpailua ei löytynyt → skipataan")
          break
# Classic
def jumping_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-saut"],
    "Estekisa"
  )

def cross_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-cross"],
    "Maastokisa"
  )

def dressage_competition(driver, amount):
  competition(
    driver,
    amount,
    [
      #"a.competition-dressage-rainbow",
      "a.competition-dressage"
    ],
    "Koulukisa"
  )

def trot_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-trot"],
    "Ravikisa"
  )

def galop_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-galop"],
    "Laukkakisa"
  )

# Western
# Classic
def barrel_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-barrel"],
    "Tynnyrikisa"
  )

def cutting_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-cutting"],
    "Cutting"
  )

def trail_competition(driver, amount):
  competition(
    driver,
    amount,
    [
    #  "a.competition-trail-class-rainbow",
      "a.competition-trail-class"
    ],
    "Trail"
  )

def reining_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-reining"],
    "Reining"
  )

def western_pleasure_competition(driver, amount):
  competition(
    driver,
    amount,
    ["a.competition-western-pleasure"],
    "Western pleasure"
  )
