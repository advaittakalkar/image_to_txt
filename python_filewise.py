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


def process_image(input_image, output_folder):
    """Process a single image and save it as a text file in the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    filename = os.path.basename(input_image)
    text = image_to_text(input_image)
    output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
    create_text_file(text, output_path)
    print(f"Processed {filename}")


# Define input image and output folder
input_image = r"C:\Users\advai\Desktop\HIG\Exam work\QP1167J\QP1167J (1).jpg"
output_folder = r"C:\Users\advai\Desktop\HIG"

# Process the image
process_image(input_image, output_folder)
