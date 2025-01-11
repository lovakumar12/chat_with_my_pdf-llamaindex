import os

from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file
api_key = os.getenv('API_KEY')

# Set the REPLICATE API Token
os.environ["REPLICATE_API_TOKEN"] = api_key



# LLM and Tokenizer Settings
LLAMA2_7B_CHAT_MODEL = "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e"
LLAMA2_7B_CHAT_TOKENIZER = "NousResearch/Llama-2-7b-chat-hf"
HUGGINGFACE_EMBED_MODEL = "BAAI/bge-small-en-v1.5"
