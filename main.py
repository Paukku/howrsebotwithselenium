from login import log_in
import json
from actions.care.care import take_care_horses
from actions.blup.blup import run_blup
with open('config.json') as f:
  config = json.load(f)

driver = log_in()

blup = config["blup"]
feeding = blup["feeding"]
horse_id = blup["horse_id"]
amount = blup["amount"]

run_blup(driver, amount, horse_id, feeding)
account = config["accounts"][0]

for account in config["accounts"]:
  print(account["name"])
  feeding = account["feeding"]

  for horse in account["horses"]:
    skip_feeding = horse.get("skip_feeding", False)
        
    take_care_horses(
      driver,
      feeding,
      horse,
      skip_feeding=skip_feeding
    )