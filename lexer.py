s='`Hello``World`+1.45-5`Anacon\`da`[`getch`[`a`|`b`01wasif]|`else`]wasif{0{1{2}}}'

class Token:
  def __init__(self,Type):
    self.command=Type
  def __repr__(self):
    return self.command
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
     branch=pair.rfind('|')
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
     idx+=1     
     continue
    lex.append(Token(s[idx]))
    idx+=1
 
  return lex


print(lexer(s))
