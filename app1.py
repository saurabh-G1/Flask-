from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my youtube hello hg v channel"

@app.route('/member')
def member():
    return "welcome to my youtube hello hg v11111111 channel"


if __name__ =='__main__':
   app.run(debug=True)
