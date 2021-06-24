class Document:
  def __init__(self,x=0,y=0,wfill='-',hfill='|',corner='+',fill=' '):
    self.board=[[]]
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
doc=Document()
print(doc.pulse())
print(str(doc))
