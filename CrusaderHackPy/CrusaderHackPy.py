from tkinter.tix import INTEGER, MAX
from ReadWriteMemory import ReadWriteMemory
import keyboard
import os
import tkinter as tk

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
        t = process.read(self.goldPointer)
        self.goldValue = 0 if t <= 0 or t > 4e9 else t

    def addGold(self):
        process.write(self.goldPointer, self.goldValue + 500)
        print("500 gold added")

    def show(self):
        if self.goldValue <= 0 or self.goldValue > 4e9:
            print(self.id, "(OFFLINE)")
        else:
            print(self.id, " <=> ", self.goldValue)

    def refresh(self):
        t = process.read(self.goldPointer)
        self.goldValue = 0 if t <= 0 or t > 4e9 else t

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

def refreshPlayersInfo():
    for i in players:
        i.refresh()
        label_gold = root.grid_slaves(row=players.index(i), column=1)[0]
        label_gold.config(text="Gold: " + str(i.goldValue))
    root.update_idletasks()
    root.after(100, refreshPlayersInfo)
    
def toggle_color():
    if button["bg"] == "red":
        button.configure(bg="green")
    else:
        button.configure(bg="red")

def on_key(event):
    if event.char == 'i':
        print('i')
    elif event.char == 'o':
        p.addGold()
        print(p.name, "gold added")
    elif event.char == 'p':
        print('p')

root = tk.Tk()
root.title("Player Info")

for i, player in enumerate(players):
    label_name = tk.Label(root, text="Name: " + player.name)
    label_gold = tk.Label(root, text="Gold: " + str(player.goldValue))
    canvas = tk.Canvas(root, width=60, height=60)
    c = "white" if player.name == "Player" else player.name
    rectangle = canvas.create_rectangle(0, 0, 60, 60, fill=c)
    x1, y1, x2, y2 = canvas.coords(rectangle)
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    canvas.create_text(center_x, center_y, text=player.name, fill="black")

    label_name.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    label_gold.grid(row=i, column=1, padx=5, pady=5, sticky="w")
    canvas.grid(row=i, column=2, padx=5, pady=5)
    
def toggle_color():
    if button["bg"] == "red":
        button.configure(bg="green")
    else:
        button.configure(bg="red")

button = tk.Button(root, text="On/Off", bg="red", command=lambda: toggle_color())
button.grid(row=i+1, column=2, padx=5, pady=5)

refreshPlayersInfo()

root.bind('<Key>', on_key)

root.focus_set()
 
root.mainloop()


    