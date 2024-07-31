"""
Number Guessing Game
Henry James Rotunno
"""
GUESSES = 6
import random
def main():
    # accumulator for ending loop
    w = 0
    l = 0
    # get random number, MUST BE NUM. Loop for playing again too
    while True:
        num = random.randint(1,100)
        w_or_l = play_game(num)

        # win or loss logic
        if w_or_l == 'W':
            w += 1
        else:
            l += 1
        # Loop to ask for play again
        """
        This function ends when the user no longer wants to play
        """
        keep_going = input('Would you like to play again? Enter "y" for yes: ')
        # No
        if keep_going == 'y':
            main()
            break
        # Display wins and loss
        else:
            print(f'Games won {w}')
            print(f'Games lost {l}')
            break


def get_user_guess():
    while True:
        user_guess = input('Enter a number from 1 and 100: ')
        # Input validation
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess > 0 and user_guess <= 100:
                return user_guess
# Pass num (random) to play game
def play_game(num):
# Accumulate, -1
    n = GUESSES
# Logic, loop that accepts new number with guess
    while n != 0:
        guess = get_user_guess()
        n -= 1
        # Win, RETURN "W"
        if guess == num:
            print(f'Congratulations, you guessed the number after {GUESSES - n} guesses')
            # send to main
            return 'W'
        # Too small
        elif guess < num:
            print(f'Your guess is too low! You have {n} guesses remaining')
        # Too big
        else:
            print(f'Your guess is too high! You have {n} guesses remaining')

    print(f'Sorry, you ran out of guesses. The number was {num}.')

    return 'L'



if __name__ == "__main__":
    main()






