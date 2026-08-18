from utils.randomTime import sleep
from selenium.webdriver.common.by import By

def feed_horse(driver, full_oats=False):
  hay_current, hay_target = get_feed_values(driver, "fourrage")
  oat_current, oat_target = get_feed_values(driver, "avoine")
  changed = False

  if hay_current < hay_target:
    select_slider_value(driver, 2, "haySlider", hay_target)
    changed = True
  sleep()

  print(full_oats)

  if full_oats:
    print(full_oats)
    oat_amount = 19
  else:
    oat_amount = oat_target + 1

  if oat_current < oat_target or full_oats:
    print(oat_amount)
    select_slider_value(driver, 4, "oatsSlider", oat_amount)
    changed = True
  sleep()
  
  if changed:
    driver.find_element(By.ID, "feed-button").click()

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


def select_slider_value(driver, tr, slider_id, amount):
  slider_index = amount + 1
  driver.find_element(
    By.XPATH,
    f"/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[{tr}]/td/div[@id='{slider_id}']/ol/li[{slider_index}]"
  ).click()

def automated_feed(driver):
  driver.find_element(By.ID, "feed-button").click()
  sleep()