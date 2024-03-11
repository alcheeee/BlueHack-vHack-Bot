# BlueHack

BlueHack is an automation script designed for the game 'vHack Revolutions - Hacker Sim'. The script includes automation for netcoin mining, botnet farming, and checking for rewards.

> [!WARNING]
> **Educational Purposes Only:** This project is designed solely for educational purposes to demonstrate concepts in programming, automation, and GUI interaction using PyAutoGUI. It is not intended for use in cheating or automating gameplay. The use of this project in a live game environment may go against the terms of service. Such practices are strongly discouraged and may result in a game ban.

## Features 🌟

- **NC Mining:** Automated mining for netcoins within the game.
- **Botnet Farming:** Automated farming in the botnet section of the game, based on the configured chapter.
  - ⚠️ *Note: Buggy, often won't find a target to 'attack'.*
- **Reward Checking:** Automated checking and collection of available wheel spins and slot spins.
- **Configurable Farm Time:** Set a duration for how long the script should farm.
- **Optional Reward and Botnet Check:** Configurable options to run reward and botnet checks after NC mining or on optional random breaks.

## Configuration 🛠️

The `config.json` allows the ability to customize some of the options for the farming script. Configuration options and their purpose:

### General Settings

- **Farm Time:** Duration (in minutes) for which farming operations are run before stopping automatically.
  - 🔄 *If both 'Check Rewards/Botnet' are enabled, it will collect those before stopping.*
- **Check Rewards after farm:** Whether to check for rewards after completing NC mining or on breaks.
- **Check Botnet after farm:** Whether to perform botnet farming after completing NC mining or on breaks.
- **Random Breaks:** Whether to take random breaks during farming.
- **Random Chance:** The probability of taking a random break.
- **Random Breaks wait:** Range of time (in seconds) that a random break will last.

### Mine Settings

- **Mine Speed:** Mine speed (16/12/6 for based upgrades in the mine).
- **Click Delay:** Range of time (in seconds) to wait between clicks.
  - 🕒 *Float values or integers.*
- **Mine Passes until Cooldown:** The number of passes to do in mine before a cooldown period starts.
- **Cooldown Wait Time:** Range of time (in seconds) to wait in the cooldown period before resuming mining.

### Botnet Settings

- **Botnet Chapter:** The chapter of the botnet to farm in.
- **TTK Botnet Target:** The time to kill (in seconds) for a botnet target.
  - ⚠️ *Note: Buggy, since it might not click the right target, put higher than it actually takes.*
  - 🕒 *Float values or integers.*

## Requirements

- 1920x1080 Resolution monitor (or change X,Y values in `BlueHackWindow.py MouseCords`)
- BlueStacks 5 (maybe other Emulators work, I haven't tried.)
- Python 3.12
- PyAutoGUI
- PyGetWindow (for managing the BlueStacks window)

## Usage 📖

To start the automation, run the `main.py` script. You have the following options:

1. **General Farm:** Runs mining with optional reward and botnet checks based on the configuration.
2. **Botnet Farm:** Starts botnet farming immediately.
3. **Prize Farm:** Checks and collects available rewards (wheel/slot spins).
4. **Quit:** Exits the script.

👉 Select an option by typing it's number.

## Installation

Ensure Python 3.6 or higher is installed. Install the required Python packages using pip:

Clone this repository, navigate to the BlueHack directory, and install the requirements in a python environment:

```
pip install -r requirements.txt
```

### BlueStacks Settings
```
Display:
- Portrait mode
- 1080x1920
- 320 DPI(High)
```
> [!IMPORTANT] 
> BlueStacks must be in Fullscreen with the above settings!

## Disclaimers

1. **Image Property Rights:** All images and assets utilized by this script are the property of their respective owners, namely the vHack Revolutions developers and/or KF-Media Solutions. This project claims no ownership over such materials and respects the intellectual property rights of the original creators.
   
2. **No Liability:** The creator(s) of this project claim no responsibility for any misuse of the software or any violation of terms of service of any platform that may arise from its use. Users choose to use or adapt the project at their own risk, and should be fully aware of the consequences of violating terms of service or ethical guidelines in their use of software.
   
## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.

