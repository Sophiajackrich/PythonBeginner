# Explain what classes are- classes are such a union of functions to influence objects.

# Functions work by themselves, and you can just call them, like "print()."

#Methods, on the other hand, should only be applied to objects. 
## Methods cannot be called by themselves, e.g., the "append()" method for lists.


# Create a class 
class Enemy:
    def __init__(self, health, attack):
        self.health = health

        self.attack = attack

    def be_attacked(self, attack): # damage in attack size

        self.health = self.health - attack # decrease in health
    

# Create character 1
enemy = Enemy(health=330, attack=10)

#print(enemy)

print(enemy.health)

print(enemy.attack)

# Create character 2
enemy_2 = Enemy(health=200, attack=18)

enemy.be_attacked(10)

print(enemy.health)

# create a "hit" variable
hits = 0
win = False # win check
# create a while loop of "True" to check health life left
while True:
    if enemy.health <= 0 and enemy_2.health <= 0: # if the health of both became <= 0

        print('Tie')

        win=True
    elif enemy.health <= 0: # if the health of 1 enemy <= 0
        print('The second won')

        print("He has health left", enemy_2.health)

        win = True

    elif enemy_2.health <= 0: # if the health of 2 enemy <= 0

        print('The first won')

        print("He has health left", enemy.health)

        win = True
    if win is True: # victory. This is another block of conditions

        print("Hits are: ", hits)

        break

    hits += 1

    enemy.be_attacked(enemy_2.attack)

    enemy_2.be_attacked(enemy.attack)

    

    print(hits, enemy.health, enemy_2.health)




