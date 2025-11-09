import cv2
import numpy as np
import graph

if __name__ == "__main__":
    # Load an image from file
    image = cv2.imread("../public_dataset/testdata.png")

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range for a specific hue (e.g., red color)
    lower_hue = 150
    upper_hue = 180

    # Create a mask using the defined hue range
    mask = cv2.inRange(hsv_image, (lower_hue, 100, 0), (upper_hue, 255, 255))

    # Apply morphological operations to clean up the mask
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_DILATE, cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    )

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the original and resulting images
    graph.plot_result(
        image, mask, result, title1="Original", title2="Mask", title3="Result"
    )
