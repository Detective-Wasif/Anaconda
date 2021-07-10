# This is an internal module which contains abstract data structures used only by the interpreter itself
# Document, Stack (WIP)

class Document:
  def __init__(self,x=0,y=0,wfill='-',hfill='|',corner='+',fill=' '):
    self.board=[]
    self.x=x
    self.y=y
    self.pos=(self.x,self.y)
    self.wfill=wfill
    self.hfill=hfill
    self.corner=corner
    self.fill=fill
    self.dir='right'
    self.props=['x','y','pos','wfill','hfill','corner','fill','dir']
  def pulse(self):
    return {attr:getattr(self,attr) for attr in self.props}
  def __str__(self):
    return "\n".join("".join(line) for line in self.board)
  def update(self):
    self.pos=(self.x,self.y)
  def downright(self,n):
    for coord in range(self.x,n):
      try:
        self.board[coord]
      except IndexError:
        self.board.append([self.fill]*(coord+1))
        self.board[coord][coord]='\\'
        self.x+=1
        self.y+=1
    self.update()
doc=Document()
print(doc.pulse())
doc.downright(5)
print(str(doc))
print(doc.pos)
