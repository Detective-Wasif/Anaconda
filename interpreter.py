import os
import re
import math
import random
import string
import time
import urllib.request
import base64
import functools
import itertools
import collections
import hashlib
import operator
#import turtle
import numpy as np
import sympy
#from lexer import *
from datetime import date
from datetime import datetime as dt
class Stack:
  def __init__(self,prep=[]):
    self.stack=prep
  def push(self,val):
    self.stack.append(val)
  def pop(self):
    return self.stack.pop()
  def peek(self):
    return self.stack[-1]
  def top(self):
    return self.stack.pop(0)
  def over(self):
    return self.stack[0]
  def len(self):
    return len(self.stack)
  def prepend(self,val):
    self.stack.insert(0,val)
  def dup(self):
    self.push(stack[-1])
  def trip(self):
    self.stack.extend([stack[-1]]*2)
  def swap(self):
    self.stack[-2],self.stack[-1]=self.stack[-1],self.stack[-2]
  def rotl(self,units=1):
    for i in range(units):
      self.push(self.top())
  def rotr(self,units=1):
    for i in range(units):
      self.prepend(self.pop())
  def fetch(self,pos):
    self.push(self.stack[pos])
  def sort(self):
    self.stack.sort()
  def reverse(self):
    self.stack=self.stack[::-1]
  def join(self,delim=''):
    self.push(delim.join(map(str,self.stack)))
  def __str__(self):
   self.join(' ')
   return self.pop()
stack=Stack()
variables=[]
register=string.ascii_lowercase
functions=[]
def product(array):
  return functools.reduce(operator.__mul__,array)
def transpose(array,filler=0):
  return list(map(list,itertools.zip_longest(array,fillvalue=filler)))
def integer_partitions(number,I=1):
  partitions=[[number]]
  for i in range(I,number//2+1):
    for p in integer_partitions(number-i,i):
      partitions.append([i]+p)
  return partitions
def partitions(iterable):
  ret=[]
  for i in range(1,len(iterable)):
    for sub in partitions(iterable[i:]):
      sub.insert(0,iterable[:i])
      ret.append(sub)
  ret.append([iterable])
  return ret
print(partitions('abcd'))
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.rotr()
print(str(stack))
