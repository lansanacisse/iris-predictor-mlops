from datetime import datetime

def add_footer():
    current_year = datetime.now().year
    footer = f"""
    <style>
        footer {{
            visibility: hidden;
        }}
        .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f5f5f5;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            color: #888;
        }}
    </style>
    <div class="footer">
        <p>Build by <b>Lansana CISSE</b> - M2 SISE | {current_year}</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
