#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 24, 2025
# This program will ask the user to prompt a mass
# and acceleration to calculate the net force.

# def function is where we add the formula for Fnet.
def calc_Fnet(mass, acceleration):
    force = mass * acceleration
    return force


def main():
    acceleration = 0
# Get prompt from user for a mass.
    while True:
        try:
            mass = float(input("Enter a positive mass (Kg): "))
            if mass <= 0:
                print("Enter a positive mass: ")
            break
        except ValueError:
            print("Invalid. Please enter a valid mass: ")
# Get prompt from user for acceleration
    while True:
        falling_object = input("Is the object falling {yes or no}: ")
        if falling_object == "yes" or falling_object == "no":
            if falling_object == "yes":
                acceleration = 9.8
                print("Acceleration is 9.8 m/s². Since your object is free falling.")
                break
            else:
                # If object not free falling ask user to enter the acceleration.
                while True:
                    try:
                        acceleration = float(input("Enter an acceleration (m/s²): "))
                        break
                    except ValueError:
                        print("Invalid. Please enter a valid acceleration: ")
                break

    force = calc_Fnet(mass, acceleration)
    print(f"\nThe force acting on the object is {force} Newtons.")


if __name__ == "__main__":
    main()
