import json
import os
import random
import time
import pyautogui as pag
pag.FAILSAFE = True

def get_config():
    filename = 'config.json'
    if not os.path.isfile(filename):
        return 'config.json not found, download it from the repo.'
    else:
        with open(filename, 'r') as fp:
            config = json.load(fp)
        return config

config = get_config()

def Press(key, amount):
    count = 0
    while count < amount:
        pag.press(key)
        time.sleep(0.1)
        count += 1

def CLICK_INTERVAL():
    return random.uniform(config["Click Delay"][0], config["Click Delay"][1])

def random_break():
    random_time = random.randrange(config["Random Breaks wait"][0], config["Random Breaks wait"][1])
    print(f'Random break, waiting {round(random_time, 0)} seconds.')
    time.sleep(random_time)