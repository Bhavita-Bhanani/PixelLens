import streamlit as st
from PIL import Image
from datetime import datetime

from image_effects import (
    edge_detection,
    sketch_effect,
    pixel_art,
    cartoon_effect,
    grayscale,
    negative,
    blur_image,
    sharpen_image
)

from metadata import (
    get_image_hash,
    get_dominant_colors
)

from utils import (
    download_image
)

st.set_page_config(
    page_title="PixelLens",
    page_icon="📷",
    layout="wide"
)

# -------------------------
# Styling
# -------------------------

st.markdown("""
<style>

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.main-title {
    font-size: 3rem;
    font-weight: 700;
    color: #6D5DF6;
}

.subtitle {
    color: #64748B;
    margin-bottom: 20px;
}

.info-box {
    background: #F8FAFC;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown(
    '<div class="main-title">PixelLens</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze • Transform • Download</div>',
    unsafe_allow_html=True
)

st.divider()

# -------------------------
# Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp"]
)

# -------------------------
# Processing
# -------------------------

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    image_bytes = uploaded_file.getvalue()

    image_hash = get_image_hash(
        image_bytes
    )

    width, height = image.size

    file_size = round(
        len(image_bytes) / 1024,
        2
    )

    aspect_ratio = round(
        width / height,
        2
    )

    col1, col2 = st.columns(
        [2, 1]
    )

    # ---------------------
    # Original Image
    # ---------------------

    with col1:

        st.subheader(
            "Original Image"
        )

        st.image(
            image,
            use_container_width=True
        )

    # ---------------------
    # Metadata
    # ---------------------

    with col2:

        st.subheader(
            "Image Details"
        )

        st.markdown(
            f"""
            **Width:** {width}px

            **Height:** {height}px

            **Aspect Ratio:** {aspect_ratio}

            **File Size:** {file_size} KB

            **Format:** {image.format}

            **Mode:** {image.mode}

            **Upload Time:** {datetime.now().strftime("%H:%M:%S")}
            """
        )

        st.subheader(
            "Image Fingerprint"
        )

        st.code(
            image_hash[:32] + "..."
        )

    st.divider()

    # ---------------------
    # Dominant Colors
    # ---------------------

    st.subheader(
        "Dominant Colors"
    )

    colors = get_dominant_colors(
        image
    )

    color_cols = st.columns(5)

    for idx, (color, count) in enumerate(colors):

        hex_color = (
            '#%02x%02x%02x'
            % color
        )

        with color_cols[idx]:

            st.markdown(
                f"""
                <div style="
                height:60px;
                border-radius:10px;
                background:{hex_color};
                border:1px solid #E5E7EB;
                ">
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                hex_color
            )

    st.divider()

    # ---------------------
    # Tabs
    # ---------------------

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "Edge",
        "Sketch",
        "Pixel Art",
        "Cartoon",
        "Grayscale",
        "Negative",
        "Blur",
        "Sharpen"
    ])

    # ---------------------
    # Edge
    # ---------------------

    with tab1:

        edges = edge_detection(
            image
        )

        st.image(
            edges,
            use_container_width=True
        )

        download_image(
            edges,
            "edge_detection"
        )

    # ---------------------
    # Sketch
    # ---------------------

    with tab2:

        sketch = sketch_effect(
            image
        )

        st.image(
            sketch,
            use_container_width=True
        )

        download_image(
            sketch,
            "sketch"
        )

    # ---------------------
    # Pixel Art
    # ---------------------

    with tab3:

        pixel = pixel_art(
            image
        )

        st.image(
            pixel,
            use_container_width=True
        )

        download_image(
            pixel,
            "pixel_art"
        )

    # ---------------------
    # Cartoon
    # ---------------------

    with tab4:

        cartoon = cartoon_effect(
            image
        )

        st.image(
            cartoon,
            use_container_width=True
        )

        download_image(
            cartoon,
            "cartoon"
        )

    # ---------------------
    # Grayscale
    # ---------------------

    with tab5:

        gray = grayscale(
            image
        )

        st.image(
            gray,
            use_container_width=True
        )

        download_image(
            gray,
            "grayscale"
        )

    # ---------------------
    # Negative
    # ---------------------

    with tab6:

        neg = negative(
            image
        )

        st.image(
            neg,
            use_container_width=True
        )

        download_image(
            neg,
            "negative"
        )

    # ---------------------
    # Blur
    # ---------------------

    with tab7:

        blur = blur_image(
            image
        )

        st.image(
            blur,
            use_container_width=True
        )

        download_image(
            blur,
            "blur"
        )

    # ---------------------
    # Sharpen
    # ---------------------

    with tab8:

        sharp = sharpen_image(
            image
        )

        st.image(
            sharp,
            use_container_width=True
        )

        download_image(
            sharp,
            "sharpen"
        )

    st.success(
        "Image processed successfully. Files remain only in your current session."
    )

else:

    st.info(
        "Upload an image to begin analysis."
    )