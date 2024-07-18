import pyautogui
from PIL import Image, ImageFilter

def blur_screenshot_and_save():
    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to PIL image format
    screenshot_pil = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

    # Apply blur filter to the screenshot
    blurred_screenshot = screenshot_pil.filter(ImageFilter.BLUR)

    # Save the blurred screenshot
    blurred_screenshot.save('blurred_screenshot.png')

if __name__ == "__main__":
    # Call the function to take a screenshot, blur it, and save it
    blur_screenshot_and_save()


# import pyautogui
# from PIL import Image, ImageFilter

# def blur_screenshot_and_save(radius=2):
#     # Capture the screenshot
#     screenshot = pyautogui.screenshot()

#     # Convert the screenshot to PIL image format
#     screenshot_pil = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

#     # Apply blur filter to the screenshot with the specified radius
#     blurred_screenshot = screenshot_pil.filter(ImageFilter.GaussianBlur(radius))

#     # Save the blurred screenshot
#     blurred_screenshot.save('blurred_screenshot.png')

# if __name__ == "__main__":
#     # Adjust the blur radius here (higher values mean more blurriness)
#     blur_radius = 5

#     # Call the function to take a screenshot, blur it, and save it
#     blur_screenshot_and_save(blur_radius)
