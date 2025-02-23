import os

from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv()  # Loads the .env file
#api_key = os.getenv('Hugging_face_API_KEY')
# api_key=os.getenv("deep_seek_api")
# login(api_key)
os.environ["GROQ_API_KEY"] = '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'

# Set the REPLICATE API Token
#os.environ["REPLICATE_API_TOKEN"] = api_key



# LLM and Tokenizer Settings
# LLAMA2_7B_CHAT_MODEL = "meta-llama/Llama-2-7b-chat-hf"
# LLAMA2_7B_CHAT_TOKENIZER = "meta-llama/Llama-2-7b-chat-hf"
HUGGINGFACE_EMBED_MODEL = "BAAI/bge-small-en-v1.5"
