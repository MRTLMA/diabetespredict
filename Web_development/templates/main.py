from flask import Flask,render_template,request
import joblib

# model=joblib.load("/Users/abuadam/Desktop/new/pickle/diabetic_joblib.pkl")


#intialize the app

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html")
...

@app.route("/contact-us")
def contanct():
    return render_template("contact.html")
'''''
@app.route("/counselingform")
def form():
    return render_template("form.html")
@app.route("/submitform",methods=['post'])
def submitform():
    
    Pregnancies=int(request.form.get('Pregnancies'))
    Glucose=int(request.form.get('Glucose'))
    BloodPressure=int(request.form.get('BloodPressure'))
    SkinThickness=int(request.form.get('SkinThickness'))
    Insulin=int(request.form.get('Insulin'))
    BMI=int(request.form.get('BMI'))
    DiabetesPedigreeFunction=int(request.form.get('DiabetesPedigreeFunction'))
    Age=int(request.form.get('Age'))
    prediction=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    if prediction[0]==1:
        return "You are diabetic"
    else:
        return "You are Non diabetic"
'''' '''
app.run(debug=True)