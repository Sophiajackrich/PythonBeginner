# Explain what classes are- classes are such a union of functions to influence objects.

# Functions work by themselves, and you can just call them, like "print()."

#Methods, on the other hand, should only be applied to objects. 
## Methods cannot be called by themselves, e.g., the "append()" method for lists.


# Import library
import random

# Create a class 
class Enemy:
    def __init__(self, name, health, attack):
        self.health = health

        self.attack = attack

        self.name = name

    def be_attacked(self, attack): # damage in attack size

        self.health = self.health - attack # decrease in health


# Create characters, using the "name" parameter
enemy_1 = Enemy(name='Knight', health=330, attack=10)

enemy_2 = Enemy(name='Fighter', health=200, attack=18)

enemy_3 = Enemy(name='Killer', health=150, attack=25)

# Create another class to inherit from "Enemy" class
class User(Enemy):
    def __init__(self, name, health, attack, armor = 10):
        self.max_health = health
        self.armor = armor
        super().__init__(name, health, attack) # we inherit from the parent
        
    # Add a health restoration method to the User class.
    def heal(self):
        if not self.health >= self.max_health:
            health = self.health // 10

            self.health += health

            print('You have restored', health, 'your current health', self.health)

        else:

            print('Impossible to restore health')

    def be_attacked(self, attack):
        self.health = int(self.health - (attack - self.armor))
        if self.armor > 0:

            self.armor -= int(attack/2)

            if self.armor < 0:

                self.armor = 0
  

# Now create a user character
user = User(name='My_name', health=200, attack=16)

# make a random choice of one of the 3 characters
enemies = [enemy_1, enemy_2, enemy_3]
enemy = random.choice(enemies)
print('Your opponent is', enemy.name)


#create a loop with the game, inwhich info o "health" & "attack"
while True:

    print(f'Your health: {user.health}, your attack: {user.attack}')

    print(f"Opponent's health: {enemy.health}, opponent's attack {enemy.attack}")
    
    userinput = input('\nSelect an action:\n1 - increase health\n2 - attack\n')
    
    if userinput == '1':
        user.heal()

    if userinput == '2':
        enemy.be_attacked(user.attack) # we attack the enemy

    user.be_attacked(enemy.attack) # the enemy attacks us

    print('You have got', enemy.attack, 'damage')

    if user.health <= 0 or enemy.health <= 0: # check health

        print('Tie')

        break
    elif user.health <= 0:

        print('You lose')

        break

    elif enemy.health <= 0:

        print('You won')

        break
    
    print(f'Your health: {user.health}, your attack: {user.attack}, your armor {user.armor}')




