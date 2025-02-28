class Controler:
    def __init__(self,buttons,hotkeys):
        self.buttons = buttons
        self.hotkeys = hotkeys
    def describe_controller_status(self):
        print(f"The controller is currently in good status, {self.buttons} {self.hotkeys}")
    


class Player:
    Player_count = 0
    def __init__(self,playtime,age,race,controler_buttons,controler_hotkeys):
        
        self.playtime = playtime
        self.age = age
        self.race = race
        self.buttons = controler_buttons
        self.hotkeys = controler_hotkeys
        self.controller = Controler(self.buttons,self.hotkeys)
        Player.Player_count += 1
    def get_player_count(self):
        print(f"The current playercount is at : {Player.Player_count}")








Player1 = Player(9000,20,"Goblin","L1","cheat code")
Player2 = Player(2000,10,"Troll","L2","virus")
Player3 = Player(1000,5,"Elf","L3","pack")
Player3.controller.describe_controller_status()