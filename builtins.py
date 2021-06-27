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
from datetime import date
from datetime import datetime as dt

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
