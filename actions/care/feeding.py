from utils.randomTime import short_sleep, sleep
from selenium.webdriver.common.by import By

def feed_horse(driver, full_oats=False):
  hay_current, hay_target = get_feed_values(driver, "fourrage")
  oat_current, oat_target = get_feed_values(driver, "avoine")
  changed = False

  if hay_current < hay_target:
    select_slider_value(driver, "haySlider", hay_target)
    changed = True
  sleep()

  if full_oats:
    oat_amount = 15
  else:
    oat_amount = oat_target + 1

  if oat_current < oat_target or full_oats:
    print(oat_amount)
    select_slider_value(driver, "oatsSlider", oat_amount)
    changed = True
  sleep()
  
  if changed:
    driver.find_element(By.ID, "feed-button").click()
    sleep()

def get_feed_values(driver, section):
  current = int(driver.find_element(
      By.CSS_SELECTOR,
      f".section-{section}-quantity"
  ).text.split("/")[0].strip())

  target = int(driver.find_element(
      By.CSS_SELECTOR,
      f".section-{section}-target"
  ).text)

  return current, target


def select_slider_value(driver, slider_id, amount):
  slider_index = amount + 1
  slider = driver.find_element(
    By.ID,
    slider_id
  )

  slider.find_element(
    By.CSS_SELECTOR,
    f"li:nth-child({slider_index})"
  ).click()

def automated_feed(driver):
  driver.find_element(By.ID, "feed-button").click()
  short_sleep()