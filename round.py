#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on November 2020
# This program calculates a rounded number

import math


def round_number(num, precision):
    # Rounds a number to a specified precision

    num[0] = num[0] * 10**precision[0] + 0.5
    num[0] = int(num[0])
    num[0] = num[0] * 10**-precision[0]


def main():
    # This function receives input

    number_var = []
    round_precision_var = []

    # Input
    number = float(input("Enter the number you want to round: "))
    round_precision = float(input("Enter how many decimal places"
                                  " you want to round by: "))
    print(" ")
    number_var.append(number)
    round_precision_var.append(round_precision)

    # Call Functions
    round_number(number_var, round_precision_var)

    print("The rounded number is {0}".format(number_var[0]))


if __name__ == "__main__":
    main()
