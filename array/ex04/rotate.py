import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def rotate(path: str):
    im = ft_load(path)
    arr = np.array(im)
    height, width, channels = arr.shape

    xoff = height - 665
    yoff = width // 2 - 55

    # Perform the slicing operation to crop the image
    cropped_image = arr[
        xoff: xoff + 400, yoff: yoff + 400, 0:1
    ]  # Slicing to get the first channel only

    transpose_image = np.transpose(
        cropped_image, axes=(1, 0, 2)
    )  # Transpose height and width axes
    crop_height, crop_width, crop_ch = transpose_image.shape
    print(
        f"The shape of image is: {cropped_image.shape}\
            or ({crop_height}, {crop_width})"
    )
    print(cropped_image)
    print(
        "New shape after transpose: ",
        f"({crop_height}, {crop_width})",
    )
    print(transpose_image)
    plt.imshow(transpose_image, cmap="gray")  # Displaying as grayscale
    plt.axis("on")  # Turn off axis
    plt.show()


def main():
    try:
        rotate("animal.jpg")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
