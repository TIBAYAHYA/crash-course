# the functionality of this calss is to store the settings of our alien invasion game
import pyautogui

class Settings:
    def __init__(self):
        self.screen_width = pyautogui.size()[0]
        self.screen_height = pyautogui.size()[1]
        self.bg_color = (0,0,0)