#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program saying if an integer is positive or negative


def main():
    # This function sees if the user inputed the magic number

    print("Input a number and I'll tell you if it is "
          "zero, negative or positive")

    # Input
    integer = int(input("Please enter an integer: "))

    # Process
    if integer < 0:
        # Output
        print("The inputted integer is negative.")
    elif integer > 0:
        # Output
        print("The inputted integer is positive.")
    else:
        # Output
        print("The inputted integer is 0.")


if __name__ == "__main__":
    main()
