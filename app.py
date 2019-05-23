from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def hello():
    return app.send_static_file('index.html')
    
@app.route('/hello', methods = ['POST'])
def hello1():
    
    
    
    print'fuck'
    
    return app.send_static_file('hello.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)