"""
AI Content Writer
A Streamlit web app for generating marketing content using AI.
"""

import streamlit as st
from content_generator import generate_content

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Content Writer",
    page_icon="📝",
    layout="centered",
)

# ----------------------------
# Custom Styling
# ----------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #6b7280;
        margin-bottom: 1.5rem;
    }
    .output-box {
        background-color: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 1.2rem;
        margin-top: 1rem;
        line-height: 1.6;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="main-title">📝 AI Content Writer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Generate ready-to-use content for blogs, social media, and product listings.</div>',
    unsafe_allow_html=True,
)

# ----------------------------
# Input Form
# ----------------------------
with st.form("content_form"):
    topic = st.text_input(
        "Topic",
        placeholder="e.g., Benefits of morning yoga for busy professionals",
    )

    content_type = st.selectbox(
        "Content Type",
        ["Blog Post", "Instagram Caption", "LinkedIn Post", "Product Description"],
    )

    submitted = st.form_submit_button("✨ Generate Content")

# ----------------------------
# Generation & Output
# ----------------------------
if submitted:
    if not topic.strip():
        st.warning("Please enter a topic before generating content.")
    else:
        with st.spinner("Generating content..."):
            result = generate_content(topic=topic, content_type=content_type)

        st.subheader("Generated Content")
        st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download as .txt",
            data=result,
            file_name=f"{content_type.lower().replace(' ', '_')}.txt",
            mime="text/plain",
        )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Powered by a placeholder generator — connect your own AI API key in content_generator.py")
