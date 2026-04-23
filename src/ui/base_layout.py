import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius: 5rem !important;
            }

        </style>  
    """, unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

            .stApp {
                background: #E0E3FF !important;
            }

        </style>  
    """, unsafe_allow_html=True)
    


def style_base_layout():

    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        #MainMenu, footer, header {
            visibility: hidden;
        }
                
        .block-container {
            padding-top:1.5rem !important;    
        }

        h1 {
    font-family: 'Climate Crisis', sans-serif !important;
    font-size: 3.2rem !important;
    margin-bottom:0rem !important;
    color: black !important;
    letter-spacing: 2px;
}

        h2 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 2rem !important;
    margin-bottom:0rem !important;
    color: black !important;
}
                
        h3, h4, p {
            font-family: 'Outfit', sans-serif;    
        }

        /* Buttons */
        button{
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
        }

        button[kind="secondary"]{
            background-color: #EB459E !important;
            color: white !important;
        }

        button[kind="tertiary"]{
            background-color: black !important;
            color: white !important;
        }

        button:hover{
            transform :scale(1.05)
        }

        </style>
    """, unsafe_allow_html=True)


    # ✅ Only necessary safe tweaks
    st.markdown("""
    <style>

    /* Stats text */
    div[style*="background: #EB459E10"] {
        color: black !important;
    }

    /* Spinner text */
    [data-testid="stSpinner"] {
        color: #7C3AED !important;
    }

    /* Input labels */
    label {
        color: #5865F2 !important;
        font-weight: 600;
    }

    /* Warning box */
    [data-testid="stAlert"] {
        background-color: #E0E3FF !important;
        border-left: 6px solid #5865F2 !important;
    }

    [data-testid="stAlert"] p {
        color: #5865F2 !important;
        font-weight: 600;
    }

    /* Keep buttons safe */
    button, button * {
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)