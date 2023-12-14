import joblib

model=joblib.load("/Users/abuadam/Desktop/new/pickle/diabetic_joblib.pkl")

prediction=model.predict([[2,4,5,6,3,4,5,6]])
print(prediction)

if prediction[0]==1:
    print("diabetic")
else:
    print("Non diabetic")