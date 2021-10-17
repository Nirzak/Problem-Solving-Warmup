#!/usr/bin/python

"""
Author: Nirjas Jakilim

Problem Statement:
See hackerrank: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

My Solution:
Here an array of clouds are given. Clouds can only have 0 or 1 values. We can't jump on the level 1 clouds. 
Only level 0 clouds can be traversed. So we have to find the minimum number of jumps required to jump to the last cloud. The player can jump on a maximum of two clouds simultaneously but only when there is no level 1 clouds are in the middle.
For example: suppose clouds are 0 1 0 0 0 1 here, in the middle, we take a jump from the 3rd cloud to the 5th cloud because
there is no level 1 clouds are there. But we can't take a jump from cloud 1 to 3. because in the 2nd position there is a
level 1 cloud there. So, our main task will be to set a condition to avoid this level 1 cloud and the rest of the time
we can take two jumps.

"""
if __name__=='__main__':
    n = int(input())
    clouds = list(map(int, input().split(' ')))
    jumps = 0
    i = 0
    while i < n - 1:
        if i + 2 >= n or clouds[i + 2] == 1:   # Condtion in which jumps on two clouds are impossible
            i = i + 1 # jumps on two clouds are not possible. So, increamenting 1.
            jumps = jumps + 1
        else:
            i = i + 2 #Jumping on two clouds
            jumps = jumps + 1
    print(jumps)
