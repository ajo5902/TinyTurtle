# Tiny Turtle

This program takes in commands and executes them using
python's `turtle` module. 


##Basic TT Commands

TT Command | Argument | Turtle Command
-----------|----------|---------------| 
F          |###       | forward(###)  |
B          |###       | backward(###) |
L          |###       | left(###)  |
R          |###       | right(###)  |
C          |###       | circle(###)  |
U          |None       | up()  |
D          |None       | down()  |

##Enhanced TT Commands
TT Command | Argument | Turtle Command
-----------|----------|---------------| 
I          |#...@       | Iterate ...# times  |
P          |# ###       | Draw polygon of # sides % ### side length |

###Program Execution
The program execution is as follows:

1. First it prompts for a string containing any combination of basic and enhanced TT commands, as a single string.
2. The expanded TT program should be displayed to standard output. It contains
only the basic TT commands.
3. As each basic TT command is interpreted, the corresponding turtle command is
displayed to standard output. For example, if the basic TT command is F100, the
output is forward(100).
4. The program ”idles on” the mainloop call until the user closes the drawing
window.