from flask import Flask,request,render_template 
from interpreter import *
  
app = Flask(__name__)   
@app.route('/',methods=["GET","POST"])
def gfg():
  if request.method=="POST":
    script=request.form.get('code')
    Input=request.form.get('input')
    if Input:
      Input=[eval(i) for i in Input.split("\n")]
    else:
      Input=[]
    data=execute(script,[''],Input)
    fine="".join(data)
    l=str(len(script))
    leng=l+' bytes, '+l+' chars, (SBCS)'
    send="\n".join(map(str,Input))
    if send=='pass':
      send=''
    return render_template('index.html',output=fine,code=script,leng=leng,input=send)        
  return render_template("index.html")
if __name__=='__main__':
   app.run(port=7777,debug=True)
