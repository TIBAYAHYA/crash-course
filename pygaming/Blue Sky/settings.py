#the blue sky game settings
import pyautogui

class Settings:
    def __init__(self):
        self.screen_width = pyautogui.size()[0]
        self.screen_height = pyautogui.size()[1]
        self.bg_color = (0,0,255) # blue color is 0 0 255