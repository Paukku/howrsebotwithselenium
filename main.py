from login import log_in
import json
from actions.care.care import take_care_horses
from actions.blup.blup import run_blup
from actions.training.training import run_training
with open('config.json') as f:
  config = json.load(f)

driver = log_in()



training = config["training"]
feeding = training["feeding"]
horse_id = training["horse_id"]
amount = training["amount"]
run_training(driver, amount, horse_id, feeding)