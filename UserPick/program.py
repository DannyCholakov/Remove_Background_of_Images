from rembg import remove
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Function to select an image
def select_image():
    # Hide the Tkinter root window
    root = Tk()
    root.withdraw()  # Prevents a full GUI window from appearing
    root.update()    # Ensures the dialog appears immediately

    # Open a file dialog to select an image
    file_path = askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    root.destroy()  # Close the Tkinter root window
    return file_path

# Get the user's desktop path
desktop_path = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')

# Allow the user to select an image file
input_path = select_image()
if input_path:
    try:
        # Open the selected image
        input_image = Image.open(input_path)

        # Remove the background
        output_image = remove(input_image)

        # Set the output path to the desktop
        output_path = os.path.join(desktop_path, 'output.png')

        # Save the output image to the desktop
        output_image.save(output_path)

        print(f"Image saved successfully on your desktop: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No image selected.")
