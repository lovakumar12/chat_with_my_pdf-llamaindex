
Here’s a neatly structured README.md file that you can use for your GitHub repository, covering all the necessary details from the code and functionality:

markdown
Copy code
# PDF Query Interface with Image Display

This is a Streamlit-based web application that allows users to upload a PDF, ask questions about its content, and view related images extracted from the PDF. The app provides an interactive interface to explore PDF documents and visualize associated images based on the query results.

## Features

- **PDF Upload**: Users can upload a PDF file.
- **Query Interface**: Ask questions related to the content of the PDF.
- **Image Display**: View images related to the answer found in the PDF.
- **Question History**: Track all asked questions and answers with their corresponding images.
- **Image Extraction**: Automatically extracts images from the PDF and associates them with relevant content.

## File Structure

The file structure of the project is as follows:

├── data/ # Directory to store uploaded PDFs ├── output/ # Directory for storing extracted images ├── src/ # Source code for utilities │ ├── pdf_utils.py # Functions for PDF image extraction │ ├── query.py # Functions for creating index and querying the PDF │ └── st_diplay_img.py # Logic for displaying images in the app ├── streamlit.py # Main Streamlit app file ├── requirements.txt # List of required Python dependencies └── README.md # This file

bash
Copy code

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Dependencies for PDF extraction and image handling (e.g., `PyMuPDF`, `Pillow`, `llama_index`)

### Install Dependencies

To get started, clone the repository and install the required libraries:

```bash
# Clone the repository
git clone https://github.com/your-username/pdf-query-interface.git
cd pdf-query-interface

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required dependencies
pip install -r requirements.txt
If you don’t have a requirements.txt, you can manually install the dependencies:

bash
Copy code
pip install streamlit PyMuPDF Pillow llama_index
Dependencies
streamlit: For building the web app.
PyMuPDF: To extract images from PDFs.
Pillow: For handling image processing.
llama_index: To create an index for querying the PDF content.
Running the App
Once all dependencies are installed, you can run the Streamlit app with the following command:

bash
Copy code
streamlit run streamlit.py
How to Use the App
Upload a PDF: Click on the "Upload a PDF file" button and select a PDF from your local machine.
Ask a Question: After uploading the PDF, enter your question in the text input field.
Get Answers: Upon submitting the question, the app will display the answer and any relevant images from the PDF.
View History: Below the query input, you'll see a history of all asked questions, their answers, and the images associated with them.
Example Interaction
Question: "What is KNN? Explain in two lines."
Answer: "KNN (K-Nearest Neighbors) is a simple, instance-based machine learning algorithm that classifies data points based on the majority class of their nearest neighbors."
Images: If there are relevant images in the PDF, they will be displayed below the answer.
Troubleshooting
Common Issues
PDF Not Found: If the PDF isn’t being processed, ensure the file is uploaded correctly and is not corrupted.
Images Not Displaying: If no images are displayed, check that the page_label metadata is being correctly referenced, and images have been successfully extracted.
No Answer Found: If no answer is returned, make sure the question is clear and the PDF contains sufficient content for query matching.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Streamlit for providing the framework to build the web app.
PyMuPDF for handling PDF extraction.
Pillow for image manipulation.
llama_index for the querying engine.
markdown
Copy code

### Key Sections Included:
1. **Project Overview**: Describes the main functionality of the app.
2. **Features**: Lists the core features provided by the app.
3. **File Structure**: Outlines the directory structure for the code.
4. **Installation**: Provides instructions on how to install dependencies and set up the app.
5. **Running the App**: Explains how to run the Streamlit app.
6. **Usage**: Guides the user on how to interact with the app.
7. **Troubleshooting**: Covers common issues and possible solutions.
8. **License and Acknowledgements**: Details about the project's license and contributors.





