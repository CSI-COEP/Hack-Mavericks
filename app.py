from flask import Flask, render_template
app = Flask(__name__)

# Code for accessing the HTML file
@app.route('/')
def home():
    return render_template("chatbot.html")

# Code for getting message from user 
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    bot_response = str(chatbot.get_response(user_text))
    return bot_response

if __name__ == "__main__":
    app.run()
