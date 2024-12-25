# chat_with_my_pdf-lamaindex

# PDF Query Interface with Image Display

This is a Streamlit-based application that allows users to upload a PDF, ask questions about its content, and view related images extracted from the PDF. The app provides an easy way to interact with the PDF's content and see visual aids that are associated with the answers.

## Features
- Upload a PDF file.
- Ask questions about the content of the uploaded PDF.
- View answers to your questions along with images extracted from the PDF.
- View a history of all questions asked along with their respective answers and related images.

## Requirements

Before running the app, ensure you have the following dependencies installed:

- Python 3.7 or higher
- Streamlit
- Dependencies for PDF extraction and image handling (e.g., `PyMuPDF`, `Pillow`, `llama_index`, etc.)

### Install Dependencies

You can create a virtual environment and install the required libraries:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the dependencies
pip install -r requirements.txt
If you don't have a requirements.txt file, you can manually install the required dependencies with:

# bash
Copy code
pip install streamlit PyMuPDF Pillow llama_index
Note: You might need additional libraries based on the utilities used for PDF extraction and image processing.

# File Structure
The file structure for the project looks like this:

graphql
Copy code
├── data/                 # Directory to store uploaded PDFs
├── output/               # Directory for storing extracted images
├── src/                  # Source code for utilities
│   ├── pdf_utils.py      # Contains functions for PDF image extraction
│   ├── query.py          # Contains functions for creating index and querying
│   ├── config.py 
│   └── st_diplay_img.py  # Contains the image display logic
├── streamlit.py          # Main Streamlit app file
├── requirements.txt      # List of required Python dependencies
└── README.md             # This file
Running the App
Once all dependencies are installed, you can run the app with the following command:

bash
# Copy code
streamlit run streamlit.py

How to Use the App
Upload a PDF: Click on the "Upload a PDF file" button and select a PDF from your local machine.
Ask a Question: After uploading the PDF, enter a question about its content in the provided text input field.
Get Answers and Images: After submitting the question, the app will display the answer along with any relevant images extracted from the PDF.
History: The app keeps a history of all questions and answers with related images, which will be displayed below the query input.
Example Interaction
Question: "What is KNN? Explain in two lines."
Answer: "KNN (K-Nearest Neighbors) is a simple, instance-based machine learning algorithm that classifies data points based on the majority class of their nearest neighbors."
Images: The app will display any images that are relevant to the page(s) where the answer was found.

# Troubleshooting
# Common Issues:
PDF Not Found: If no PDF is processed, ensure the file is uploaded correctly and is not corrupted.
Images Not Displaying: If no images are displayed, check if images were successfully extracted from the PDF and ensure that the page_label metadata is correctly being referenced.
# License
This project is licensed under the MIT License - see the LICENSE file for details.
