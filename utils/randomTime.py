import time
import random

def short_sleep():
  time.sleep(random.uniform(0.23, 0.27)) #vaihda 23 ja 33

def sleep():
  time.sleep(random.uniform(1.23,  1.35))

def task_sleep():
  time.sleep(random.uniform(1.51, 2.27))

def random_wait():
  time.sleep(random.uniform(5, 50))
