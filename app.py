from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',url="wwww.baidu.com",list=[1,3,6],dict={'url':"aaa",'name':'zyq'})

if __name__ == '__main__':
    app.run()
