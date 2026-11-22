"""Decision logic for training a horse (target: actions/training/horse_decision.py).

Pure Python, no browser needed. The state is read from the page elsewhere;
this module only decides what to do with it. Each horse gets at most one
stable move and exactly one main action per run.
"""

from dataclasses import dataclass
from enum import Enum

MAX_TRAINING_AGE_MONTHS = 24 * 12 + 10  # 24y10m


def age_in_months(age):
  """'24y10m' -> 298 (foals count as 0)."""
  if age == "foal":
      return 0
  years, months = age.rstrip("m").split("y")
  return int(years) * 12 + int(months)


class Action(Enum):
  STOP = "stop"  # horse is old enough: end the whole run
  FOREST_WALKS = "forest_walks"
  MOUNTAIN_WALKS = "mountain_walks"
  TRAIN_SKILL = "train_skill"
  COMPETE = "compete"  # specialise and equip if needed, then compete or do the task


@dataclass
class HorseState:
  age_months: int
  in_center: bool
  stable: str | None  # "forest", "mountain", another stable's name, or None
  forest_walks_left: bool
  mountain_walks_left: bool
  incomplete_skills: list[str]  # empty when every skill is complete
  can_compete_for_skills: bool  # specialised, equipped and competitions give skill points


@dataclass
class Plan:
  action: Action
  move_to: str | None = None  # "forest", "mountain", "pizkunen" or "gear"
  skill: str | None = None  # only for TRAIN_SKILL


# (stable the walk belongs to, HorseState field, action); forest has priority
WALKS = (
  ("forest", "forest_walks_left", Action.FOREST_WALKS),
  ("mountain", "mountain_walks_left", Action.MOUNTAIN_WALKS),
)


def choose_stable(state):
  """Stable to move the horse to when it is not in a center, else None."""
  if state.in_center:
    return None
  if state.forest_walks_left:
    return "forest"
  if state.mountain_walks_left:
    return "mountain"
  if not state.incomplete_skills:
    return "pizkunen"
  return "gear"  # a stable that offers gear, needed for competitions


def plan_horse(state):
  if state.age_months >= MAX_TRAINING_AGE_MONTHS:
    return Plan(Action.STOP)

  move_to = choose_stable(state)
  stable = move_to or state.stable

  # A walk whose own stable the horse is in
  for walk_stable, left_field, action in WALKS:
    if getattr(state, left_field) and stable == walk_stable:
      return Plan(action, move_to)

  # A walk is left, but the horse is in the wrong stable. Only when every
  # skill is complete: compete if that gives skill points, otherwise walk.
  walk_left = next((a for _, f, a in WALKS if getattr(state, f)), None)
  if walk_left and not state.incomplete_skills:
    if state.can_compete_for_skills:
      return Plan(Action.COMPETE, move_to)
    return Plan(walk_left, move_to)

  if state.incomplete_skills:
    return Plan(Action.TRAIN_SKILL, move_to, skill=state.incomplete_skills[0])

  return Plan(Action.COMPETE, move_to)