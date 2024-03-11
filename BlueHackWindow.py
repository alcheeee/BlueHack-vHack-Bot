import time
import pyautogui as pag
import pygetwindow as pgw
from Utils import config

#PyAutoGUI for certain handling
BlueHackImages = {
    'disconnected': ['images/connection_lost.png', 'Connection Lost'],
    'nc_block': ['images/nc_block.png', 'NC Block'],
    'botnet_attack': ['images/botnet_attack.png', 'Botnet Attack'],
    'botnet_target': ['images/target_icon.png', 'Botnet Target'],
    'wheel_confirm': ['images/wheel_confirm.png', 'Center Wheel'],
    'no_spins': ['images/no_spins.png', 'No Spins']
}

#X,Y positions for 1920x1080 Resolution, Fullscreen Bluestacks
MouseCords = {
    'Home Btn': [943, 1053],
    'Reconnect': [944, 659],
    'Mine Icon': [874, 812],
    'Mining Back': [704, 1038],
    'Mining Zoom': [1185, 964],
    'Wheel Icon': [802, 982],
    'Slot Icon': [894, 982],
    'Slot Spin': [946, 893],
    'Botnet Icon': [1147, 405],
    'Target Icon': [1169, 971],
    'Botnet Back': [1169, 477]
}

def get_bluestacks_window():
    while True:
        try:
            # Attempt to find the BlueStacks window by title
            BlueHack = pgw.getWindowsWithTitle('BlueStacks App Player')[0]
            if BlueHack:

                # Check if the window is completely visible on the screen
                box = BlueHack.box
                ON_SCREEN = all([box[0] >= 0, box[1] >= 0, box[2] >= 0, box[3] >= 0])
                if ON_SCREEN:
                    return BlueHack
                else:
                    print('Move Window on main screen.')
                    time.sleep(3)
        except:
            print("Can't get BlueStacks... Trying again in 3 seconds")
            time.sleep(3)
            continue

BlueHack = get_bluestacks_window()

def HOME():
    pag.click(MouseCords['Home Btn'][0], MouseCords['Home Btn'][1])

def GetElement(element, CONFIDENCE):
    # Locate a UI element on the screen within the vHack window
    try:
        vHack_box = BlueHack.box
        region = (vHack_box[0], vHack_box[1], vHack_box[2], vHack_box[3])
        find_element = pag.locateOnScreen(element, region=region, confidence=CONFIDENCE)
        if find_element:
            center_x, center_y = pag.center(find_element)
            return True, (center_x, center_y)
    except:
        return False, (None, None)

def check_for_block():
    # Checked for NC Mining block
    found, (x, y) = GetElement(BlueHackImages['nc_block'][0], 0.85)
    if found:
        return True, (x, y)
    else:
        return False, (None, None)



def check_connection(attempts):
    # Check for and attempt to recover if lost connection
    lost_con, (_, _) = GetElement(BlueHackImages['disconnected'][0], 0.8)
    if lost_con and attempts < 10:
        print('Connection Lost')
        print('Attempting Reconnect...')
        pag.click(MouseCords['Reconnect'][0], MouseCords['Reconnect'][1])
        time.sleep(3)
        check_connection(attempts+1)
    elif lost_con and attempts >= 10:
        return True
    else:
        return False