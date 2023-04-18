from tkinter.tix import INTEGER, MAX
from ReadWriteMemory import ReadWriteMemory
import keyboard
import os

rwm = ReadWriteMemory()

process = rwm.get_process_by_name("Stronghold Crusader.exe")
process.open()

class Game:
    gold = 0x00000000
    name = "base"

    def __init__(self):
        self.id = self.name
        self.goldAddress = self.gold
        self.goldPointer = process.get_pointer(self.goldAddress)
        self.goldValue = process.read(self.goldPointer)

    def addGold(self):
        process.write(self.goldPointer, self.goldValue + 500)
        print("500 gold added")

    def show(self):
        if self.goldValue <= 0 or self.goldValue > 4e9:
            print(self.id, "(OFFLINE)")
        else:
            print(self.id, " <=> ", self.goldValue)


class Player(Game):
    gold = 0x0115FCF8
    name = "Player"

    def __init__(self):
        super().__init__()
    

class Blue(Game):
    gold = 0x0116AAD4
    name = "Blue"

    def __init__(self):
        super().__init__()

class Gray(Game):
    gold = 0x0116E4C8
    name = "Gray"

    def __init__(self):
        super().__init__()

class Purple(Game):
    gold = 0x01171EBC
    name = "Purple"

    def __init__(self):
        super().__init__()

class Orange(Game):
    gold = 0x011636EC
    name = "Orange"

    def __init__(self):
        super().__init__()

class LightBlue(Game):
    gold = 0x011758B0
    name = "LightBlue"

    def __init__(self):
        super().__init__()

class Yellow(Game):
    gold = 0x011670E0
    name = "Yellow"

    def __init__(self):
        super().__init__()

class Green(Game):
    gold = 0x011792A4
    name = "Green"

    def __init__(self):
        super().__init__()



p = Player()
b = Blue()
g = Gray()
pu = Purple()
o = Orange()
l = LightBlue()
y = Yellow()
gr = Green()

players = [p, b, g, pu, o, l, y, gr]

def showPlayerInfo():
    for i in players:
        i.show()

while 1:
    for i in players:
        i.__init__()
    
    try:
        if keyboard.read_key() == 'q':
            break
        elif keyboard.read_key() == '[':
            p.addGold()
        elif keyboard.read_key() == ']':
            os.system('cls')
            showPlayerInfo()
        
    except:
        break


    