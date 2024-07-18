# app.py

import streamlit as st
from PIL import Image
from pynput.keyboard import Key, Listener
import pyautogui
import io
import base64
from cryptography.fernet import Fernet
from PIL import Image, ImageFilter

# Generate a random key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_image(image):
    # Convert PIL image to bytes
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='JPEG')  # Save as JPEG to avoid lossy compression
    img_bytes = img_byte_array.getvalue()

    # Encrypt the image bytes
    encrypted_img = cipher_suite.encrypt(img_bytes)

    # Encode the encrypted image bytes in base64 format
    encrypted_img_base64 = base64.b64encode(encrypted_img)

    return encrypted_img_base64

def blur_screenshot_and_save():
    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to PIL image format
    screenshot_pil = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

    # Apply blur filter to the screenshot
    blurred_screenshot = screenshot_pil.filter(ImageFilter.BLUR)

    # Encrypt the blurred screenshot
    encrypted_blurred_screenshot = encrypt_image(blurred_screenshot)

    # Save the encrypted blurred screenshot
    with open('encrypted_blurred_screenshot.jpeg', 'wb') as f:
        f.write(encrypted_blurred_screenshot)

def on_press(key):
    if key == Key.print_screen:
        blur_screenshot_and_save()

def on_release(key):
    pass

def main():

    st.markdown(
    """
    <style>
    body {
        background-image: url('D:\acmw\post_flask\doodle.jpg');
        background-size: cover;
        background-position: center;
        }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown('<div class="background"></div>', unsafe_allow_html=True)


    st.title("DivaGram📸")

    users = [
        {"name": "Samantha", "image": "Img1.jpg"},
        {"name": "Savithri", "image": "Img4.jpg"},
        {"name": "Roshni", "image": "Img2.jpeg"},
        {"name": "Mary", "image": "Img3.webp"}
    ]

    # Open images, resize, and display
    for user in users:
        st.markdown(f"## {user['name']}")
        image = Image.open(user['image'])
        # Resize image to desired dimensions
        resized_image = image.resize((400, 400))
        st.image(resized_image, use_column_width=False)

    # Start listening for key presses
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
