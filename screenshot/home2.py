import pyautogui
from PIL import Image, ImageEnhance

def tv_signal_effect_and_save():
    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to PIL image format
    screenshot_pil = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

    # Convert the image to grayscale
    grayscale_image = screenshot_pil.convert('L')

    # Enhance the contrast to increase the intensity of the dithering effect
    enhancer = ImageEnhance.Contrast(grayscale_image)
    grayscale_image = enhancer.enhance(2.0)  # Increase contrast by a factor of 2

    # Convert the grayscale image to black and white using manual thresholding
    threshold = 200  # Adjust the threshold to control the dithering effect
    bw_image = grayscale_image.point(lambda x: 0 if x < threshold else 255, '1')

    # Resize the image to increase the size of the dithered pixels
    bw_image = bw_image.resize((bw_image.width * 2, bw_image.height * 2), Image.NEAREST)

    # Save the black and white image
    bw_image.save('tv_signal_effect.png')

if __name__ == "__main__":
    # Call the function to take a screenshot, apply TV signal effect, and save it
    tv_signal_effect_and_save()
