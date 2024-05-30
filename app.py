from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace <token> with your actual Worqhat API token
API_URL = "https://api.worqhat.com/api/ai/content/v2"
API_TOKEN = "sk-4553c2378af54b33bf8986dfdae6092c"

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    payload = {
        "question": user_message,
        "preserve_history": True,
        "randomness": 0.5,
        "stream_data": False,
        "conversation_history": [],
        "training_data": "You are StuBot and will be helping students for counselling purpose after giving entrance exams based on their scores and preferences.And you were made for Value Add on course by Aditya Dhanwai, Shivam Bhagwat, Janardhan Chikale and Rushikesh under the guidance of Workhat Team.",
        "response_type": "text"
    }
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(API_URL, json=payload, headers=headers)
    response_json = response.json()
    
    print(response_json)
    # Extract the answer from the content field in the response
    bot_answer = response_json.get('content', 'I am not sure how to respond to that.')

    return jsonify({'answer': bot_answer})

if __name__ == '__main__':
    app.run(debug=True)
