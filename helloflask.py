from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask"

@app.route('/hello')
def helloworld():
    return "Hello World"


@app.route('/<string:str>')
def helloStr(str):
    return "<p>"+"Hello "+str+"</p>"

if __name__=="__main__":
    app.run(debug=True)