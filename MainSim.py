import math
import numpy as np
import random as rand

goodOne = "AA"
goodOne_duration_sec = 60
goodOne_uses = 2






def multikillToPoints(m): 
    return (50 if m == 1 else 60 + m*10)

def pointsToAmmo(p): 
    return p/10

def zombiesOnRound(r): 
    if r < 10:
        return ["0", "6", "8", "13", "18", "24", "27", "28", "28", "29"][r]
    else:
        return math.floor(24 + r / 5 * (.15 * r) * 3)

def machinePrice(r, gNum):
    match gNum:
        case 1:
            return 0
        case 2:
            return      2 ** (r//10) * 1000 + 500
        case 3:
            return 2 * (2 ** (r//10) * 1000 + 500)

class bag:
    def __init__(self):
        self.gumball_master = ["SO", "ABH", "AA", "IPS", "ArA"]
        self.gumball_bag_state = []
        self.choice = ""
    
    def takeFromBag(self):
        if self.gumball_bag_state == []:
            self.gumball_bag_state = rand.sample(self.gumball_master, 5)

        self.choice = self.gumball_bag_state.pop(0)

        return self.choice

class gun:
    def __init__(self, ammoCount, ammoMax, clipCount, clipMax, reloadTimeSecs):
        self.ammoCount = ammoCount
        self.ammoMax = ammoMax
        self.clipCount = clipCount
        self.clipMax = clipMax
        self.reloadTimeSecs = reloadTimeSecs
