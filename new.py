from flask import Flask, request, jsonify
from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load your API key from an environment variable
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

@app.route('/ask', methods=['POST'])
def ask_question():
    # Get the question from the request data
    inputquestion = request.json.get('question')
    if inputquestion.lower() == 'stop':
        return jsonify({'status': 'Thank you! Hope we were able to resolve your querry'}), 200


    # If no question is provided, return an error response
    if not inputquestion:
        return jsonify({'error': 'No question provided'}), 400

    # Create conversation array with initial instruction
    conversationarray = [{"role": "system", "content": "You are an Niyo-FAQ assistant who only answers related to questions of NIYO."}]

    # Append user question to the conversation array
    conversationarray.append({"role": "system","content": inputquestion})

    # Request gpt-3.5-turbo for chat completion or a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversationarray
    )

    # Get assistant's response
    assistant_response = response.choices[0].message.content

    # Append the response back to the main array
    conversationarray.append({"role": "assistant", "content": assistant_response})

    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
