import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

def process_frame(frame):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for blue color
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    # Create a mask for blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw red rectangles around blue objects
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return frame

def main():
    while True:
        # Capture the computer monitor screen
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)

        # Convert the image from RGB to BGR
        frame = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Process the frame
        processed_frame = process_frame(frame)

        # Display the processed frame
        cv2.imshow('Processed Frame', processed_frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
