# Install packages if needed
# pip install openai
# pip install python-dotenv

from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
# Load your API key from an environment variable
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

# Create an instruction for our bot
conversation = [{"role": "system", "content": "You are an assistant who only answers questions related to Niyo-FAQs. You dont respond to anything besides Niyo FAQs"}]

# Ask the user to input question to the bot
print("How can I help you?")
inputquestion = input("Question: ")

# Before sending the inputted question to the api for answer, we will append it with the instruction so the bot knows what persona to use while answering the question.
conversation.append({"role": "system","content": inputquestion})

# Request gpt-3.5-turbo for chat completion or a response
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

# Access the response from the api to display it
assistant_response = response.choices[0].message.content

# Print the response
print(f"Assistant: {assistant_response}")