# Finds the accuracy of the chatbot using Random Forest model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = data.drop(['Class'],axis=1)
y = data['Class']
# Splitting the dataset into a training set of 80% and tesing set of 20%.
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.20,random_state = 41)

# Random Forest Algorithm
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
model=rf.fit(X_train,y_train)
prediction=model.predict(X_test)
rf_accuracy = accuracy_score(y_test,prediction)
print("The accuracy of our model using RF classifier = {} %".format(rf_accuracy*100))
