'''
INPUTS THE RADIUS OF A CIRCLE AND CALCULATES THE AREA
'''

from math import pi

def rad():

    r = float(input ("Input the radius of the circle : "))
    print(f"The area of the circle with radius {r} is {pi * r ** 2}")

rad()

input("Press ENTER to exit")