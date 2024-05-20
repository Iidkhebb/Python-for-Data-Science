from PIL import Image
import numpy as np


def ft_load(path: str) -> Image:
    im = Image.open(path)
    array = np.array(im)
    print(f"The shape of image is: ({array.shape})")
    print(array)
    return array
