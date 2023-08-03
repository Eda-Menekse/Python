from PIL import Image
import pytesseract as pt

def image_to_text(image_path):
    image = Image.open(image_path)
    custom_config = r'--oem 3 --psm 6'
    text = pt.image_to_string(image, config=custom_config, lang='eng+tur')
    return text

image_path = "yazi.jpeg"
text = image_to_text(image_path)

print(text)