from flask import Flask, render_template, request
import medicalchatbot 
import sys
app = Flask(__name__)

app.static_folder = 'static'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot')
def chatbot():
    # print(medicalchatbot.get_bot_response('hello'), file=sys.stderr)
    return render_template('chatbot.html')    

@app.route("/ask")
def ask_bot():
    userText = request.args.get('userInput')
    return medicalchatbot.bot_response(userText)

@app.route('/skin')
def skin():
    return render_template('skin.html')

if __name__ == "__main__":
    app.run()  