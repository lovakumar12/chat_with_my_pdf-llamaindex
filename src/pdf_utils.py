import fitz
import os

def extract_images_formatted(pdf_file_path, output_dir):
    """Extracts images from a PDF file, organizes them with consistent paths and page numbers,
       and returns a list of dictionaries in the desired format."""
    doc = fitz.open(pdf_file_path)
    images_formatted = []
    image_index = 0  # Global image index for consistent filenames

    for i in range(len(doc)):
        page = doc[i]
        images = page.get_images()

        for img in images:
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:  # Ensure RGB color space
                pix = fitz.Pixmap(fitz.csRGB, pix)

            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Save image with consistent filename format
            filename = f"drawing-{str(i).zfill(3)}-{str(image_index).zfill(2)}.jpg"
            image_path = os.path.join(output_dir, filename)
            pix.save(image_path)

            # Create dictionary entry with image path and page number
            image_data = {"image_path": image_path, "page_number": i+1}
            images_formatted.append(image_data)
            image_index += 1  # Increment image index for the next image

    return images_formatted
