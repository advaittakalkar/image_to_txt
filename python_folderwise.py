from PIL import Image
import pytesseract
import os

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    """Convert image to text using OCR."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def create_text_file(text, output_path):
    """Create a text file from text."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def process_images(input_folder, output_folder):
    """Process all images in the input folder and save them as text files in the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            text = image_to_text(image_path)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            create_text_file(text, output_path)
            print(f"Processed {filename}")

# Define input and output folders
input_folder = r"C:\Users\advai\Desktop\HIG\Exam work\QP1167J"
output_folder = r"C:\Users\advai\Desktop\HIG"

# Process the images
process_images(input_folder, output_folder)