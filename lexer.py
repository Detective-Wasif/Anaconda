s='100(⍵15%0=[`FizzBuzz`|⍵5%0=[`Fizz`|⍵3%0=[`Buzz`|⍵;;;d; xx'
import re
# My poor man's parser for Anaconda written in pure Python (But it gets the job done)
class Token:
  def __init__(self,Type):
    self.command=Type
  def __repr__(self):
    return self.command
def transform(s):
  k=s
  d=re.sub('[^[{(ƛλ]','',s)[::-1]
  close={'{':'}','(':')','ƛ':';','[':']','λ':';'}
  for _ in range(10):
    for x,y in enumerate(d):
      i=s.replace(';','X',x).find(';')
      l=[*s]
      l[i]=close[y]
      s=''.join(l)
  if s[-1]==']':
    s+=k[-1]
  return s
def lexer(s):
  lex=[]
  s=s.replace('\`','ƙ')
  idx=0
  while idx<len(s):
    if s[idx].isdigit():
      cap=''
      try:
        while (s[idx].isdigit() or s[idx]=='.'):
          cap+=s[idx]
          idx+=1
      except:
        pass
      f=int
      if '.' in cap:
        f=float
      lex.append(f(cap))
      continue
    if s[idx]=='`':
      cap=''
      idx+=1
      while s[idx]!='`':
        cap+=s[idx]
        idx+=1
      lex.append(cap.replace('ƙ','`'))
      idx+=1
      continue
    if s[idx]=='[':
     cap=''
     idx+=1
     cup=1
     while cup:
       if s[idx]=='[':
         cup+=1
       if s[idx]==']':
         cup-=1
       cap+=s[idx]
       idx+=1
     pair=cap[:-1]
     free=0
     branch=pair.rfind('|')
     for a,b in enumerate(pair):
       if b=='[':
         free+=1
       if b==']':
         free-=1
       if (not free) and (b=='|'):
         branch=a
     pair=[Token('if')]+[*map(lexer,[pair[:branch],pair[branch+1:]])]
     lex.append(pair)
     continue
    if s[idx]=='{':
     cap=''
     idx+=1
     cup=1
     while cup:
       if s[idx]=='{':
         cup+=1
       if s[idx]=='}':
         cup-=1
       cap+=s[idx]
       idx+=1
     block=cap[:-1] 
     catch=[Token('while')]+[lexer(block)]
     lex.append(catch)    
     continue
    if s[idx]=='(':
     cap=''
     idx+=1
     cup=1
     while cup:
       if s[idx]=='(':
         cup+=1
       if s[idx]==')':
         cup-=1
       cap+=s[idx]
       idx+=1
     block=cap[:-1] 
     catch=[Token('for')]+[lexer(block)]
     lex.append(catch)    
     continue
    if s[idx]=='v':
      idx+=1
      catch=[Token('vectorise')]+lexer(s[idx])
      lex.append(catch)
      idx+=1
      continue
    if s[idx]=='ƛ':
     cap=''
     idx+=1
     cup=1
     infunc=False
     while cup:
       if s[idx]=='λ':
         infunc=True
       if s[idx]=='ƛ':
         cup+=1
       if (s[idx]==';') and (not infunc):
         cup-=1
       if (s[idx]==';') and infunc:
         infunction=False     
       cap+=s[idx]
       idx+=1
     block=cap[:-1] 
     catch=[Token('map')]+[lexer(block)]
     lex.append(catch)    
     continue
    if s[idx]=='λ':
     cap=''
     idx+=1
     cup=1
     inmap=False
     while cup:
       if s[idx]=='ƛ':
         inmap=True
       if s[idx]=='λ':
         cup+=1
       if (s[idx]==';') and (not inmap):
         cup-=1
       if (s[idx]==';') and inmap:
         inmap=False
       cap+=s[idx]
       idx+=1
     block=cap[:-1] 
     catch=[Token('function')]+[lexer(block)]
     lex.append(catch)    
     continue
    lex.append(Token(s[idx]))
    idx+=1
  return lex


#print(lexer(transform(s)))
