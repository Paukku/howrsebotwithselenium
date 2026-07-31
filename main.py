from login import log_in
import json
from actions.care.care import take_care_horses

with open('config.json') as f:
  config = json.load(f)

driver = log_in()
account = config["accounts"][0]

for account in config["accounts"]:
  print(account["name"])

  for horse in account["horses"]:
    take_care_horses(
      driver,
      horse
    )