
import random

import main

random.randint(1, 10)

main.get_print_name()

def get_high_low_grades():
    grades = [78, 92, 65, 92, 81, 74, 99, 67, 88, 99]

    grades.sort(reverse=True)
    print(grades[:3])

    grades.sort()
    print(grades[:3])

get_high_low_grades()