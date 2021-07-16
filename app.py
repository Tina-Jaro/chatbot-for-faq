#importing libraries for implementation 
from flask import Flask, render_template, request
from bot import chatbot #importing the chatbot

#creates the flask app
app = Flask(__name__, static_url_path='/static')
app._static_folder = 'static'

#reads the html file 
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bot')
def bot():
    return render_template("bot.html")

#gets response
@app.route("/get")
def get_response():
    text = request.args.get("msg")
    return str(chatbot.get_response(text))

if __name__ == '__main__':
    app.run()
