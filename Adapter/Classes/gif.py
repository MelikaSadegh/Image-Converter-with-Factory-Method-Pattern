from .image import Image 

class GIF(Image):
    def __init__(self, format, width, height, pixels):
        super().__init__(format, width, height, pixels)

def convert(self):
    return "You're Image converted to GIF format!"