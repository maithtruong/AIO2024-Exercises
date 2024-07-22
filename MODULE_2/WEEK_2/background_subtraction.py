import numpy as np
import cv2
import matplotlib.pyplot as plt

def compute_difference(bg_img, input_img):
    difference_single_channel = cv2.absdiff(bg_img, input_img)
    return difference_single_channel

def compute_binary_mask(difference_single_channel):
    gray = cv2.cvtColor(difference_single_channel, cv2.COLOR_BGR2GRAY)
    _, binary_mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    return binary_mask

def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask[:, :, None] == 255, ob_image, bg2_image)
    return output

def main():
    bg1_image = cv2.imread('MODULE_2/WEEK_2/images/GreenBackground.png', 1)
    bg1_image = cv2.resize(bg1_image, (678, 381))

    ob_image = cv2.imread('MODULE_2/WEEK_2/images/Object.png', 1)
    ob_image = cv2.resize(ob_image, (678, 381))

    bg2_image = cv2.imread('MODULE_2/WEEK_2/images/NewBackground.jpg', 1)
    bg2_image = cv2.resize(bg2_image, (678, 381))

    difference_single_channel = compute_difference(bg1_image, ob_image)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.title('Difference Image')
    plt.imshow(cv2.cvtColor(difference_single_channel, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    binary_mask = compute_binary_mask(difference_single_channel)

    plt.subplot(1, 3, 2)
    plt.title('Binary Mask')
    plt.imshow(binary_mask, cmap='gray')
    plt.axis('off')

    output = replace_background(bg1_image, bg2_image, ob_image)

    plt.subplot(1, 3, 3)
    plt.title('Output Image')
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()