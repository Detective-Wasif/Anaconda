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
