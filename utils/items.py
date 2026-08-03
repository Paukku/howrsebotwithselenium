from selenium.webdriver.common.by import By

def has_item(driver, item_name):
  return len(driver.find_elements(
    By.CSS_SELECTOR,
    f'img[alt="{item_name}"]'
  )) > 0