"""
# Copyright William Song, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is a tester file for Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Man, that makes this look official. 
# Good luck!

# Note evaluate's formatting is:
# variables
# values
# formula
# output

from formula_game_functions import build_tree, draw_formula_tree, evaluate, play2win

test = ["Formulas"]
# You can comment these out to help you reduce the clutter while testing
test.append("build_tree")
test.append("draw_formula_tree")
test.append("evaluate")
test.append("play2win")



# Formulas from the assignment and piazza
# Valid formulas from the assignment sheet
a1 = "x"
a2 = "-y"
a3 = "(x*y)"
a4 = "((-x+y)*-(-y+x))"
a5 = "((x+y)*((y+z)*(-y+-z)))"
# Invalid formulas from the assignment sheet
a6 = "X"
a7 = "x*y"
a8 = "-(x)"
a9 = "(x+(y)*z)"
# Valid from Piazza
p1 = "(x+-y)"
p2 = "(((x*y)*z)*w)"
p3 = "--x"
p4 = "----------------x"
p5 = "(-x*(y+z))"
p6 = "((x+y)*(x+z))"
p7 = "((x+y)*((y+z)*(-y+-z)))"
p8 = "(---x*y)"
p9 = "-(x+y)"
# t(o_ot)
p10 = "(a+(((((c*v)*(t+u))+-((o+-z)+((p+(r*s))*-q)))+(d*e))*((f+-(y+z))+-((x+j)*((k+(l+w))+(m*-n))))))"
# Invalid formulas from piazza
f1 = "(x+y*z)"
f2 = "(x*y*z)"
f3 = "((x+y)*(x-y)*(x+z))"
f4 = "(x+(u*v*w*z)+y) "
f5 = "-x-y"
f6 = "(x+y*x+y)"
f7 = "x)"
f8 = "++++x"
f9 = "-(-a)"
f10 = "(x+y)*(x+z)"
f11 = "-(ab)"
f12 = "(a+(B*-c))"
f13 = "(x * c)"
f14 = "-+x"
f15 = "!a"
f16 = "(x+x(()"
f17 = "((x+y))"
f18 = ")x+y("
f19 = "(x+y))"
f20 = "((x*y)"
f21 = "((x+y)*((y!z)*(-y+-z)))"
f22 = ""
f23 = " "
f24 = "(a+*+*+*b)"
f25 = "(a+*)"
f26 = "(((((x*y)))))"
f27 = "(x*y) "
assignment_pass = [a1, a2, a3, a4, a5]
assignment_fail = [a6, a7, a8, a9]
piazza_pass = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
piazza_fail = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27]

# build_tree
if "build_tree" in test:
    print("=======================build_tree=======================")
    print("========Failures========")
    for formula in assignment_fail:
        print(formula)
        print(build_tree(formula))
        print("\n")
    for formula in piazza_fail:
        print(formula)
        print(build_tree(formula))
        print("\n")
    print("========Passes========")
    for formula in assignment_pass:
        print(formula)
        print(build_tree(formula))
        print("\n")
    for formula in piazza_pass:
        print(formula)
        print(build_tree(formula))
        print("\n")

# draw_formula_tree
if "draw_formula_tree" in test:
    print("====================draw_formula_tree====================")
    for formula in assignment_pass:
        print(formula)
        print(draw_formula_tree(build_tree(formula)))
        print("\n")
    for formula in piazza_pass:
        print(formula)
        print(draw_formula_tree(build_tree(formula)))
        print("\n")

# evaluate
if "evaluate" in test:
    print("\n\n\n\n\n\n\n\n")
    print("==================evaluate==================")

    values1 = ["1", "0"]
    values2 = ["11", "10", "01", "00"]
    values3 = ["111", "110", "101", "011", "100", "010", "001", "000"]
    values4 = ["1111", "1110", "1101", "1011", "1100", "1010", "1001",
    "1000", "0111", "0110", "0101", "0011", "0100", "0010", "0001", "0000"]

    variables = "x"
    for values in values1:
        print(variables)
        print(values)
        print(a1)
        print(evaluate(build_tree(a1), variables, values))
        print("\n")

    variables = "y"
    for values in values1:
        print(variables)
        print(values)
        print(a2)
        print(evaluate(build_tree(a2), variables, values))
        print("\n")

    variables = "xy"
    for values in values2:
        print(variables)
        print(values)
        print(a3)
        print(evaluate(build_tree(a3), variables, values))
        print("\n")

    variables = "xy"
    for values in values2:
        print(variables)
        print(values)
        print(a4)
        print(evaluate(build_tree(a4), variables, values))
        print("\n")    

    variables = "xyz"
    for values in values3:
        print(variables)
        print(values)
        print(a5)
        print(evaluate(build_tree(a5), variables, values))
        print("\n")

    variables = "xy"
    for values in values2:
        print(variables)
        print(values)
        print(p1)
        print(evaluate(build_tree(p1), variables, values))
        print("\n")

    variables = "wxyz"
    for values in values4:
        print(variables)
        print(values)
        print(p2)
        print(evaluate(build_tree(p2), variables, values))
        print("\n")

    variables = "x"
    for values in values1:
        print(variables)
        print(values)
        print(p3)
        print(evaluate(build_tree(p3), variables, values))
        print("\n")

    variables = "x"
    for values in values1:
        print(variables)
        print(values)
        print(p4)
        print(evaluate(build_tree(p4), variables, values))
        print("\n")

    variables = "xyz"
    for values in values3:
        print(variables)
        print(values)
        print(p5)
        print(evaluate(build_tree(p5), variables, values))
        print("\n")

    variables = "xyz"
    for values in values3:
        print(variables)
        print(values)
        print(p6)
        print(evaluate(build_tree(p6), variables, values))
        print("\n")

    variables = "xyz"
    for values in values3:
        print(variables)
        print(values)
        print(p7)
        print(evaluate(build_tree(p7), variables, values))
        print("\n")

    variables = "xy"
    for values in values2:
        print(variables)
        print(values)
        print(p8)
        print(evaluate(build_tree(p8), variables, values))
        print("\n")

    variables = "xy"
    for values in values2:
        print(variables)
        print(values)
        print(p9)
        print(evaluate(build_tree(p9), variables, values))
        print("\n")

# play2win
if "play2win" in test:
    print("\n\n\n\n\n\n\n\n")
    print("==================play2win==================")
    a1_tree = build_tree(a1)
    print(a1)
    print(play2win(a1_tree, "E", "x", ""))
    print()
    print(a1)
    print(play2win(a1_tree, "A", "x", ""))
    print()

    a2_tree = build_tree(a2)
    print(a2)
    print(play2win(a2_tree, "E", "y", ""))
    print()
    print(a2)
    print(play2win(a2_tree, "A", "y", ""))
    print()

    a3_tree = build_tree(a3)
    print(a3)
    print(play2win(a3_tree, "EE", "xy", ""))
    print()
    print(a3)
    print(play2win(a3_tree, "EA", "xy", ""))
    print()
    print(a3)
    print(play2win(a3_tree, "AE", "xy", ""))
    print()
    print(a3)
    print(play2win(a3_tree, "AA", "xy", ""))
    print()
    print(a3)
    print(play2win(a3_tree, "EE", "xy", "1"))
    print()
    print(a3)
    print(play2win(a3_tree, "EA", "xy", "0"))
    print()
    print(a3)
    print(play2win(a3_tree, "AE", "xy", "1"))
    print()
    print(a3)
    print(play2win(a3_tree, "AA", "xy", "0"))
    print()