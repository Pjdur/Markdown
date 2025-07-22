import streamlit as st
import markdown

st.set_page_config(page_title="Markdown to HTML Converter", layout="centered")
st.title(" Markdown to HTML Converter")

# Upload or paste Markdown
uploaded_file = st.file_uploader("Upload a Markdown (.md) file", type=["md"])
markdown_input = uploaded_file.read().decode("utf-8") if uploaded_file else st.text_area("Or paste your Markdown here:", height=200)

# Convert and style HTML preview
if markdown_input:
    raw_html = markdown.markdown(markdown_input)

    styled_html = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: 'Source Sans Pro', sans-serif;
                    padding: 1em;
                    background-color: transparent;
                    color: #262730;
                }}
                h1, h2, h3, h4, h5 {{
                    color: #0E1117;
                }}
                a {{
                    color: #1E90FF;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>{raw_html}</body>
    </html>
    """

    st.markdown("### Converted HTML:")
    st.code(raw_html, language="html")

    st.markdown("###  Live HTML Preview with Streamlit-style fonts:")
    st.components.v1.html(styled_html, height=300, scrolling=True)