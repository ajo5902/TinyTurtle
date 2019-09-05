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
        if string[cmdLength] == "0":
            cmdLength += 1
        secCom = getValue(string[cmdLength:])
        cmdLength = cmdLength + valLength(str(secCom))
        cmdP(value, secCom)

    elif cmd == "I":
        cmdLength = valLength(string) + 1
        secCom = string[cmdLength: ]
        cmdLength = cmdLength + len(secCom)
        cmdI(value, secCom)

    return cmdLength

def cmdP(sides, length):
    angle = 360 / sides
    while sides != 0:
        cmdF(length)
        cmdL(angle)
        sides -= 1

def cmdI(amount, command):
    loops = amount
    commandcpy = command[:]

    while loops != 0:
        while command != "" and command[0] != "@":
            if command[0] == "F":
                cmdLength = processArg("F", command[1:])
                if cmdLength < len(command) + 1:
                    command = command[cmdLength + 2:]
                else:
                    pass

            elif command[0] == "B":
                cmdLength = processArg("B", command[1:])
                if cmdLength < len(command) + 1:
                    command = command[cmdLength + 2:]
                else:
                    pass

            elif command[0] == "L":
                cmdLength = processArg("L", command[1:])
                if cmdLength < len(command) + 1:
                    command = command[cmdLength + 2:]
                else:
                    pass

            elif command[0] == "R":
                cmdLength = processArg("R", command[1:])
                if cmdLength < len(command) + 1:
                    command = command[cmdLength + 2:]
                else:
                    pass

            elif command[0] == "C":
                cmdLength = processArg("C", command[1:])
                if cmdLength < len(command) + 1:
                    command = command[cmdLength + 2:]
                else:
                    pass

            elif command[0] == "U":
                print("Up()")
                cmdU()
                if len(command) == 1:
                    break
                else:
                    command = command[2:]

            elif command[0] == "D":
                print("Down()")
                cmdD()
                if len(command) == 1:
                    break
                else:
                    command = command[2:]

            elif command[0] == "P":
                cmdLength = processArg("P", command[1:])
                if cmdLength < len(command) + 1:
                    command = command[cmdLength + 2:]
                else:
                    pass

            elif command[0] == "I":
                cmdLength = processArg("I", command[1:])
                if cmdLength < len(command) + 1:
                    command = command[cmdLength + 2:]
                else:
                    pass

        loops -= 1
        command = commandcpy


def commandExpander(cmd):
    commandSnip = ""
    while cmd != "":
        if cmd[0] == "F":
            nextcmd = valLength(cmd[1:]) + 2
            print(cmd[0] + str(getValue(cmd[1:])), end=" ")
            cmd = cmd[nextcmd:]

        elif cmd[0] == "B":
            nextcmd = valLength(cmd[1:]) + 2
            print(cmd[0] + str(getValue(cmd[1:])), end=" ")
            cmd = cmd[nextcmd:]

        elif cmd[0] == "L":
            nextcmd = valLength(cmd[1:]) + 2
            print(cmd[0] + str(getValue(cmd[1:])), end=" ")
            cmd = cmd[nextcmd:]

        elif cmd[0] == "R":
            nextcmd = valLength(cmd[1:]) + 2
            print(cmd[0] + str(getValue(cmd[1:])), end=" ")
            cmd = cmd[nextcmd:]

        elif cmd[0] == "C":
            nextcmd = valLength(cmd[1:]) + 2
            print(cmd[0] + str(getValue(cmd[1:])), end=" ")
            cmd = cmd[nextcmd:]

        elif cmd[0] == "U":
            print(cmd[0], end=" ")
            cmd = cmd[2:]

        elif cmd[0] == "D":
            print(cmd[0], end=" ")
            cmd = cmd[2:]

        elif cmd[0] == "I":
            loops = getValue(cmd[1:])

            cmd1 = valLength(cmd[1:]) + 2
            cmd1C = cmd[cmd1]
            cmd1Val = getValue(cmd[cmd1+1:])
            cmd1ValOrig = str(cmd1Val)
            secCmdLoc = valLength(str(cmd1Val))

            if cmd[cmd1 + 1] == "0":
                secCmdLoc += 1
                cmd1ValOrig = "0" + str(cmd1Val)

            cmd2 = cmd1 + secCmdLoc + 2
            cmd2C = cmd[cmd2]
            cmd2Val = getValue(cmd[cmd2+1:])
            cmd2ValOrig = str(cmd2Val)

            if cmd[cmd2 +1] == "0":
                cmd2 += 1
                cmd2ValOrig = "0" + str(cmd2Val)

            cmd1Merged = cmd1C + cmd1ValOrig
            cmd2Merged = cmd2C + cmd2ValOrig

            nextcmd = cmd1 + cmd2 + valLength(str(cmd2Val)) + 1

            while loops != 0:
                print(cmd1Merged, cmd2Merged, end=" ")
                loops -= 1

            cmd = cmd[nextcmd:]

        elif cmd[0] == "P":
            sides = getValue(cmd[1:])
            angle = int(360 / sides)

            angleSTR = str(angle)
            length = getValue(cmd[valLength(cmd[1:]) + 2:])

            if cmd[valLength(cmd[1:]) + 2] == "0":
                length = "0" + str(length)

            if len(angleSTR) < 3:
                angleSTR = "0" + angleSTR

            cmdLength1 = valLength(cmd[1:]) + 1
            cmdLength2 = valLength(cmd[cmdLength1 + 1:]) + 2

            nextcmd = cmdLength1 + cmdLength2

            while sides != 0:
                print("F", length, sep="", end=" ")
                print("L", angleSTR, sep="", end=" ")
                sides -= 1
            cmd = cmd[nextcmd:]


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

        elif cmd[0] == "I":
            cmdLength = processArg("I", cmd[1:])
            if cmdLength < length + 1:
                cmd = cmd[cmdLength + 2:]
            else:
                break


#commandExpander("P4 050")


commandExpander("P3 100 U F200 D P4 050 U F100 D P8 025 U B500 D I2 C050 L180 @")

#processArg("I", "2 F100 C10 F100 U D P3 100 @")


#cmdI('2', 'F100 C10 F100 U D P3 100 @')

# = "cool beans"

#tinyTurtle("I2 I4 F100 L090 @ F100 @")


#idx = 1
#while cmd[idx] != " ":
#value += cmd[idx]
#idx += 1
#if idx > length:
#break