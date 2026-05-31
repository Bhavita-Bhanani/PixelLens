import hashlib
from collections import Counter


def get_image_hash(image_bytes):

    return hashlib.sha256(
        image_bytes
    ).hexdigest()


def get_dominant_colors(image):

    img = image.resize(
        (100, 100)
    )

    pixels = list(
        img.getdata()
    )

    colors = Counter(
        pixels
    )

    return colors.most_common(5)