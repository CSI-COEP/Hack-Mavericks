# Code for saving the machine learning model of the chatbot which will then be connected with the GUI.
import joblib
joblib.dump(rf,'chatbot_model')
model = joblib.load('chatbot_model')
model.predict(new_data)
