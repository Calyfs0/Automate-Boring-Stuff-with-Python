# Guess the number page 50

import random

number = random.randint(1, 20)
max_turns = 10
for guess_count in range(0, max_turns - 1):
    print("Guess the number")
    num = int(input())

    if num < number:
        print(
            f"You guessed a smaller number. Keep guessing. You have {max_turns-guess_count - 1} turns left!"
        )
    elif num > number:
        print(
            f"You guessed a larger number. Keep guessing. You have {max_turns-guess_count - 1} turns left!"
        )
    else:
        break

if num == number:
    print(f"{num} is correct. You guessed the correct number in {guess_count} turns.")

else:
    print(f"The correct number was {number}. Better luck next time buddy!")
