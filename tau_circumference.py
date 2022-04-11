#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import constants


def main():
    # I calculate circumference

    # input
    radius = int(input("Enter radius of the circle in mm: "))

    # process
    circumference = constants.TAU * radius

    # output
    print("Circumference is {} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
