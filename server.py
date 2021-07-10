from flask import Flask,request,render_template 
from interpreter import *
  
app = Flask(__name__)   
@app.route('/',methods=["GET","POST"])
def gfg():
  if request.method=="POST":
    script=request.form.get('code')
    Input=request.form.get('input')
    flags=request.form.get('flags')
    if Input:
      Input=[eval(i) for i in Input.split("\n")]
    else:
      Input=[]
    data=execute(script,[''],Input,[*flags])
    fine="".join(data[0])
    l=str(len(script))
    leng=l+' bytes, '+l+' chars, (SBCS)'
    send="\n".join(map(str,Input))
    if send=='pass':
      send=''
    debug=request.form.get('debug')
    transpiled="".join(data[1])
    if debug:
      fine+="\n"
      fine+="=====================================\n"
      fine+=transpiled
    return render_template('index.html',output=fine,code=script,leng=leng,input=send,trans=transpiled,elapsed=data[2])        
  return render_template("index.html")
if __name__=='__main__':
   app.run(port=7777,debug=True)
