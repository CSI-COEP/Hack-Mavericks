# Finds the accuracy of the chatbot using Random Forest model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = data.drop(['Class'],axis=1)
y = data['Class']

# Random Forest Algorithm
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
model=rf.fit(X_train,y_train)
prediction=model.predict(X_test)
rf_accuracy = accuracy_score(y_test,prediction)
print("The accuracy of our model using RF classifier = {} %".format(rf_accuracy*100))
