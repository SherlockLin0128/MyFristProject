"""
File: PotholeFilling.py
Name: TODO:Sherlock
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99_beeper()
        go_out()

def go_in():
    """
    pre_condition:karel ia at the upper left of the pothole, facing East
    post_condition:karel is in the pothole,facing south.
    """
    move()
    turn_right()
    move()
def go_out():
    """
    pre_condition:karel is in the pothole,facing south.
    post_condition:karel ia at the upper left of the pothole, facing East

    """
    turn_around()
    move()
    turn_right()
    move()
def put_99_beeper():
    for i in range(99):
        put_beeper()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()




# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
