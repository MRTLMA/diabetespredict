import pickle

model=pickle.load(open("diabetic.pkl",'+rb'))

prediction=model.predict([[2,3,4,5,66,7,8,9]])
print(prediction)

if prediction[0]==1:
    print("diabetic")

else:
    print("Non diabetic")