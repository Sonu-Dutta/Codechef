# Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.

# Class ID	Ship Class
# B or b	BattleShip
# C or c	Cruiser
# D or d	Destroyer
# F or f	Frigate
# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains a character.

# Output
# For each test case, display the Ship Class depending on ID, in a new line.

# Input

# 3 
# B
# c
# D

# Output
# BattleShip
# Cruiser
# Destroyer

t=int(input("Enter number of test cases: "))
while(t>0):
    text=input("Enter character: ")
    if(text=="f" or text=="F"):
        print("Frigate")
    elif(text=="b" or text=="B"):
        print("BattleShip")
    elif(text=="d" or text=="D"):
        print("Destroyer")
    elif(text=="c" or text=="C"):
        print("Cruiser")
    
    
    t-=1