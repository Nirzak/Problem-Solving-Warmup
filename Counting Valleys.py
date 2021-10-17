#!/usr/bin/python

"""
Author: Nirjas Jakilim

Problem Statement:
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly n steps,
for every step it was noted if it was an uphill, U , or a downhill, D step. Hikes always start and end at sea level,
and each step up or down represents a 1 unit change in altitude. We define the following terms:
A mountain is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

My Solution:
Here we only have to count the valleys that we have traversed. A valley is only traversed when someone has stepped down
and then step up to sea level. As sea level is stated at level = 0, So we have to increment the number of valley only
when we found D occurs and then level = 0. 'Cause, it means we have stepped down and then moved up to the sea level.
On the other hand, if step-up occurs we have to increment the level and otherwise decrement the level to keep it synced with
the occurrence of step-down. 
"""

if __name__== '__main__':
    n = int(input()) # Input N. Number of steps
    steps = input().strip() # Steps will contain either D or U.
    level = 0
    valley = 0 # Initially Level and Valley both are 0
    for i in range(n):
        if(level == 0 and steps[i] == 'D'): # if sea level found after down steps then it means we have traversed valley already. So increment it.
            valley += 1
        if(steps[i] == 'U'): # IF step up found then increase the level by 1 otherwise decrease it by 1.
            level += 1
        else:
            level -= 1
    print(valley) # Print the answer
