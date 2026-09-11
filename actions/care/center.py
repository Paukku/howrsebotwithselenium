from utils.randomTime import sleep, task_sleep
from selenium.webdriver.common.by import By
from utils.items import has_item

def center_automated(driver):
  if(has_item(driver, "hypnosin peite")):
     print("Älä laita keskukseen")
  else:
    try:
      change_to_own_stable(driver)
      task_sleep()
    except:
      pass

def center_not_automated(driver):
  if(has_item(driver, "hypnosin peite")):
    print("Älä laita keskukseen")
  else:
    try:
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div/div/div/div/div/div/div[@id='cheval-inscription']/a").click()
      task_sleep()
      task_sleep()
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/ul/li[@id='tab-box-reserve']/div/a").click()
      task_sleep()
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='boxContent']/table/tbody/tr[3]/td[10]/button").click()
      task_sleep()
    except:
      pass

def change_to_own_stable(driver):
  registration_buttons = driver.find_elements(
    By.CSS_SELECTOR,
    "a[href*='centreInscription']"
  )

  if not registration_buttons:
    print("Hevonen on jo omassa tallissa. Talliin laitto ohitetaan.")
    return

  print("Laitetaan hevonen omaan talliin.")

  registration_buttons[0].click()
  sleep()

  driver.find_element(
    By.CSS_SELECTOR,
    "#tab-box-reserve a"
  ).click()

  sleep()

  row = driver.find_element(
    By.XPATH,
    "//tr[.//a[contains(@class, 'usergroup_2') and normalize-space()='wory']]"
  )

  row.find_element(
    By.XPATH,
    ".//button[normalize-space()='Vapaana']"
  ).click()

  sleep()

def change_to_mountain_stable(driver):
  cancel_current_stable(driver)
  search_right_stable(driver, "*bluppivuori klassinen")

def select_right_stable(driver):
  forest_skills = forest_skills_left(driver)
  if forest_skills:
    search_right_stable(driver, "varsat metsä 30pv")
  else:
    search_right_stable(driver, "varsat vuoret 30pv")

# Help functions for stable management
def cancel_current_stable(driver):
  # 1. Peruuta nykyinen majoitus 
  driver.find_element( By.XPATH, "//button[.//span[normalize-space()='Peru majoitus']]" ).click() 
  # 2. Chromen oma vahvistusikkuna 
  alert = driver.switch_to.alert 
  alert.accept() 
  sleep()

def is_in_stable(driver):
  return not bool(driver.find_elements(
    By.CSS_SELECTOR,
    "a[href*='centreInscription']"
  ))

def open_registration(driver):
  driver.find_element(
    By.CSS_SELECTOR,
    "a[href*='centreInscription']"
  ).click()
  sleep()

def open_vip_search(driver):
  driver.find_element(By.CSS_SELECTOR, "div.select-vip").click()
  sleep()

def select_stable(driver, search_name):
  driver.find_element(
      By.XPATH,
      f"//span[contains(@class,'vip-search-label') and normalize-space()='{search_name}']"
  ).click()
  sleep()

def register_first_stable(driver):
    row = driver.find_element(
        By.XPATH,
        "//table[@id='table-0']/tbody/tr[1]"
    )

    cells = row.find_elements(By.TAG_NAME, "td")

    button = cells[8].find_element(By.TAG_NAME, "button")   # 30 pv sarake

    button.click()
    sleep()

def search_right_stable(driver, search_name):

  if is_in_stable(driver):
    return

  open_registration(driver)
  open_vip_search(driver)
  select_stable(driver, search_name)
  register_first_stable(driver)

def forest_skills_left(driver):
  forest_walk = driver.find_element(By.ID, "boutonBalade-foret")

  tooltip = forest_walk.get_attribute("data-tooltip")

  if "gains" in tooltip:
    print("Metsälenkkejä on vielä jäljellä")
    return True
  else:
    print("Metsälenkit on jo tehty")
    return False