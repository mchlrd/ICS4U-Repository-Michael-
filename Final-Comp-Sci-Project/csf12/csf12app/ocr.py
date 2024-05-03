from PIL import Image
from pytesseract import pytesseract
import enum


class OS(enum.Enum):
    Windows = 1


class Language(enum.Enum):
    ENG = 'eng'
    FRC = 'fr'
    ITA = 'ita'
    RUS = 'rus'


class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path

    def extract_text(self, image_file, lang: Language):
        try:
            img = Image.open(image_file)
        except FileNotFoundError:
            print("Error: Image file not found.")
            return ""

        if lang not in Language:
            print("Error: Unsupported language.")
            return ""

        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text
