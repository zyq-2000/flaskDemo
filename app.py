from flask import Flask,render_template,url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootStrap=Bootstrap(app)


@app.route('/')
def hello_world():
    print(url_for('list',id='baidu.com'))
    return render_template('test.html',url="wwww.baidu.com",list=[1,3,6],dict={'url':"aaa",'name':'zyq'})
@app.route('/list/<id>')
def list():
    return render_template('test.html',url="wwww.baidu.com")

if __name__ == '__main__':
    app.run(debug=True)
