import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import display, Image
#from IPython.display import display, Image
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
#from llama_index.llms.replicate import Replicate
from transformers import AutoTokenizer
from huggingface_hub import HfApi
import os
from huggingface_hub import login

import src.config as config

from dotenv import load_dotenv

from llama_index.llms.groq import Groq

load_dotenv()  # Loads the .env file
#api_key = os.getenv('Hugging_face_API_KEY')

# api_key=os.getenv("deep_seek_api")

# login(api_key)

import os

os.environ["GROQ_API_KEY"] = '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'
#from groq import Groq

# setup prompts - specific to StableLM
from llama_index.core import PromptTemplate

system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
- StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
- StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
- StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
- StableLM will refuse to participate in anything that could harm a human.
"""

# This will wrap the default prompts that are internal to llama-index
query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")


# llm = HuggingFaceLLM(
#     context_window=4096,
#     max_new_tokens=256,
#     generate_kwargs={"temperature": 0.7, "do_sample": False},
#     system_prompt=system_prompt,
#     query_wrapper_prompt=query_wrapper_prompt,
#     tokenizer_name="meta-llama/Llama-2-7b-chat-hf",
#     model_name="meta-llama/Llama-2-7b-chat-hf",
#     device_map="auto",
#     #stopping_ids=[50278, 50279, 50277, 1, 0],
#     tokenizer_kwargs={"max_length": 4096},
#     # uncomment this if using CUDA to reduce memory usage
#     # model_kwargs={"torch_dtype": torch.float16}
# )

llm = Groq(model="llama3-8b-8192")

Settings.llm = llm

# # Set up LLM and tokenizer
# Settings.llm = HuggingFaceLLM(
#     model=config.LLAMA2_7B_CHAT_MODEL,
#     generate_kwargs={"temperature": 0.7, "do_sample": False}
    
#     context_window=4096,
#     max_new_tokens=256,
# )

#Settings.tokenizer = AutoTokenizer.from_pretrained(config.LLAMA2_7B_CHAT_TOKENIZER)
Settings.embed_model = HuggingFaceEmbedding(model_name=config.HUGGINGFACE_EMBED_MODEL)

# Function to load documents and create an index
def create_index(pdf_file_path):
    documents = SimpleDirectoryReader(input_files=[pdf_file_path]).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index

# Function to display images from the extracted list
def display_images_for_page(response, image_info_list):
    if hasattr(response, 'metadata'):
        document_info = str(response.metadata)
        find = re.findall(r"'page_label': '([^']*)'", document_info)

        if find:
            page_label = find[0]
            matching_images = [img_info['image_path'] for img_info in image_info_list if str(img_info['page_number']) == page_label]

            if matching_images:
                print(f"Images for Page {page_label}:")
                for img_path in matching_images:
                    img = mpimg.imread(img_path)
                    plt.imshow(img)
                    plt.axis('off')  # Optional: Hide axis labels
                    plt.show()
            else:
                print(f"No matching images found for Page {page_label}.")
        else:
            print("No 'page_label' found in the response.")
    else:
        print("No metadata found in the response.")
