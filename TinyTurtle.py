"""
Author: Abereni Opuiyo
File: TinyTurtle.py

Turtle interpreter!
"""

import turtle as tt

def cmdF(value):
    """
    cmdF moves the turtle marker forward a certain amount.
    :param value: How far you want the turtle to move.
    :return:
    """
    tt.fd(value)

def cmdB(value):
    """
    cmdB moves the turtle marker backward a certain amount.

    :param value: the distance the turtle marker moves backward
    :return:
    """

    tt.back(value)

def cmdL(value):
    """
    cmdL turns the turtle left a certain number of degrees.
    :param value: the amount of degrees the turtle will turn to
                 the left.
    :return:
    """

    tt.left(value)

def cmdR(value):
    """
    cmdR turns the turtle marker right a certain number of degrees.
    :param value: the amount the turtle turns to the right.
    :return:
    """

    tt.right(value)

def cmdC(value):
    """
    cmdC draws a circle of a certain radius.

    :param value: radius of the circle to be drawn
    :return:
    """

    tt.circle(value)

def cmdU():
    """
    cmdU raises the turtle marker up from the canvas.

    :return:
    """

    tt.up()

def cmdD():
    """
    cmdD raises the turtle marker up from the canvas.

    :return:
    """

    tt.down()

def tinyTurtle(cmd):
    idx = 0
    value = ""
    length = len(cmd) - 1
    if cmd[0] == "F":
        idx = 1
        while cmd[idx] != " ":
            value += cmd[idx]
            idx += 1
            if idx > length:
                break
        print("Forward (", value, ")", sep="")
        cmdF(int(value))


tinyTurtle("F100")

