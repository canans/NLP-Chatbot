from flask import Flask,url_for,request,render_template,jsonify,send_file

from chat import chatbot

app=Flask(__name__)

@app.route("/chatbot")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

app.run()