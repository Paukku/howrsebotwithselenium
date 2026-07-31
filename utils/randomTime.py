import time
import random

def short_sleep():
  time.sleep(random.uniform(0.6, 1.09))

def sleep():
  time.sleep(random.uniform(1.43,  1.55))


def task_sleep():
  time.sleep(random.uniform(1.51, 2.27))


def long_sleep():
  time.sleep(random.uniform(5.75, 12.103))

def very_long_sleep():
  time.sleep(random.uniform(90.75, 454.103))

def random_wait():
  time.sleep(random.uniform(5, 50))
