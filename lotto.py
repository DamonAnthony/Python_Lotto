# Damon Anthony Class 1
from lotto_func import *


# Input
check_age()
guessed_numbers = taking_numbers()

# Processing
lotto_num = generate_lotto_num()
matches = checking_matches(guessed_numbers, lotto_num)
result = prize_check(matches)

# Output
display_output(lotto_num, guessed_numbers, matches, result)
exit()
