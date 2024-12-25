import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import display, Image
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.replicate import Replicate
from transformers import AutoTokenizer

import src.config as config

# from dotenv import load_dotenv
# import os

# load_dotenv()  # Loads the .env file
# api_key = os.getenv('API_KEY')


# Set up LLM and tokenizer
Settings.llm = Replicate(
    model=config.LLAMA2_7B_CHAT_MODEL,
    temperature=0.01,
    additional_kwargs={"top_p": 1, "max_new_tokens": 300},
)

Settings.tokenizer = AutoTokenizer.from_pretrained(config.LLAMA2_7B_CHAT_TOKENIZER)
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
