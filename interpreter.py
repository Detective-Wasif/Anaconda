import os
import re
import sys
import math
import random
import string
import time
import urllib.request
import base64
import itertools
import collections
import hashlib
import operator
import turtle
import numpy as np
import sympy
from lexer import *
from functools import *
from datetime import date
from datetime import datetime as dt
global commands
commands={
'+':('inter=add(lhs,rhs)',2,'rhs=stack.pop();lhs=stack.pop()','stack.push(inter)'),
'-':('inter=sub(lhs,rhs)',2,'rhs=stack.pop();lhs=stack.pop()','stack.push(inter)'),
' ':('pass',0),
"\n":('pass',0),
'w':('stack.wrap(stack.pop())',0),
'X':('stack.pair()',0),
'$':('stack.swap()',0),
':':('stack.dup()',0),
'_':('stack.pop()',0)
}
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
    self.push(stack.peek())
  def trip(self):
    self.stack.extend([stack.peek()]*2)
  def swap(self):
    self.stack[-2],self.stack[-1]=self.stack[-1],self.stack[-2]
  def rotl(self,units=1):
    for i in range(units+1):
      self.push(self.top())
  def rotr(self,units=1):
    for i in range(units+1):
      self.prepend(self.pop())
  def fetch(self,pos):
    self.push(self.stack[pos])
  def sort(self):
    self.stack.sort()
  def reverse(self):
    self.stack=self.stack[::-1]
  def join(self,delim=''):
    self.push(delim.join(map(str,self.stack)))
  def wrap(self,items,all=False):
    if all:
      self.stack=[stack]
    else:
      wrap=[]
      for _ in range(items):
        wrap.append(self.pop())
      self.push(wrap[::-1])
  def pair(self):
      rhs=stack.pop()
      lhs=stack.pop()
      stack.push([lhs,rhs])
  def __str__(self):
   self.join(', ')
   return self.pop()
stack=Stack()
variables=[]
register=string.ascii_lowercase
functions=[]
lazy=False
frac=False
def isnum(*args):
  return all(type(arg) in [int,float,bool] for arg in args)
def ifbs(*args):
  return all(type(arg) in [int,float,bool,str] for arg in args)
def isit(*args):
  return all(type(arg) in [str,list] for arg in args)
def add(lhs,rhs):
  types=[type(lhs),type(rhs)]
  if types[0]==list and types[1]!=list:
    return [add(x,rhs) for x in lhs]
  elif types==[list]*2:
    return [add(x,y) for x,y in zip(lhs,rhs)]
  elif types[0]!=list and types[1]==list:
    return str(lhs).join(map(str,rhs))
  elif isnum(lhs,rhs):
    return lhs+rhs
  else:
    return str(lhs)+str(rhs)
def sub(lhs,rhs):
  types=[type(lhs),type(rhs)]
  if types[0]==list and types[1]!=list:
    return [sub(x,rhs) for x in lhs]
  elif types==[list]*2:
    return [sub(x,y) for x,y in zip(lhs,rhs)]
  elif types[0]==str and ifbs(rhs):
    return lhs.replace(str(rhs),'')
  elif isnum(lhs) and isit(rhs):
    temp=[*rhs]
    del temp[lhs]
    if types[1]==str:
      return ''.join(temp)
    else:
      return temp
  elif isnum(lhs,rhs): 
    return lhs-rhs
def mul(lhs,rhs):
  types=[type(lhs),type(rhs)]
  if types[0]==list and types[1]!=list:
    return [mul(x,rhs) for x in lhs]
  elif types==[list]*2:
    return [mul(x,y) for x,y in zip(lhs,rhs)]
  if ifbs(lhs) and isnum(rhs):
    return lhs*rhs 
def product(array):
  return reduce(operator.__mul__,array)
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
data=open(sys.argv[1]).read()
data=lexer(data)
def compile(src,indent=0):
  compiled=''
  for token in src:
    if type(token) in [int,float,str]:
      compiled+=' '*indent+'stack.push('+repr(token)+")\n"
      continue
    if type(token)==list:
      c,args=str(token[0]),token[1:]
      if c=='if':
        compiled+=' '*indent+"if stack.peek():\n"
        indent+=2
        compiled+=compile([Token(' ')]+args[0],indent)
        compiled+=' '*(indent-2)+"else:\n"
        compiled+=compile([Token(' ')]+args[1],indent)
        indent-=2
        continue
      if c=='while':
        compiled+=' '*indent+"while stack.peek():\n"
        indent+=2
        compiled+=compile([Token(' ')]+args[0],indent)
        indent-=2
        continue
      if c=='vectorise':
        compiled+=' '*indent+"after=[]\n"
        compiled+=' '*indent+"for lhs in stack.pop():\n"
        indent+=2
        compiled+=' '*indent+commands[str(args[0])][0]+"\n"
        compiled+=' '*indent+"after.append(inter)\n"
        indent-=2
        compiled+=' '*indent+"stack.push(after)\n"
        compiled+=' '*indent+"after=[]\n"
        continue
      if c=='for':
        compiled+=' '*indent+"for lhs in range(1,stack.pop()+1):\n"
        indent+=2
        compiled+=compile(args[0],indent)
        indent-=2
        continue
    else:
      if str(token) in commands:
        io=commands[str(token)]
        if io[1]:
          for _ in [2,0,3]:
            compiled+=' '*indent+io[_]+"\n"
        else:
          compiled+=' '*indent+io[0]+"\n"
  return compiled
print(compile(data))
#print(sub(2,[1,2,3]))
