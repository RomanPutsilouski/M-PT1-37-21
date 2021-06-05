from random import randint 

class Creature:

    def __init__(self, health, attack, level):
        self.health = health
        self.attack = attack
        self.level = level


class Hero(Creature):
    def __init__(self):
        Creature.__init__(self, randint(170, 280), randint(20, 40),23)


class Villian(Creature):
    def __init__(self):
        Creature.__init__(self, randint(190, 300), randint(25, 35), 26)

H = Hero()
V = Villian()



def fight():

    count = 0
    
    while H.health > 0 or V.health > 0:
        H.health =  H.health - V.attack
        V.health =  V.health - H.attack
        count +=1

    if H.health > V.health:
        return f"Hero has won! He made {count} strikes!"
    else:
        return f"Villian has won! He made {count} strikes!"
   
    
print(fight())

        
    


