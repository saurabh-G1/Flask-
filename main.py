# Building url dynamically
# HTTP verb GET and POST
# Jinja2 Template
'''
{%.....%}  condition ,for loops
{{.....}}  expressions to print output
{#......#} for putting comments
'''

from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)

@app.route('/')
def members():
     return render_template('index.html')
 
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>50:
       res="PASS"
    else:
      res="FAIL"
    exp={'score':score,'result':res}
    
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
     return 'You are Failed with the score of ' + str(score)
 
 
# Result Checker 
@app.route('/results/<int:marks>')
def results(marks):
     result=""
     if marks>50:
         result='success'
         
     else:
         result='fail'
     return redirect(url_for(result,score=marks))
 
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
    total_score = (science + maths + c + datascience)/4
    res=""
   
    return redirect(url_for('success',score=total_score))
        
    
    
    
    
if __name__=='__main__':
    app.run(debug=True)