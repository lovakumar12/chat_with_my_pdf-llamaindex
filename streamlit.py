
import os
import streamlit as st
from src.pdf_utils import extract_images_formatted
from src.query import create_index
from src.st_diplay_img import display_images_for_page  # Import the updated function

def main():
    st.title("PDF Query Interface with Image Display")
    st.write("This app allows you to query information from a PDF and view related images.")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        pdf_file = os.path.join("data", uploaded_file.name)
        with open(pdf_file, "wb") as f:
            f.write(uploaded_file.getbuffer())

        output_dir = 'output'
        images_by_page = extract_images_formatted(pdf_file, output_dir)
        index = create_index(pdf_file)
        query_engine = index.as_query_engine()

        if "qa_history" not in st.session_state:
            st.session_state.qa_history = []

        question = st.text_input("Ask a question:", "")

        if st.button("Submit Query"):
            if question:
                response = query_engine.query(question)

                # Display images and get matching images for the response
                matching_images = display_images_for_page(response, images_by_page)

                st.session_state.qa_history.append({
                    "question": question,
                    "response": response,
                    "images": matching_images,
                })

        # Display history
        if st.session_state.qa_history:
            st.write("### Questions, Answers, and Images")
            for i, qa in enumerate(st.session_state.qa_history, 1):
                st.write(f"**Q{i}:** {qa['question']}")
                st.write(f"**A{i}:** {qa['response']}")
                st.write("#### Related Images:")
                if qa["images"]:
                    for img_path in qa["images"]:
                        st.image(img_path, caption=f"Image for Q{i}")#, use_column_width=True
                else:
                    st.write("No images found for this answer.")
                st.write("---")

if __name__ == "__main__":
    main()
