from flask import Flask,request,render_template 
  
app = Flask(__name__)   
@app.route('/', methods =["GET","POST"])
def gfg():
  if request.method=="POST":
    script=request.form.get('code')
    return render_template('index.html',output=script,code=script)        
  return render_template("index.html")
if __name__=='__main__':
   app.run(port=7777,debug=True)
