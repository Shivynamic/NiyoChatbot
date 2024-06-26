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
conversationarray = [{"role": "system", "content": "You are an assistant who only answers questions related to Niyo-FAQs. You dont respond to anything besides Niyo FAQs"}]
print("How can I help you? - Type 'stop' when you are done.")

while True:
    # Ask the user to input question to the bot
    inputquestion = input("Question: ")

    # If no question, then type stop
    if inputquestion.lower() == 'stop': break

    # Before sending the inputted question to the api for answer, we will append it with the instruction so the bot knows what persona to use while answering the question.
    conversationarray.append({"role": "system","content": inputquestion})

    # Request fine tuned model for chat completion or a response
    response = client.chat.completions.create(
        model=os.getenv('TRAINED_MODEL_ID'),
        messages=conversationarray,
        temperature=0
    )

    # Access the response from the api to display it
    assistant_response = response.choices[0].message.content

    # Append the response back to the main array
    conversationarray.append({"role": "assistant", "content": assistant_response})

    # Print the response
    print(f"Assistant: {assistant_response}")