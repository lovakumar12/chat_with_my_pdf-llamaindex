
import streamlit as st
import re

def display_images_for_page(response, image_info_list):
    """Displays images for the page related to the response metadata."""
    if hasattr(response, 'metadata'):
        document_info = str(response.metadata)
        
        # Extract the page label from the response metadata
        match = re.search(r"'page_label': '([^']*)'", document_info)
        
        if match:
            page_label = match.group(1)
            st.write(f"Searching for images on Page {page_label}...")

            # Find images matching the page label
            matching_images = [
                img_info['image_path']
                for img_info in image_info_list
                if str(img_info['page_number']) == page_label
            ]

            if matching_images:
                #st.write(f"Images for Page {page_label}:")
                for img_path in matching_images:
                    # Display each matching image
                    #st.image(img_path, caption=f"Image from Page {page_label}") #, use_column_width=True
                    return matching_images  # Return the paths of displayed images
            else:
                st.write(f"No images found for Page {page_label}.")
                return []
        else:
            st.write("No 'page_label' found in the response metadata.")
            return []
    else:
        st.write("No metadata available in the response.")
        return []
