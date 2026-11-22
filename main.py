import argparse
import json
import sys

from actions.blup.blup import run_blup
from actions.training.train_horses import run_training
from actions.care.care import take_care_horses
from actions.training.train_horses import run_training
from login import log_in
from utils.random_time import sleep


def load_config(path):
  try:
    with open(path, encoding="utf-8") as f:
      return json.load(f)
  except FileNotFoundError:
    raise SystemExit(
      f"Config file not found: {path}. "
      "Copy config.example.json to config.json first."
    )
  except json.JSONDecodeError as e:
    raise SystemExit(f"Invalid JSON in {path}: {e}")


def run_blup_task(driver, config):
  blup = config["blup"]
  run_blup(driver, blup["amount"], blup["horse_id"], blup.get("feeding"))


def run_care_task(driver, config):
  for account in config["accounts"]:
    print(account["name"])
    feeding = account.get("feeding")
    for horse in account["horses"]:
      take_care_horses(
        driver,
        feeding,
        horse,
        skip_feeding=horse.get("skip_feeding", False),
      )

def run_quick_care_task(driver, config):
  quick_care = config["quick_care"]
  take_care_horses(
      driver,
      quick_care.get("feeding"),
      {"id": quick_care["horse_id"], "amount": quick_care["amount"]},
      skip_feeding=quick_care.get("skip_feeding", False),
    )
        


def run_training_task(driver, config):
  training = config["training"]
  run_training(
    driver, training["amount"], training["horse_id"], training.get("feeding"), training.get("owner")
  )

def run_testing_task(driver, config):
  testing = config["testing"]
  driver.get("https://www.howrse.fi/elevage/chevaux/")
  sleep()
  
  driver.get(f"https://www.howrse.fi/elevage/chevaux/cheval?id={testing['horse_id']}")
  run_training(driver)


# Order matters: tasks always run in this order
TASKS = {
  "care": run_care_task,
  "blup": run_blup_task,
  "training": run_training_task,
  "testing": run_testing_task,
  "quick_care": run_quick_care_task,
}


def is_enabled(config, task):
  if task == "care":
    return bool(config.get("accounts"))
  return config.get(task, {}).get("enabled", False)


def parse_args(argv=None):
  parser = argparse.ArgumentParser(description="Howrse browser automation bot.")
  parser.add_argument(
    "-t",
    "--task",
    nargs="+",
    choices=list(TASKS),
    help="tasks to run (default: every task enabled in the config)",
  )
  parser.add_argument(
    "-c", "--config", default="config.json", help="path to the config file"
  )
  return parser.parse_args(argv)


def main(argv=None):
  args = parse_args(argv)
  config = load_config(args.config)

  if args.task:
    tasks = [t for t in TASKS if t in args.task]
  else:
    tasks = [t for t in TASKS if is_enabled(config, t)]

  if not tasks:
    print("No tasks to run. Enable tasks in the config or use --task.")
    return 0

  driver = log_in()
  try:
    for name in tasks:
      TASKS[name](driver, config)
  finally:
    driver.quit()
  return 0


if __name__ == "__main__":
  sys.exit(main())