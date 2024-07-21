from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (600, 600), color='white')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw a red rectangle
draw.rectangle((100, 50, 300, 200), fill='red', outline='black')

# Draw a blue circle
draw.ellipse((50, 100, 150, 200), fill='blue', outline='black')

# Save the image (optional)
image.save('drawn_image.png')

# Show the image (optional, requires an image viewer)
image.show()

##Note: Pillow is a fork of the Python Imaging Library (PIL) and provides easy-to-use functions for opening, manipulating, and saving many different image file formats
