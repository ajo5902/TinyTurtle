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
    print("Forward(", str(value), ")", sep="")
    tt.fd(value)

def cmdB(value):
    """
    cmdB moves the turtle marker backward a certain amount.

    :param value: the distance the turtle marker moves backward
    :return:
    """
    print("Back(", str(value), ")", sep="")
    tt.back(value)

def cmdL(value):
    """
    cmdL turns the turtle left a certain number of degrees.
    :param value: the amount of degrees the turtle will turn to
                 the left.
    :return:
    """
    print("Left(", str(value), ")", sep="")
    tt.left(value)

def cmdR(value):
    """
    cmdR turns the turtle marker right a certain number of degrees.
    :param value: the amount the turtle turns to the right.
    :return:
    """
    print("Right(", str(value), ")", sep="")
    tt.right(value)

def cmdC(value):
    """
    cmdC draws a circle of a certain radius.

    :param value: radius of the circle to be drawn
    :return:
    """
    print("Circle(", str(value), ")", sep="")
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

def processArg(cmd, string):

    value = getValue(string[0:])

    if cmd == "F":
        cmdF(value)
        cmdLength = valLength(string)

    elif cmd == "B":
        cmdB(value)
        cmdLength = valLength(string)

    elif cmd == "L":
        cmdL(value)
        cmdLength = valLength(string)

    elif cmd == "R":
        cmdR(value)
        cmdLength = valLength(string)

    elif cmd == "C":
        cmdC(value)
        cmdLength = valLength(string)

    elif cmd == "P":
        cmdLength = valLength(string) + 1
        secCom = getValue(string[cmdLength:])
        cmdLength = cmdLength + valLength(str(secCom))
        cmdP(value, secCom)

    return cmdLength

def cmdP(sides, length):
    angle = 360 / sides
    while sides != 0:
        cmdF(length)
        cmdL(angle)
        sides -= 1

def tinyTurtle(cmd):
    idx = 0
    length = len(cmd) - 1
    ivalue = 0

    while cmd != "":
        if cmd[0] == "F":
            cmdLength = processArg("F", cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break

        elif cmd[0] == "B":
            cmdLength = processArg("B", cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break

        elif cmd[0] == "L":
            cmdLength = processArg("L", cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break

        elif cmd[0] == "R":
            cmdLength = processArg("R", cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break

        elif cmd[0] == "C":
            cmdLength = processArg("C", cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break

        elif cmd[0] == "U":
            print("Up()")
            cmdU()
            if len(cmd) == 1:
                break
            else:
                cmd = cmd[2:]

        elif cmd[0] == "D":
            print("Down()")
            cmdD()
            if len(cmd) == 1:
                break
            else:
                cmd = cmd[2:]

        elif cmd[0] == "P":
            cmdLength = processArg("P", cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break







tinyTurtle("F100 P4 100 U F200 D P3 100 ")


#idx = 1
#while cmd[idx] != " ":
#value += cmd[idx]
#idx += 1
#if idx > length:
#break