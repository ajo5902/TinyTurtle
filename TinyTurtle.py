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

def getValue(string):
    """
    getValue takes a string of numbers and outputs it as an integer.

    :param string: a string composed of numbers.
    :return: an integer.
    """
    length = len(string) - 1
    idx = 0
    value = ""
    while string[idx] != " ":
        value += string[idx]
        idx += 1
        if idx > length:
            break
    return int(value)

def valLength(string):
    count = 0
    idx = 0
    while string[idx] != " ":
        count += 1
        idx += 1
        if idx < len(string):
            continue
        else:
            break
    return count


def tinyTurtle(cmd):
    idx = 0
    length = len(cmd) - 1
    ivalue = 0

    while cmd != "":
        if cmd[0] == "F":
            ivalue = getValue(cmd[1:])
            print("Forward(", str(ivalue), ")", sep="")
            cmdF(int(ivalue))
            cmdLength = valLength(cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break
        

tinyTurtle("F100 F100")


#idx = 1
#while cmd[idx] != " ":
#value += cmd[idx]
#idx += 1
#if idx > length:
#break