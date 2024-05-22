# Builduing url dynamically

from flask import Flask,redirect,url_for


app=Flask(__name__)

@app.route('/')
def members():
     return 'Welcome to my Youtubess Channel'
 
@app.route('/success/<int:score>')
def success(score):
     return '<html><body><h1>The result 1212 passed</h1></body></html>'

@app.route('/fail/<int:score>')
def fail(score):
     return 'Welcome fail to my Youtubess Channel' + str(score)
 
 
# Result Checker 
@app.route('/results/<int:marks>')
def results(marks):
     result=""
     if marks>50:
         result='success'
         
     else:
         result='fail'
     return redirect(url_for(result,score=marks))
 
 


if __name__=='__main__':
    app.run(debug=True)