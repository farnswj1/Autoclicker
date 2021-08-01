# Imported libraries
from pynput.keyboard import GlobalHotKeys
from pynput.mouse import Controller, Button
from threading import Thread
import time

# Auto Clicker class
class AutoClicker:
    click_rate = 1/100  # in seconds

    def __init__(self):
        '''Initializes the auto clicker'''

        print("Initializing Autoclicker... ", end="")
        self.__listener = None
        self.__mouse = Controller()
        self.__run_autoclick = False
        self.__threads = []
        self.__x = 0
        self.__y = 0
        print("done!")

    
    def __autoclick(self):
        '''Automatically clicks the saved coordinates'''

        # Keep clicking until autoclick is disabled
        while self.__run_autoclick:
            self.__mouse.position = (self.__x, self.__y)
            self.__mouse.click(Button.left, 1)
            time.sleep(self.click_rate)
    

    def __toggle_autoclick(self):
        '''Toggles the autoclick functionality'''

        self.__run_autoclick = not self.__run_autoclick
        
        # If autoclick is enabled, use threading to autoclick
        if self.__run_autoclick:
            self.__x, self.__y = self.__mouse.position
            self.__threads = [Thread(target=self.__autoclick, daemon=True) for _ in range(1)]
            
            for thread in self.__threads:
                thread.start()

    
    def __terminate(self):
        '''Stops the autoclicker'''

        self.__run_autoclick = False
        
        # Wait for the thread(s) to stop first
        for thread in self.__threads:
            thread.join()
        
        self.__listener.stop()


    def run(self):
        '''Runs the autoclicker program'''

        print("Setting up listeners... ", end="")
        hotkeys = {
            "<alt>+<shift>+a": self.__toggle_autoclick,
            "<alt>+<shift>+q": self.__terminate
        }

        with GlobalHotKeys(hotkeys) as self.__listener:
            print("done!\nTo toggle autoclicking, press: ALT+SHIFT+A\nTo exit, press: ALT+SHIFT+Q")
            self.__listener.join()
        
        print("Exiting program...")


# Execute the program
if __name__ == "__main__":
    AutoClicker().run()
