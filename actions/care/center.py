from utils.randomTime import sleep, task_sleep
from selenium.webdriver.common.by import By
from utils.items import has_item

def center_automated(driver):
  if(has_item(driver, "hypnosin peite")):
     print("Älä laita keskukseen")
  else:
    try:
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[5]/div/div/div/div/div/div/div[@id='cheval-inscription']/a").click()
      task_sleep()
      task_sleep()
      driver.find_element(By.ID, "tab-box-reserve").click()
      task_sleep()
      task_sleep()
      driver.find_element(By.XPATH, "html/body/div[@id='container']/main/section/section/div[@id='boxContent']/table/tbody/tr[7]/td[9]/button").click()
      task_sleep()
      driver.find_element(By.ID, "boutonCoucher").click()
      sleep()
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

  # 1. Peruuta nykyinen majoitus
  driver.find_element(
    By.XPATH,
    "//button[.//span[normalize-space()='Peru majoitus']]"
  ).click()

  # 2. Chromen oma vahvistusikkuna
  alert = driver.switch_to.alert
  alert.accept()

  sleep()

  # 3. Mene tallin rekisteröintiin
  driver.find_element(
    By.CSS_SELECTOR,
    "a[href*='centreInscription']"
  ).click()

  sleep()
  driver.find_element(
    By.XPATH,
    "//span[contains(@class, 'vip-search-label') and normalize-space()='*bluppivuori klassinen']"
  ).click()
  sleep()

  row = driver.find_element(
      By.XPATH,
      "//table[@id='table-0']/tbody/tr[1]"
  )

  cells = row.find_elements(By.TAG_NAME, "td")

  # Tulosta debuggausta varten
  for i, cell in enumerate(cells):
      print(i, cell.text)

  # 3 päivän sarake
  three_day_cell = cells[6]

  button = three_day_cell.find_element(
    By.TAG_NAME,
    "button"
  )

  if "disabled" in button.get_attribute("class"):
    raise Exception("Ensimmäisessä tallissa ei ole vapaata 3 päivän paikkaa.")

  button.click()

  sleep()

  print("Ensimmäinen vuoritalli valittu 3 päiväksi.")