import tkinter as tk
from tkinter import PhotoImage

def display_image(image_path):
    image = PhotoImage(file=image_path)
    image_label.config(image=image)
    image_label.image = image  # Keep a reference to the image to prevent it from being garbage collected

# Create the main application window
root = tk.Tk()
root.title("Image Viewer")

# Load and store three different images
image1 = "image1.gif"  # Replace with the actual path to your image file
image2 = "image2.gif"  # Replace with the actual path to your image file
image3 = "image3.gif"  # Replace with the actual path to your image file

# Create buttons with associated callback functions
button1 = tk.Button(root, text="Image 1", command=lambda: display_image(image1))
button2 = tk.Button(root, text="Image 2", command=lambda: display_image(image2))
button3 = tk.Button(root, text="Image 3", command=lambda: display_image(image3))

# Create a label to display the images
image_label = tk.Label(root)
image_label.pack()

# Place the buttons in the window
button1.pack()
button2.pack()
button3.pack()

# Start the tkinter main loop
root.mainloop()
