import os
import sys
from src.pdf_utils import extract_images_formatted
from src.query import create_index, display_images_for_page

def main():
    pdf_file = 'data\HighVoltag(36-42) (1) (2).pdf'
    output_dir = 'output'

    # Step 1: Extract images from the PDF
    images_by_page = extract_images_formatted(pdf_file, output_dir)

    # Step 2: Create the query index from the PDF
    index = create_index(pdf_file)

    # Step 3: Create the query engine
    query_engine = index.as_query_engine()

    # Step 4: Perform the query and display the response and images
    # response = query_engine.query("what is the operational voltage of abb switch gear cd type")
    # print(response)
    # display_images_for_page(response, images_by_page)
    while True:
        # Ask the user to input a question
        question = input("Please enter your question (or type 'exit' to quit): ")

        # Exit the loop if the user types 'exit'
        if question.lower() == 'exit':
            print("Exiting the program.")
            break

        # Query the engine with the user's question
        response = query_engine.query(question)

        # Print the response
        print("Response:", response)

        # Display images related to the response
        display_images_for_page(response, images_by_page)


if __name__ == "__main__":
    main()
