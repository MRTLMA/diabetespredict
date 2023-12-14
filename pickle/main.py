import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import joblib

df=pd.read_csv("/Users/abuadam/Desktop/new/diabetes.csv")

print(df.head())

array=df.values

x=array[:,0:8]
y=array[:,8]

test_size=0.2

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=test_size,random_state=101)

model=LogisticRegression()
model.fit(X_train,y_train)

train_result=model.score(X_train,y_train)
test_result=model.score(X_test,y_test)
print("Training Accuracy",train_result)
print("Testing Accuracy",test_result)

pickle.dump(model,open("diabetic.pkl",'wb'))
joblib.dump(model,"diabetic_joblib.pkl")





