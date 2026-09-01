from selenium.webdriver.common.by import By
from utils.randomTime import sleep
from actions.care.care_actions import element_exists

def competition(driver, amount, selectors, name):
  for i in range(amount):
    print(f"{name} {i + 1}/{amount}")

    for selector in selectors:
      if element_exists(driver, By.CSS_SELECTOR, selector):
        driver.find_element(
          By.CSS_SELECTOR,
          selector
        ).click()
        break
    else:
      raise Exception(f"{name}-kilpailua ei löytynyt")

    sleep()

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
      "a.competition-trail-class-rainbow",
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
