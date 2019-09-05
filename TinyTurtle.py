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
    """
    valLength returns the length of a value of a turtle
    command.
    :param string: string of values
    :return: int
    """
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
    """
    processArg takes the TT command and arguement, processes it,
    and returns the length of the value of the command.
    :param cmd: a string containing a TT command. (F, L, R, C, U, D, ETC)
    :param string: a string of numerical values.
    :return: int
    """

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
    """
    cmdP draws a polygon of * sides and * side length

    :param sides: integer representing the number of sides to be drawn.
    :param length: integer representing the legnth of the sides.
    :return:
    """
    angle = 360 / sides
    while sides != 0:
        cmdF(length)
        cmdL(angle)
        sides -= 1

def cmdI(amount, command):
    """

    :param amount: integer representing the amount of iterations to complete.
    :param command: a string representing the commands to be iterated through.
    :return:
    """

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
    """
    commandExpander expands the string of TT commands provided by
    the user, and outputs those commands.

    :param cmd: string of TT commands to be expanded.
    :return:
    """

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
    """
    tinyTurtle breaks down a string of TT commands and process it
    using the processArg func.

    :param cmd:
    :return:
    """

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

def main():
    """
    main prompts the user for a string of turtle commands, expands them
    to standard output, and then interpretes them through the tinyTurtle
    function.
    :return:
    """
    ttcmd = input("Enter Tiny Turtle program (CMD+D or CTRL+D to terminate):")
    print("\n")
    if ttcmd != "^D":
        commandExpander(ttcmd)
    else:
        pass
    print("\n")
    print("Evaluating...")
    print("\n")
    tinyTurtle(ttcmd)
    tt.done()

main()
