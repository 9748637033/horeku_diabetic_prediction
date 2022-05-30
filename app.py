
from flask import Flask , render_template,request
import joblib

# initialise the app
app=Flask(__name__)
model=joblib.load('dib_79.pkl')

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/deployment')
def deployment():
    return 'Deployment class'

@app.route('/Spectra')
def spectra():
    return 'This is spectra'

@app.route('/welcome')
def welcome():
    return 'welcome to the page'

@app.route('/gallery')
def gallery():
    return 'This is gallery page' 

@app.route('/blog')
def blog():
    return 'This is blog page'

@app.route('/konnagar')
def konnagar():
    return "This is konnagar. THis is kolkata"

@app.route('/predict', methods=['POST'])
def predict():

    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    
    print(preg,plas,pres,skin,test,mass,pedi,age)

    output=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    # output= model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0]==1:
      print('Diabetic')
    else:
        print('Non-Diabetic')


    # print(first_name)
    # print(Last_name)
    

    return 'Form submitted'   

app.run(debug=True)