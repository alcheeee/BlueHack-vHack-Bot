import time
import pyautogui as pag
from Utils import config, CLICK_INTERVAL
from BlueHackWindow import BlueHack, BlueHackImages, GetElement, HOME, MouseCords
pag.FAILSAFE = True

def Farm_Botnet():
    #Target icon, low conficence threshold so may get random selection
    target = BlueHackImages['botnet_target'][0]
    target_chapter = str(config['Botnet Chapter'])
    botnet_x, botnet_y = MouseCords['Botnet Icon'][0], MouseCords['Botnet Icon'][1]

    # Chapter locations and whether scrolling is needed to access them
    Chapters = {
        '1': [False, 944, 478],
        '2': [False, 943, 637],
        '3': [False, 943, 799],
        '4': [True, 943, 561],
        '5': [True, 943, 782]
    }
    chapter_info = Chapters[target_chapter] # Get chapter info

    pag.click(botnet_x, botnet_y)
    time.sleep(.6)

    # Click the botnet targets icon
    targetapp_x, targetapp_y = MouseCords['Target Icon'][0], MouseCords['Target Icon'][1]

    pag.click(targetapp_x, targetapp_y)
    time.sleep(0.5)

    # If the chapter requires scrolling to be accessed, perform the scroll
    if chapter_info[0]:
        scroll_x, scroll_y = Chapters['2'][1], Chapters['2'][2]
        pag.moveTo(scroll_x, scroll_y)
        pag.scroll(-500,x=scroll_x, y=scroll_y)
        time.sleep(2)

    # Click the specific chapter
    chapt_x, chapt_y = chapter_info[1], chapter_info[2]
    time.sleep(CLICK_INTERVAL())
    pag.click(chapt_x, chapt_y)

    # Attempt to find and click on the target within the botnet chapter
    target_found, (target_x, target_y) = GetElement(target, 0.5)
    if target_found:
        time.sleep(CLICK_INTERVAL())
        pag.click(target_x, target_y)
        time.sleep(.5)

        # Locate the attack button
        attack_btn_found,(attack_x, attack_y) = GetElement(BlueHackImages['botnet_attack'][0], 0.7)
        time.sleep(.2)
        if not attack_btn_found:
            print('No more energy.') # If no attack button found, assume out of energy and return to home
            return HOME()

        while True: # Continuously attack targets until no more energy
            pag.click(attack_x, attack_y)
            time.sleep(config['TTK Botnet Target'] + CLICK_INTERVAL())
            back_x, back_y = MouseCords['Botnet Back'][0], MouseCords['Botnet Back'][1]

            time.sleep(CLICK_INTERVAL())
            pag.click(back_x, back_y)
            time.sleep(.4)

        #Home
        print('Completed Botnet Farm.')
        return HOME()
    else:
        print('Could not find target.')
        return HOME()