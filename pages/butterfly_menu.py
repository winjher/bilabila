import streamlit as st
from pathlib import Path
from streamlit.components.v1 import html

css_file= Path("C:/Users/jerwin/Documents/GitHub/bilabila/pages/css/style.css")
st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Butterfly App</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="mainNav">
            <ul class="navbar-nav">
                <li class="nav-item" style="color:white; margin-right:15px; text-decoration:none;"><a class="nav-link active" aria-current="page" href="#">Species</a></li>
                <li class="nav-item" style="color:white; margin-right:15px; text-decoration:none;"><a class="nav-link" href="#">Diseases</a></li>
                <li class="nav-item" style="color:white; margin-right:15px; text-decoration:none;"><a class="nav-link" href="#">Defects</a></li>
                <li class="nav-item" style="color:white; margin-right:15px; text-decoration:none;"><a class="nav-link" href="#">Stages</a></li>
            </ul>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)



# HTML for the menu bar
menu_bar = """
<div style="background-color:#333; padding:10px;">
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
</div>
"""

# Add the menu bar to the page
html(menu_bar, height=50)
