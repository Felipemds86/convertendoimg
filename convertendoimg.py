from email.mime import image
from PIL import Image

image_file = Image.open(r".\colorida.png")

image.file = image_file.convert('L')

image_file.save(r".\preta-e-branca.png")