import time
import random
import pyautogui as pag
from Utils import Press, CLICK_INTERVAL, random_break, config
from BlueHackWindow import BlueHack, BlueHackImages, GetElement, check_for_block, check_connection, MouseCords
pag.FAILSAFE = True

nc_block = BlueHackImages['nc_block']

def set_location():
    # Set the start location in the NC Mine
    Press('down', 3)
    Press('right', 1)
    Press('left', 7)


def NC_Mining(stop_mining):
    """
    :param stop_mining: Periodically checks if stop_mining is True.
    NC_Mining loop
    """
    ON_MINE_APP = False
    STOP_MINING = False
    while True:
        # Check the connection, just in case.
        if check_connection(0):
            break
        if STOP_MINING:
            break
        else:
            # Click on Mine App
            mine_x, mine_y = MouseCords['Mine Icon'][0], MouseCords['Mine Icon'][1]

            # Start the bot
            if not ON_MINE_APP:
                pag.click(mine_x, mine_y)

            ON_MINE_APP = True

            # Grid management for moving around the mine
            grid = 'LeftBot'
            locations = {
                'LeftBot': ['up', 6, 'LeftTop'],
                'LeftTop': ['right', 6, 'MidTop'],
                'MidTop': ['right', 5, 'RightTop'],
                'RightTop': ['down', 6, 'RightBot'],
                'RightBot': ['left', 5, 'MidBot'],
                'MidBot': ['left', 6, 'LeftBot']
            }

            back_btn_x, back_btn_y = MouseCords['Mining Back'][0], MouseCords['Mining Back'][1]
            zoom_x, zoom_y = MouseCords['Mining Zoom'][0], MouseCords['Mining Zoom'][1]

            #Zoom out for larger scan
            time.sleep(0.1)
            pag.mouseDown(x=zoom_x, y=zoom_y)
            time.sleep(1)
            pag.mouseUp()
            time.sleep(1)
            set_location()

            while not stop_mining.value:
                if check_connection(0): # Again to make sure we're still connected
                    break

                # Random breaks in mining
                if config['Random Breaks'] and random.randint(0,100) < config["Random Chance"]:
                    pag.click(back_btn_x, back_btn_y)
                    random_break()
                    break

                # Looks for a block
                found, (x, y) = check_for_block()
                if found:
                    pag.click(x, y) # Block found, click it
                    time.sleep(CLICK_INTERVAL() + config["Mine Speed"])

                else:
                    # Block not found, starts grid scan
                    count = 0
                    passes = config["Mine Passes until Cooldown"] * 6
                    while True:

                        # Does x amount of scans before cooldown if none
                        if count >= passes:
                            random_sleep = random.randrange(config['Cooldown Wait Time'][0],
                                                            config['Cooldown Wait Time'][1])
                            print("Full pass done, mine is empty.")
                            print(f'Waiting {round(random_sleep, 0)} seconds.')
                            time.sleep(random_sleep)
                            count = 0

                        time.sleep(.3)
                        found, (_,_) = check_for_block()
                        if found or stop_mining.value:
                            break
                        else:
                            # Scan grid and sets current location on the grid for later use
                            print('Looking for Block...')
                            Press(locations[grid][0], locations[grid][1])
                            grid = locations[grid][2]
                            count += 1

            # Go back to main menu
            pag.click(back_btn_x, back_btn_y)
            STOP_MINING = True