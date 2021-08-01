# Autoclicker
This script allows the user to set up an autoclicker, which is currently programmed to run at 100 clicks per second.

## Setup & Installation
First, install the dependencies: `pip install -r requirements.txt`

## How to Use
With Python 3.6 or newer, run the script via `python autoclicker.py`

Then, place the mouse at the desired position on the screen.

To toggle the autoclicker, press **ALT+SHIFT+A**. Note that the autoclicker will lock the mouse in the position that that mouse was when autoclicking was enabled.

To exit the program, press **ALT+SHIFT+Q**.

## Known Bugs
Sometimes the program doesn't stop completely and immediately on command. It's likely that the event listener's thread(s) still run despite the program being called to terminate. They may eventually stop, but after a random duration of time following termination of the program, usually several seconds.