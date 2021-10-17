#!/usr/bin/python

# Author: Nirjas Jakilim

# Problem Statement:
# Given an array of integers representing the color of each sock,
# You have to determine how many pairs of socks with matching colors there are.

# My Solution:
# Each array reprsent the colors of the socks. As we have to find the matching pairs that means
# we have to actually find the matching number pairs. For example: Suppose 10 is a color.
# So, if there is another 10 in this array then we count it as a pair. So, we have to
# actually count a occurance of a number and then divide it by 2 as we are only counting 2 as a pair.

# Importing Counter library
from collections import Counter
if __name__== '__main__':
    n = int(input()) # importing n
    c = 0 # counter value
    arr=list(map(int, input().split(' ')[:n])) # Array
    d = Counter(arr)
    for a in arr:
        if(d[a]>1):
            c+=int(d[a]/2) # Dividing the occurances by 2.
            d[a] = int(d[a]%2) # Resetting the occurances back to 1 so that it can't be counted again.
    print(c)
        
    
        
    