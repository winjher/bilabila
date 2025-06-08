import streamlit as st

# Custom CSS to mimic your HTML's styling
# You can put this in a separate .css file and link it, or inline it as shown.
st.markdown("""
<style>
    .card-banner {
        display: flex; /* Use flexbox for horizontal alignment */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center; /* Center items */
        gap: 40px; /* Space between cards */
        margin-top: 30px;
        margin-bottom: 30px;
    }
    .col-card {
        flex: 1 1 calc(25% - 20px); /* Approx 4 columns, adjusts for gap */
        min-width: 220px; /* Minimum width for each card */
        max-width: 250px; /* Max width to prevent cards from becoming too wide */
        text-align: center;
        padding: 15px;
        /* border: 1px solid #ddd; /* Optional: if you want card borders */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #fcfcfc;
        transition: transform 0.2s ease-in-out;
    }
    .col-card:hover {
        transform: translateY(-5px); /* Simple hover effect */
    }
    .banner {
        /* Styles for the div wrapping the image */
        margin-bottom: 15px;
    }
    .img-banner {
        max-width: 80px; /* Control icon size */
        height: auto;
        border-radius: 50%; /* Make icons circular if desired */
        padding: 5px; /* Spacing around icon */
        background-color: #e0f7fa; /* Light background for icons */
    }
    .title-banner {
        color: #333;
        font-size: 1.3em;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .p-index {
        color: #555;
        font-size: 0.9em;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)


# --- Content for each card ---
cards_data = [
    {
        "icon": "./icon-1.webp",
        "title": "Purpose",
        "text": "To address these challenges, the complex, multivariate and unpredictable agricultural ecosystems need to be better understood by monitoring, measuring and analyzing continuously various physical aspects and phenomena."
    },
    {
        "icon": "icon/quality.png",
        "title": "Quality",
        "text": "As a farmer its task is to culture butterflies with extra care management by maintaining the indicator host plant for sustainability needs in butterfly farming or propagation."
    },
    {
        "icon": "icon/dtask.png",
        "title": "Function",
        "text": "In order to have knowledge about the lepidoptera, the cultured species are examined sequentially and adaptively identified by the researcher. The system should decide on the precise tasks, and predicting model such as segmenting images, detecting objects in images, or classifying images."
    },
    {
        "icon": "icon/jewels.png",
        "title": "Elegant",
        "text": "With the ability to adapt and learn from new data, machine learning models can refine their breeding strategies and improve quality performance, helping breeders stay ahead in an ever-evolving and dynamic biodiversity. As markets become more data-driven and sophisticated, the integration of machine learning in breeding is no longer a luxury but a necessity for those seeking a competitive edge."
    }
]

# Create columns for the card layout
# Using `st.columns` directly allows better control than just writing markdown.
# The number of columns should match the number of cards, or you can dynamically adjust.
cols = st.columns(len(cards_data)) # Create as many columns as there are cards

for i, card in enumerate(cards_data):
    with cols[i]:
        # Use st.markdown with unsafe_allow_html=True to inject custom HTML for cards
        # This allows us to use our custom CSS classes for styling.
        st.markdown(f"""
        <div class="col-card">
            <div class="banner">
                <img src="{card['icon']}" class="img-banner" alt="{card['title']}">
            </div>
            <div class="card-app-banner">
                <h2 class="title-banner">{card['title']}</h2>
                <p class="p-index">{card['text']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Note: The `onclick="bounceBanner()"` JavaScript functionality would need to be
# reimplemented using Streamlit's event handling or custom HTML/JS if truly necessary,
# but for a static display of information, it's often not critical.