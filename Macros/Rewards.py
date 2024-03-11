import time
import random
import pyautogui as pag
from BlueHackWindow import BlueHackImages, GetElement, HOME, check_connection, MouseCords
pag.FAILSAFE = True

def Check_Rewards():
    WheelSpins()
    time.sleep(random.uniform(1.5, 3))
    SlotSpins()

def click_wait(x, y, clicks):
    count = 0
    while count < clicks:
        pag.click(x, y)
        time.sleep(random.uniform(0.03, .08))
        count += 1

def WheelSpins():
    # Click on the wheel icon
    pag.click(MouseCords['Wheel Icon'][0], MouseCords['Wheel Icon'][1])
    time.sleep(.3)

    FIRST_SPIN = True # Track if it's the first spin
    while True:
        if check_connection(0):
            break

        # Check for the confirmation button to spin the wheel
        wheel_confirm, (confirm_x, confirm_y) = GetElement(BlueHackImages['wheel_confirm'][0], 0.8)
        if FIRST_SPIN:
            click_wait(confirm_x, confirm_y, 5)
            time.sleep(1.2)
            FIRST_SPIN = False

        elif not wheel_confirm:
            click_wait(confirm_x, confirm_y, 5)
            time.sleep(random.uniform(1.8, 2.2))
        else:
            HOME() # Return to home screen if no confirmation
            break
    return HOME()

def SlotSpins():
    pag.click(MouseCords['Slot Icon'][0], MouseCords['Slot Icon'][1])
    time.sleep(.3)

    no_spins, (_, _) = GetElement(BlueHackImages['no_spins'][0], 0.8)
    if no_spins:
        return HOME()

    while True:
        no_spins, (_, _) = GetElement(BlueHackImages['no_spins'][0], 0.8)
        if no_spins:
            HOME() # Return to home screen if no more spins
            break
        else:
            click_wait(MouseCords['Slot Icon'][0], MouseCords['Slot Icon'][1], 5) # Perform spins if available


