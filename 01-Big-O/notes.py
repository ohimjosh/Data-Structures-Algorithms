# -----------------------------------------------------------

# What is Big O?
# It is a way to compare two sets of code
# Compare code 1 vs code 2 to see how efficient they run

# Factors for Big O
# Time Complexity
# How long it takes for a program to run
# Measured in the number of operations it takes to
# complete something

# Space Complexity
# How much memory a program takes

# -----------------------------------------------------------

# Best Case: Ω
# Average Case: θ
# Worst Case: O

# -----------------------------------------------------------

# Big O of O(n)

def print_items(n):
    for i in range(n):
        print(i)

# print_items(10)

# We pass in n and it ran n times
# Linear run time
# Proportional

# -----------------------------------------------------------

# Drop Constants

def drop_constants(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

# drop_constants(10)

# Run time: n + n times Or 2n

# Simplified run time is O(n)
# You can just drop the constants to simplify it

# -----------------------------------------------------------

# Big O         O(n^2)

def nsquared(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# nsquared(10)

# When printed we got n * n times 
# Run time: n^2
# O(n^2)

# Lets add another for loop
def new(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
# new(3)

# Although it is n * n * n times we must simplify it
# simplified run time is O(n^2)

# In a time complexity standpoint it is less efficient than O(n)

# -----------------------------------------------------------

# Drop Non-Dominants

def newloop(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

# newloop(3)

# first nested loop ran O(n^2)
# second loop ran O(n)

# Total runtime: O(n^2 + n)

# Add n is not important
# Since n^2 is more dominant 

# Runtime: O(n^2)

# -----------------------------------------------------------

# O(1)
# constant time

def addition(n):
    return n + n

# addition(2)

# there is one operation so it is O(1)
# even if it is n + n + n it willl still be O(1)

# Number of operations remain constant as n increases

# O(1) IS THE MOST EFFICIENT BIG O
# The most optimal solution

# -----------------------------------------------------------

# Big O         O(log n)

# lets say we have 8 items 
# [1 2 3 4 5 6 7 8]

# we are looking for a item so we keep splitting the list
# [1 2 3 4]

# our item is not here is we split
# [1 2]

# until we find it
# [1]

# The number of steps it took to find the item is 3

# we had 8 items in the list 
# and it took 3 steps to find a number

# 2^3 = 8

# this is the same as 

# log(2)8 = 3 

# O(log n) is very efficient but not as efficient as O(1)

# another log is O(nlog n)

# O(nlog n) is the most efficient you can make a sorting algorithm
# used in merge sort and quick sort

# -----------------------------------------------------------

# Different Terms for Inputs

# What if instead of one parameter its two

def twopara(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# first loop is O(a)
# second loop is O(b)

# adding them together
# Runtime: O(a + b)

# you cannot simplify it further

# What if you have nested for loops

def nestedtwopara(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)

# multiply them together
# Runtime: O(a * b)

# -----------------------------------------------------------

# Lists

list = [11, 3, 23, 7]

list.append(17)

print(list)

list.pop(17)

# All we do is add or remove at the end of the list
# Runtime: O(1)

# HOWEVER
# if you remove at index 0, 11
# then the list will need to be moved and reordered

# so 3 is index 0, 23 is index 1 and 7 index 2

# IF THERE IS REINDEXING
# Runtime: O(n)

# n representing the number of items in the list

# if you are looping through a list for a value
# Runtime: O(n)

# if you are looking for an index 
# Runtime: O(1)

# -----------------------------------------------------------

# BIG O SUMMARY

# O(n^2)    Loop within a loop

# O(n)      Proportional

# O(log n)  Divide and Conquer

# O(1)      Constant
