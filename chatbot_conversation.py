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
conversationarray = [{"role": "system", "content": "You are an Niyo-FAQ assistant who only uses ft:gpt-3.5-turbo-1106:niyo::9HofkSIH data to answer the questions."}]

print("How can I help you? - Type 'stop' when you are done.")

while True:
    # Ask the user to input question to the bot
    inputquestion = input("Question: ")

    # If no question, then type stop
    if inputquestion.lower() == 'stop': break

    # Before sending the inputted question to the api for answer, we will append it with the instruction so the bot knows what persona to use while answering the question.
    conversationarray.append({"role": "system","content": inputquestion})

    # Request gpt-3.5-turbo for chat completion or a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversationarray
    )

    # Access the response from the api to display it
    assistant_response = response.choices[0].message.content

    # Append the response back to the main array
    conversationarray.append({"role": "assistant", "content": assistant_response})

    # Print the response
    print(f"Assistant: {assistant_response}")