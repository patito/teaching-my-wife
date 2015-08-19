#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.1 Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of
# the numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333

def all_in_one():
    total = 0
    count = 0
    average = 0
    num = "notdone"

    while num != "done":
        
        num = raw_input('Enter a number: ')
        try:
            num = int(num)
        except:
            print('Try again, invalid number')
            break

        total = total + int(num)
        count =  count + 1
        average = total / count

        num = raw_input('Enter a number: ')


    return total, count, average

        
if __name__ == '__main__':
    t, a, c = all_in_one()
    print ("Total = " + str(t))
    print ("Average = " + str(a))
    print ("Count = " + str(c))
