from flask import Flask, render_template, request, jsonify
from os_bot import OSBot
import os

app = Flask(__name__)

# Initialize the bot locally
# We do this outside the route so it loads once at startup
try:
    print("Initializing OS Bot...")
    bot = OSBot()
    print("OS Bot initialized successfully.")
except Exception as e:
    print(f"Error initializing bot: {e}")
    bot = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not bot:
        return jsonify({'response': "Error: Bot failed to initialize. Please check server logs."}), 500
    
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': "Please enter a message."}), 400
    
    try:
        response = bot.chat(user_message)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error during chat: {e}")
        return jsonify({'response': "Sorry, I encountered an internal error."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
