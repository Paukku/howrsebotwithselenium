"""Functions that read a horse's state from its page (target: actions/training/state_readers.py).

Call them after the horse page has loaded (for example after get_horse_age).
Already existing readers that can be reused as they are:
  - in a center stable:  actions.care.center.is_in_stable
  - specialisation:      actions.care.care_actions.get_specialization
"""
import re

from selenium.webdriver.common.by import By

from actions.care.care_actions import EQUIP_LINK, get_specialization
from actions.training.training import SKILLS


def get_incomplete_skills(driver):
  """Return the skills that are not complete yet, in training order.

  A complete skill's label cell has the CSS class "complete".
  """
  incomplete = []
  for skill, word in SKILLS.items():
    classes = driver.find_element(By.ID, f"{word}Label").get_attribute("class") or ""
    if "complete" not in classes.split():
      incomplete.append(skill)
  return incomplete


def is_specialised(driver):
  return get_specialization(driver) is not None


def is_equipped(driver):
  """The horse counts as equipped when the 'Varusta hevonen' link is not shown."""
  return not driver.find_elements(*EQUIP_LINK)

WALK_BUTTONS = {
  "forest": "boutonBalade-foret",
  "mountain": "boutonBalade-montagne",
}

# Text that appears in the walk button's tooltip only while the walk still
# gives skill points. Candidates so far: "gains" or "<b>+</b>". Confirm with
# the tooltip of a horse that has walks left and one that has none.
WALK_LEFT_MARKER = "gains"


def walks_left(driver, walk):
  """True if the walk ("forest" or "mountain") still gives skill points."""
  buttons = driver.find_elements(By.ID, WALK_BUTTONS[walk])
  if not buttons:
    return False
  tooltip = buttons[0].get_attribute("data-tooltip") or ""
  return WALK_LEFT_MARKER in tooltip

# The center box on the horse page shows the stable the horse is in. The link
# with the stable's name has a class that tells the location.
STABLE_LOCATIONS = {
    "centerLocalisationForet": "forest",
    "centerLocalisationMontagne": "mountain",
}


def get_stable(driver):
  """Return "forest", "mountain", "other", or None if the horse is not in a center.

  HorseState.in_center is simply get_stable(driver) is not None.
  """
  links = driver.find_elements(By.CSS_SELECTOR, "#center-tab-main a.centerLocalisation")
  if not links:
    return None
  classes = (links[0].get_attribute("class") or "").split()
  for css_class, stable in STABLE_LOCATIONS.items():
    if css_class in classes:
      return stable
  return "other"


# The "Edut" row of the center box lists the free gear as images, for example
# ".../selle-classique-3x_v123.png". The word after "selle-" tells the style.
# Only classic is confirmed; the western word is still unknown.
GEAR_STYLES = {"classique": "classic"}


def get_stable_gear_style(driver):
  """Return the gear style the stable offers ("classic"), or None if unknown or none."""
  images = driver.find_elements(By.CSS_SELECTOR, "#center-tab-main img[src*='selle-']")
  for image in images:
    match = re.search(r"selle-([a-z]+)-", image.get_attribute("src") or "")
    if match:
      return GEAR_STYLES.get(match.group(1))
  return None