from PIL import Image

def ft_load(path: str) -> Image:
    im = Image.open(path)
    return im