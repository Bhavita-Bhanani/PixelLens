import streamlit as st
from PIL import Image
import io
import numpy as np


def download_image(
    img,
    filename
):

    buffer = io.BytesIO()

    if isinstance(
        img,
        np.ndarray
    ):
        img = Image.fromarray(img)

    img.save(
        buffer,
        format="PNG"
    )

    st.download_button(
        f"Download {filename}",
        buffer.getvalue(),
        f"{filename}.png",
        "image/png"
    )