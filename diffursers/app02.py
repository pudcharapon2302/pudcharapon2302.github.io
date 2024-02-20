import diffursers
from PTL import Image, ImageDraw, ImageFont

def text_to_image(text, diffuser_model):
    diffuser = diffuser.load_diffuser(diffuser_model)
    image_data = diffuser.generate(text)
    image = Image.fromarray(image_data)
    image.show()
    
if __name__ == "__main__":
    input_text = "Hello, World!!"
    diffuser_model = "example_diffuser_model"
    text_to_image(input_text, diffuser_model)