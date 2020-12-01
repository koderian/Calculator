# Dependecies
import time
from art import *
import math
import operator
import random as rand
from colorama import Fore, Back, Style

calcArt = text2art("PyCalc", font="block")
off = False
on = True
print(calcArt)

# time.sleep(2)
pyCalc_welcome = (Fore.RED + "Welcome to PyCalc, solve problem to continue")
#for i in pyCalc_welcome:
#  print(i, flush=True, end="")
#  time.sleep(0.1)
pyCalc_possible_operations = [operator.add, operator.sub, operator.truediv, operator.mul]

def pyCalc_problem_op(list):
    global pyCalc_op
    global pyCalc_english_op_representation
    pyCalc_english_op_representation = ""
    pyCalc_op = rand.choice(list)
    if pyCalc_op == pyCalc_possible_operations[0]:
        pyCalc_english_op_representation = "+"
        return pyCalc_english_op_representation
        
    elif pyCalc_op == pyCalc_possible_operations[1]:
        pyCalc_english_op_representation = "-"
        return pyCalc_english_op_representation
        
    elif pyCalc_op == pyCalc_possible_operations[2]:
        pyCalc_english_op_representation = "/"
        return pyCalc_english_op_representation
        
    elif pyCalc_op == pyCalc_possible_operations[3]:
        pyCalc_english_op_representation = "*"
        return pyCalc_english_op_representation
    else:
        print("Error: Does not match")
        

pyCalc_problem_op(pyCalc_possible_operations)
print(Fore.WHITE, "", end="\n")
num1 = int(rand.randint(1,9))
num2 = int(rand.randint(1,9))
pyCalc_problem = str(num1) + " " + str(pyCalc_english_op_representation) + " " + str(num2)
unsolved = True
while unsolved is True:
    print("What is the solution to " + pyCalc_problem + ":") 
    correct_Answer = pyCalc_op(num1, num2)
    while answers is <3:
        



