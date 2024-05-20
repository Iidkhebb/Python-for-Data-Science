import numpy as np
import matplotlib.pyplot as plt

def display_image(image_array):
    # Display the image
    plt.imshow(image_array)
    plt.axis('off')  # Turn off axis
    plt.show()

def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted_image = np.max(array) - array
    display_image(inverted_image)
    return inverted_image

def ft_red(array) -> np.ndarray:
    # Keep only the red channel, setting green and blue channels to 0
    red_only = np.zeros_like(array)
    red_only[:, :, 0] = array[:, :, 0]
    display_image(red_only)
    return red_only

def ft_green(array) -> np.ndarray:
    green_channel = array[:, :, 1]
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    display_image(array)
    return array

def ft_blue(array) -> np.ndarray:
    red_green_zeroed = array.copy()
    red_green_zeroed[:, :, :2] = 0  # Zero out red and green channels
    display_image(red_green_zeroed)
    return red_green_zeroed

def ft_grey(array) -> np.ndarray:
    # Calculate luminance using weighted sum
    grey = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    # Assign grey values to all channels
    grey_image = np.zeros_like(array)
    grey_image[..., 0] = grey
    grey_image[..., 1] = grey
    grey_image[..., 2] = grey
    display_image(grey_image)
    return grey_image