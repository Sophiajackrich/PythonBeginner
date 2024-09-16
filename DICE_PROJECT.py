import random

def roll_dice():
    """Simulate rolling two six-sided dice."""
    return random.randint(1, 6), random.randint(1, 6)

def main():
    points = 100
    print("Welcome to the Dice Game!")
    print(f"You start with {points} points.")

    while points > 0:
        # Player input
        chosen_number = int(input("Choose a number between 2 and 12: "))
        bet = int(input(f"Place your bet (you have {points} points): "))

        if bet > points:
            print("You cannot bet more than your current points.")
            continue

        # Roll the dice
        die1, die2 = roll_dice()
        dice_sum = die1 + die2
        print(f"The dice rolled {die1} and {die2}, with a sum of {dice_sum}.")

        # Determine the outcome
        if dice_sum < 7 and chosen_number < 7:
            points += bet
            print(f"Dice Sum is less than 7 and your number is less than 7. You win the bet! New points: {points}")
        elif dice_sum > 7 and chosen_number > 7:
            points += bet
            print(f"Dice Sum is greater than 7 and your number is greater than 7. You win the bet! New points: {points}")
        elif dice_sum == chosen_number:
            points += 4 * bet
            print(f"The sum matches your number! You win four times your bet! New points: {points}")
            break
        else:
            points -= bet
            print(f"You lose the bet. New points: {points}")
            

        # Ask if the player wants to continue
        if 0 <= points > 0 and dice_sum == chosen_number:
            continue_game = input("Do you want to continue the game? (yes/no): ").lower()
            if continue_game != 'yes':
                print("Thank you for playing!")
                break
    else:
        print("You have run out of points. Game over!")
            

if __name__ == "__main__":
    main()

















































































































































