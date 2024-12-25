# PDF Query Interface with Image Display

This is a Streamlit-based web application that allows users to upload a PDF, ask questions about its content, and view related images extracted from the PDF. The app provides an interactive interface for querying PDF documents and visualizing associated images based on the query results.

## Features

- **PDF Upload**: Allows users to upload PDF files for processing.
- **Query Interface**: Users can ask questions about the content of the uploaded PDF.
- **Image Display**: Displays images extracted from the PDF that are related to the query results.
- **Question History**: Tracks the history of questions and their corresponding answers with images.
- **Image Extraction**: Automatically extracts and associates images with relevant content in the PDF.

## Project Structure

├── data/                 # Directory for storing input data files (e.g., PDFs).
├── output/               # Directory for storing output files or processed data.
├── src/                  # Source code files.
│   ├── pdf_utils.py      # Utility functions for handling PDFs.
│   ├── config.py         # Configuration file for API keys and settings.
│   ├── query.py          # Logic for querying and processing data.
│   └── st_display_img.py # Streamlit utility functions for displaying images.
├── streamlit.py          # Main Streamlit app file.
├── testing.ipynb         # Jupyter Notebook for testing and prototyping.
├── app.py                # Application entry point for the overall project.
├── requirements.txt      # Python dependencies required for the project.
└── README.md             # Documentation and project overview.




## Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.7 or higher**
- **Streamlit** for the web app
- **PyMuPDF** for PDF extraction
- **Pillow** for image handling
- **llama_index** for indexing and querying the PDF

### Steps to Install

### Clone the Repository

   ```bash
   git clone https://github.com/your-username/pdf-query-interface.git
   cd pdf-query-interface
Set up a Python virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

### Install Dependencies

```bash
pip install -r requirements.txt
```



### Run the Application

To launch the Streamlit app locally, use the following command:

```bash
streamlit run streamlit.py
```

The app will open in your browser at `http://localhost:8501`.

---
