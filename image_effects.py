from PIL import Image, ImageOps, ImageFilter
import cv2
import numpy as np


def edge_detection(image):

    img = cv2.cvtColor(
        np.array(image),
        cv2.COLOR_RGB2BGR
    )

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    return cv2.Canny(
        gray,
        100,
        200
    )


def sketch_effect(image):

    img = cv2.cvtColor(
        np.array(image),
        cv2.COLOR_RGB2BGR
    )

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    invert = 255 - gray

    blur = cv2.GaussianBlur(
        invert,
        (21, 21),
        0
    )

    inverted_blur = 255 - blur

    return cv2.divide(
        gray,
        inverted_blur,
        scale=256
    )


def pixel_art(image):

    small = image.resize(
        (
            max(1, image.width // 16),
            max(1, image.height // 16)
        )
    )

    return small.resize(
        image.size,
        Image.NEAREST
    )


def grayscale(image):
    return image.convert("L")


def negative(image):

    return ImageOps.invert(
        image.convert("RGB")
    )


def blur_image(image):

    return image.filter(
        ImageFilter.BLUR
    )


def sharpen_image(image):

    return image.filter(
        ImageFilter.SHARPEN
    )


def cartoon_effect(image):

    img = cv2.cvtColor(
        np.array(image),
        cv2.COLOR_RGB2BGR
    )

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.medianBlur(
        gray,
        5
    )

    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    color = cv2.bilateralFilter(
        img,
        9,
        250,
        250
    )

    cartoon = cv2.bitwise_and(
        color,
        color,
        mask=edges
    )

    return cv2.cvtColor(
        cartoon,
        cv2.COLOR_BGR2RGB
    )