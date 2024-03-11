from multiprocessing import Process, Value
from threading import Timer
import ctypes
import os
import time
from Macros.Botnet import Farm_Botnet
from Macros.Mining import NC_Mining
from Macros.Rewards import Check_Rewards
from Utils import config

FARM_TIME = config['Farm Time'] * 60
CLOSE_SCRIPT = False

def GeneralFarm(stop_mining):
    """
    :param stop_mining: Stops on timer pulled from config 'Farm Time'
    Main loop of the 'General Farm' until stop_mining
    """
    while not stop_mining.value:
        NC_Mining(stop_mining)
        if config['Check Rewards after farm']:
            time.sleep(3)
            Check_Rewards()
        if config['Check Botnet after farm']:
            time.sleep(3)
            Farm_Botnet()


def main():
    #This is the timer, farming operations will stop after this
    stop_mining = Value(ctypes.c_bool, False)
    farm_time_timer = Timer(FARM_TIME, quit_script, [stop_mining])
    farm_time_timer.start()
    """
    Main menu, Farm Timer starts as soon as the script is ran.
    General farm is NC Mine with rewards and botnet farms (if enabled in config).
    """
    while True:
        if CLOSE_SCRIPT:
            os.system('cls||clear')
            break
        print('BlueHack | Education Purposes only!')
        print('Type the number of the option you want.')
        print('[1] General Farm\n[2] Botnet Farm\n[3] Prize Farm\n[5] Quit')
        user_input = input('What would you like to do? ')

        if user_input == '1':
            print('Started Farming')
            farm_process = Process(target=GeneralFarm, args=(stop_mining,))
            farm_process.start()
            farm_process.join()

        elif user_input == '2':
            print(f'Farming Botnet')
            Farm_Botnet()

        elif user_input == '3':
            print(f'Farming Prizes')
            Check_Rewards()

        elif user_input == '4':
            quit_script(stop_mining, farm_process=None)
        else:
            os.system('cls||clear')
            print('Not a valid option.')

def quit_script(stop_mining, farm_process=None):
    """
    Exit function for the entire script, called once 'Farm Time' is done.
    """
    global CLOSE_SCRIPT
    os.system('cls||clear')
    print('Farm finished, closing...')
    stop_mining.value = True
    if farm_process is not None:
        farm_process.terminate()
    time.sleep(3)
    CLOSE_SCRIPT = True

if __name__ == '__main__':
    main()