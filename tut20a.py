# You have to build a "Number Guessing Game," in which a winning number is set to some integer value. The Program should take input from the user, and if the entered number is less than the winning number, a message should display that the number is smaller and vice versa.

# Instructions:
# 1. You are free to use anything we've studied till now.
# 2. The number of guesses should be limited, i.e (5 or 9).
# 3. Print the number of guesses left.
# 4. Print the number of guesses he took to win the game.
# 5. “Game Over” message should display if the number of guesses becomes equal to 0.
# You are advised to participate in solving this problem. This task helps you to become a good problem solver and helps you accepting the challenge and acquiring new skills.

n = 69
i = 5
print("RULES FOR THE GAME:\n1) You have to guess the number feeded in the system\n2) You have only 5 guesses after that you'll be eliminated\n")
while True:
    g = int(input("Guess and enter the number between 0 to 100:\n"))
    i = i - 1
    if g == 69:
        print("\nWonders!You were able to guess the number right you win\n")
        print("You took", 5 - i , "number of guesses\n")
        break
    elif i == 0:
        print("\nSORRY! GAME OVER")
        break
    elif g > 100:
        print("You have entered a number greater than 100.TRY AGAIN!\n")
        print(i, " more guesses left\n")
        continue
    elif g < 69 :
        print("Try entering a greater number this time\n")
        print(i, " more guesses left\n")
        continue
    elif g > 69:
        print("Try entering a smaller number this time\n")
        print(i, " more guesses left\n")
        continue
    else:
        print("Enter a valid integral input between , and this will deduct your one chance")
        print(i, " more guesses left\n")
        continue
    