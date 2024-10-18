from rembg import remove
from PIL import Image

# Paths to input and output images
input_path = 'img.jpg'
output_path = 'output.png'  # Use PNG format to support transparency

# Open the input image
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the output image as PNG
output_image.save(output_path)
