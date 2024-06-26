from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
# Load your API key from an environment variable
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

# Upload the dataset to openai for fine-tuning
client.files.create(
  file=open("./data/FAQ_converted.jsonl", "rb"),
  purpose="fine-tune"
)