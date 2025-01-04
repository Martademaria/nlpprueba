import os
import streamlit as st
from openai import AzureOpenAI
from io import BytesIO
from fpdf import FPDF
from PIL import Image
import requests
import PyPDF2
import markdown 

# SET UP
# ======
## Initialize our streamlit app
st.set_page_config(
    page_title="RiskRadar", 
    page_icon='⚖️',
    layout='wide'
    )

menu = ["HOME", "OUR SOLUTION", "FEEDBACK"]

# Color Hex codes
lightblue = "#15abf7"
purpleblue = "#6b76f7"
purble = "#c13cfc"

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@800&display=swap');
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .stButton > button {
        height: auto;
        padding-top: 20px;
        padding-bottom: 20px;
        font-weight: bold !important;
        color: #15abf7; /* Blue text */
        background-color: black; /* Black background */
        border: 5px solid #15abf7; /* Blue border */
        border-radius: 40px;
        width: 100%;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #15abf7; /* Blue background */
        color: white; /* White text */
        border: 5px solid #15abf7; /* Ensures border stays blue */
    }

    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .stDownloadButton > button {
        height: auto;
        padding-top: 20px;
        padding-bottom: 20px;
        font-weight: bold !important;
        color: #15abf7; /* Blue text */
        background-color: black !important; /* Black background */
        border: 5px solid #15abf7 !important; /* Blue border */
        border-radius: 40px;
        width: 100%;
        cursor: pointer;
    }
    .stDownloadButton > button:hover {
        background-color: #15abf7 !important; /* Blue background */
        color: white !important; /* White text */
        border: 5px solid #15abf7 !important; /* Ensures border stays blue */
    }

    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
        .custom-list {
            color: white !important;
            font-family: 'Open Sans', serif;
            font-weight: normal;
            font-size: 16px !important;
            list-style-position: inside;
            padding: 0;
            margin: 0;
        }
        .custom-list li {
            margin-bottom: 0px;
        }
    </style>
    """, unsafe_allow_html=True)