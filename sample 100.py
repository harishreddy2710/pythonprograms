# counter = 0
# while counter<10:
#     counter += 3
#     print(counter)
# 1.
# l = []
# for i in range(2000, 3201):
#     if (i % 7 == 0) & (i % 5 != 0):
#         l.append(str(i))
# print(','.join(l))
# print(len(l))
#
# # 2.
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
#
# x = int(input())
# print(fact(x))
# from audioop import reverse
#
# import self as self


# #3.
# n = int(input())
# d = dict()
# for i in range(1, n + 1):
#     d[i] = i * i
# print(d)

# # 4.
# values = input()
# l = values.split(',')
# t = tuple(l)
# print(l)
# print(t)

# # 5.
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#         print(self.s.upper())
#
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()

# #6.
# import math
#
# c = 50
# h = 30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
# print(sep=','.join(value))
# print(value)

#  #.7
# input_str = input()
# dimensions = [int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#       multilist[row][col] = row*col
#
# print(multilist)

# # 8.
# items = [x for x in input().split(',')]
# items.sort()
# print(sep="".join(items))
# print(items)

# 9.
# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#  print(sentence)

# 10.
# s = input()
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))
# hello world and practice makes perfect and hello world again
#
# 11.
# value = []
# items = [x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp % 5:
#         value.append(p)
# print(','.join(value))
# 0100,0011,1010,1001
#
# 12.
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
#         values.append(s)
# print(",".join(values))

# 13.
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"] += 1
#     elif c.isalpha():
#         d["LETTERS"] += 1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])
# hello world! 123

# 14.
# s = input()
# d={"UPPER CASE" : 0, "LOWER CASE" : 0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"] += 1
#     elif c.islower():
#         d["LOWER CASE"] += 1
#     else:
#         pass
# print("UPPER CASE", d["UPPER CASE"])
# print("LOWER CASE", d["LOWER CASE"])
# Hello world!
#
# 15.
# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print(n1+n2+n3+n4)
# i/p:9

# 16.
# values = input()
# numbers = [x for x in values.split(",") if int(x) % 2 != 0]
# print(",".join(numbers))
# 1,2,3,4,5,6,7,8,9

# 17.
# netAmount = 0
# while True:
#   s = input()
#   if not s:
#       break
# values = s.split(" ")
# operation = values[0]
# amount = int(values[1])
# if operation == "D":
#     netAmount += amount
# elif operation == "W":
#     netAmount -= amount
# else:
#     pass
# print(netAmount)
#
# 18.
# import re
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#   if len(p)<6 or len(p)>12:
#     continue
#   else:
#     pass
#   if not re.search("[a-z]",p):
#     continue
#   elif not re.search("[0-9]",p):
#     continue
#   elif not re.search("[A-Z]",p):
#     continue
#   elif not re.search("[$#@]",p):
#     continue
#   elif re.search("\s",p):
#     continue
#   else:
#    pass
#    value.append(p)
# print(",".join(value))
# ABd1234@1,a F1#,2w3E*,2We3345

# 19.
# from operator import itemgetter
# l = []
# while True:
#  s = input()
#  if not s:
#    break
#  l.append(tuple(s.split(",")))
# print(sorted(l, key=itemgetter(0,1,2)))
# Tom,19,80
# John,20,90
# Jony,17,91
# jony,17,93
# Json,21,85
# # 20.
# def putNumbers(n):
#     i = 0
#     while i < n:
#         j = i
#         i += 1
#         if j % 7 == 0:
#             yield j
# for i in putNumbers(100):
#     print(i)
#
# # 21.
# import math
#
# pos = [0, 0]
# while True:
#     s = input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction == "UP":
#         pos[0] += steps
#         pos[0] -= steps
#     elif direction == "LEFT":
#         pos[1] -= steps
#     elif direction == "RIGHT":
#         pos[1] += steps
#     else:
#         pass
# print(int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2))))
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# 22.
# freq = {}  # frequency of words in text
# line = input()
# for word in line.split():
#     freq[word] = freq.get(word, 0) + 1
# words = freq.keys()
# words.sort()
# for w in words:
#     print("%s:%d" % (w, freq[w]))

# 23.
# def square(num):
#     return num ** 2
#
#
# print(square(2))
# print(square(3))

# 24.
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

#
# def square(num):
#     """Return the square value of the input number.The input number must be integer.
#  """
#     return num ** 2
#
#
# print(square(2))
# print(square.__doc__)

# 25.
# class Person:
#     name = "Person"
#
#     def __init__(self, name=None):
#         self.name = name
#
#
# # self.name is the instance parameter
# jeffrey = Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name))
#
# nico= Person()
# nico.name = "Nico"
# print("%s name is %s" % (Person.name, nico.name))

# # 26.
# def SumFunction(number1, number2):
#     return number1+number2
# print(SumFunction(1,2))

# # 27.
# def printValue(n):
#     print(str(n))
#
#
# printValue(3)
# print(type(printValue))

# 28.
# def printValue(s1,s2):
#     print(int(s1)+int(s2))
# printValue("3","4") #7

# 29.
# def printValue(s1,s2):
#     print(s1+s2)
# printValue("3","4") #34

# 30.
# def printValue(s1, s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1 > len2:
#         print(s1)
#     elif len2 > len1:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
#
#
# printValue("one", "three")

# 31.
# def checkValue(n):
#
#     if n % 2 == 0:
#         print("It is an even number")
#     else:
#         print("It is an odd number")
#
#
# checkValue(7)

# 32.
# def printDict():
#     d = dict()
#     d[1] = 1
#     d[2] = 2**2
#     d[3] = 3**2
#     print(d)
# printDict()

# 33.
# def printDict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i ** 2
#     print(d)
#
#
# printDict()

# 34.
# def print_dict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i ** 2
#     for (k, v) in d.items():
#         print(v)
#
#
# print_dict()

# 35.
# def printDict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=i**2
#     for k in d.keys():
#         print(k)
#     for j in d.values():
#         print(j)
#
# printDict()

# 36.
# def printList():
#     li = list()
#     for i in range(1, 21):
#         li.append(i ** 2)
#     print(li)
#
#
# printList()

# 37.Define a function which can generate a list where the values are
# square of numbers between 1 and 20 (both included). Then the function
# needs to print the first 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list
# Solution:

# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[:20])
# printList()

# 38.
#
# Define a function which can generate a list where the values are
# square of numbers between 1 and 20 (both included). Then the function
# needs to print the last 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list
# Solution
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[-5:])
# printList()

# 39.
# Define a function which can generate a list where the values are
# square of numbers between 1 and 20 (both included). Then the function
# needs to print all values except the first 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list
# Solution
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[5:])
# printList()

# 40.
# Define a function which can generate and print a tuple where the value
# are square of numbers between 1 and 20 (both included).
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.
# # Solution
# def printTuple():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(tuple(li))
# printTuple()

# 41.
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print
# the first half values in one line and the last half values in one
# line.
# Hints:
# Use [n1:n2] notation to get a slice from a tuple.
# Solution
# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print(tp1)
# print(tp2)

# 42.
# Write a program to generate and print another tuple whose values are
# even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.
# Solution
# tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# li = list()
# for i in tp:
#     if i % 2 == 0:
#         li.append(i)
# tp2 = tuple(li)
# print(tp2)

# 43.
# Write a program which accepts a string as input to print "Yes" if the
# string is "yes" or "YES" or "Yes", otherwise print "No".
# Hints:
# Use if statement to judge condition.
# Solution
# s = input()
# if s == "yes" or s == "YES" or s == "Yes":
#     print("Yes")
# else:
#     print("No")

# 44.

# Write a program which can filter even numbers in a list by using
# filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.
# Solution
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evenNumbers = filter(lambda x: x % 2 == 0, li)
# print(','.join(evenNumbers))
#
# 45
# Write a program which can map() to make a list whose elements are
# square of elements in [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.
# Solution
# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x**2, li)
# print(list(squaredNumbers))
