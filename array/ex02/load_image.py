from PIL import Image

def ft_load(path: str) -> list:
    im = Image.open(path)
    w, h = im.size
    band_len = len(im.getbands())
    pix = list(im.getdata())
    pix_val_flat = [list(x) for x in pix]
    print(f'The shape of image is: ({h}, {w}, {band_len})')
    return pix_val_flat

    

    