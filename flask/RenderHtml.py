from flask import Flask
from flask import render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('HomePage.html')


@app.route('/about')
def about():
    return render_template('about.html',UserName='SNT')

@app.route('/SignIn')
def SignIn():
  
        return render_template('SignIn.html')
   

@app.route('/hello',methods=[ 'POST'])
def hello():
        UserText=request.form['UserName']
        return render_template('hello.html',User=UserText)

# @app.route('/hello?UserName={str:string}')
# def hello(str):
#     return render_template('SignIn.html',User=str)


if __name__=="__main__":
    app.run(debug=True)