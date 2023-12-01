#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 30th, 2023
# This program asks the user for their grade level
# then displays the mark that corresponds to that level


def calc_mark(level):
    # Return mark to main using If else
    if level == "4++":
        return 98
    elif level == "4+":
        return 95
    elif level == "4":
        return 90
    elif level == "4-":
        return 84
    elif level == "3+":
        return 78
    elif level == "3":
        return 75
    elif level == "3-":
        return 71
    elif level == "2+":
        return 68
    elif level == "2":
        return 65
    elif level == "2-":
        return 61
    elif level == "1+":
        return 58
    elif level == "1":
        return 55
    elif level == "1-":
        return 51
    elif level == "R":
        return 25
    else:
        return -1


def main():
    # get level from user
    user_level = input("Enter your grade level: ")

    # Call function to find mark
    calculated_mark = calc_mark(user_level)

    # Check if user mark is invalid
    if calculated_mark == -1:
        print("{} is not a valid level.".format(user_level))
    else:
        # Display mark
        print("Your mark is {}%.".format(calculated_mark))


if __name__ == "__main__":
    main()
