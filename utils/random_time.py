import random
import time


def tiny_sleep():
  """Tiny pause (0.03-0.08 s) before a click."""
  time.sleep(random.uniform(0.13, 0.19))
def short_sleep():
  time.sleep(random.uniform(0.23, 0.27)) #vaihda 23 ja 33

def sleep():
  time.sleep(random.uniform(1.23,  1.35))

def task_sleep():
  time.sleep(random.uniform(1.51, 2.27))

def random_wait():
  time.sleep(random.uniform(5, 50))
