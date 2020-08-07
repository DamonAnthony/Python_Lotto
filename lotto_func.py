# Damon Anthony Class 1
# Imported random for random numbers, sys for exit and datetime for current date
import random
import datetime
import sys


# Generating random numbers
def generate_lotto_num():
    """
    >>> a = generate_lotto_num()
    >>> all([1 <= num <= 50 for num in a])
    True
    """
    lotto_numbers = []

    for i in range(0, 6):
        number = random.randint(1, 49)
        # Checking if number is already in the list and changing if it is
        while number in lotto_numbers:
            number = random.randint(1, 49)

        lotto_numbers.append(number)
    lotto_numbers.sort()
    return lotto_numbers


# Checks how many matches
def checking_matches(l1, l2):
    """
    >>> list1 =  [1, 2, 3]
    >>> list2 = [3, 4, 5]
    >>> checking_matches(list1, list2)
    1
    """
    count = 0
    for i in l1:
        if i in l2:
            count += 1
    return count


# Checking prize category
def prize_check(correct_guesses):
    """
    >>> a = 5
    >>> prize_check(a)
    8584.00
    """
    if correct_guesses == 6:
        prize = 10000000.00
    elif correct_guesses == 5:
        prize = 8584.00
    elif correct_guesses == 4:
        prize = 2384.00
    elif correct_guesses == 3:
        prize = 100.50
    elif correct_guesses == 2:
        prize = 20.00
    else:
        prize = "No prize"
    return prize


# Exit
def exit():
    input("Press enter to exit...")
    sys.exit()


# Writing results to console
def display_output(lotto_numbers, guessed_numbers, number_matches, prize_won):
    print(str(datetime.date.today()) + "\n")
    print("These are the lotto numbers " + str(lotto_numbers) + "\n")
    print("These were your numbers " + str(guessed_numbers) + "\n")
    print("This is the number of matches " + str(number_matches) + "\n")
    print("This is what you've won " + str(prize_won) + "\n")


# If user age less than 18 then not allowing them to play
def check_age():
    # Checking user age
    try:
        age = int(input("Please enter your age: "))
    except TypeError:
        age = int(input("Please enter your age as a number: "))
    except ValueError:
        age = int(input("Please enter your age as a number: "))
    # Checking if user is old enough
    if age >= 18:
        pass
    elif age < 18:
        return sys.exit("You are underage and cannot play")


def taking_numbers():
    # Taking user input of 6 numbers
    guessed_numbers = []

    while len(guessed_numbers) < 6:
        try:
            user_number = int(input("Please enter a number between 1 and 49: "))
            # Checking if number is already in the list
            if user_number in guessed_numbers:
                print("Can not use duplicate numbers")
                continue
            # Checking if number is more than 50 or less than 1
            elif user_number > 49 or user_number < 1:
                print("Number must be between 1 and 49")
                continue
            else:
                guessed_numbers.append(user_number)
        except TypeError:
            print("That was not a number")
            continue
        except ValueError:
            print("That was not a number")
            continue

    guessed_numbers.sort()
    return guessed_numbers
