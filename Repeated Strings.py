#!/usr/bin/python

"""
Author: Nirjas Jakilim

Problem Statement:
https://www.hackerrank.com/challenges/repeated-string/problem

My Solution:
The problem is mainly to count the number of a in a repeated string within a particular range. For example:
Suppose a string is aba and n = 10 that means we have to find occurances of a in "abaabaabaa" this string.
So, the solution is either building the string with a loop and then count the occurance of a in that string.
But there is an optimal solution there. and this is just multiply the count of 'a' in the given string 'aba' with
the value of 'n' and then divide it with the lenght of the string. It's the basic rule of Unitary method.
But now there is a problem. It exclude the remainder string that is not full. In the above example which the extra
'a' in the 10th position of the string "abaabaabaa". So we have count it separately and add with our previous answer.That's it.

"""
st = input().strip()
n = int(input().strip())
count_of_a = st.count("a")*int((n/len(st))) # Initial Count
count_of_a += st[:n%len(st)].count("a") # Counting on the remainder string
print(count_of_a)