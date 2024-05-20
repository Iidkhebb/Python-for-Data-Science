from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom(path: str):
    im = ft_load(path)
    arr = np.array(im)
    height, width, channels = arr.shape

    xoff = height - 665 
    yoff = width // 2 - 55

    # Perform the slicing operation to crop the image
    cropped_image = arr[xoff:xoff+400, yoff:yoff+400, 0:1]  # Slicing to get the first channel only

    print("The shape of image is:", arr.shape)
    print(arr)
    crop_height, crop_width, crop_ch = cropped_image.shape
    print("New shape after slicing:", cropped_image.shape, f" or ({crop_height}, {crop_width})")
    print(cropped_image)
    plt.imshow(cropped_image, cmap='gray')  # Displaying as grayscale
    plt.axis('on')  # Turn off axis
    plt.show()


def main():
    try:
        zoom('animal.jpg')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
