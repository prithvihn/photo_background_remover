import streamlit as st
from PIL import Image 
from rembg import remove 
import io

# Page config
st.set_page_config(
    page_title="AI Background Remover",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    /* Center content */
    .block-container {
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Title styling */
    h1 {
        color: white !important;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Subtitle */
    .subtitle {
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    /* File uploader styling */
    .stFileUploader {
        background: white;
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .stFileUploader label {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: #667eea !important;
    }
    
    /* Upload section */
    [data-testid="stFileUploadDropzone"] {
        border: 3px dashed #667eea !important;
        border-radius: 15px !important;
        background: #f8f9ff !important;
        padding: 2rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 3rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 50px !important;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin-top: 1rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 7px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: #10b981 !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 3rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 50px !important;
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4) !important;
        width: 100% !important;
        margin-top: 1rem !important;
    }
    
    /* Image column containers */
    [data-testid="stVerticalBlock"] [data-testid="stImage"] {
        background: white;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    
    /* Checkerboard pattern for result image (shows transparency) */
    [data-testid="stColumn"]:nth-child(2) [data-testid="stImage"] {
        background-image:
            linear-gradient(45deg, #ccc 25%, transparent 25%),
            linear-gradient(-45deg, #ccc 25%, transparent 25%),
            linear-gradient(45deg, transparent 75%, #ccc 75%),
            linear-gradient(-45deg, transparent 75%, #ccc 75%);
        background-size: 20px 20px;
        background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        background-color: #fff;
    }
    
    /* Make uploaded filename text visible */
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] p,
    [data-testid="stFileUploader"] div,
    [data-testid="stFileUploader"] a,
    [data-testid="stFileUploadDropzone"] ~ div *,
    [data-testid="stFileUploader"] [data-testid="stMarkdownContainer"] {
        color: #e5e7eb !important;
    }
    
    /* Section headers */
    h3 {
        color: #667eea !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
        text-align: center;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Success message */
    .stSuccess {
        background: #d1fae5 !important;
        color: #065f46 !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        font-weight: 500 !important;
    }
    
    /* Info boxes */
    .info-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    /* Feature list */
    .feature-list {
        color: #4b5563;
        font-size: 1rem;
        line-height: 2;
    }
    
    /* Hide empty markdown containers (prevents white ghost boxes) */
    .stMarkdown:empty,
    .stMarkdown > div:empty {
        display: none !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>✨ AI Background Remover</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Remove backgrounds from photos instantly with AI-powered precision</p>", unsafe_allow_html=True)

# Info section
col_info1, col_info2, col_info3 = st.columns(3)

with col_info1:
    st.markdown("""
        <div class='info-box'>
            <h4 style='color: #667eea; text-align: center;'>🚀 Fast</h4>
            <p style='text-align: center; color: #6b7280;'>Process images in seconds</p>
        </div>
    """, unsafe_allow_html=True)

with col_info2:
    st.markdown("""
        <div class='info-box'>
            <h4 style='color: #667eea; text-align: center;'>🎯 Accurate</h4>
            <p style='text-align: center; color: #6b7280;'>AI-powered precision</p>
        </div>
    """, unsafe_allow_html=True)

with col_info3:
    st.markdown("""
        <div class='info-box'>
            <h4 style='color: #667eea; text-align: center;'>💯 Free</h4>
            <p style='text-align: center; color: #6b7280;'>No watermarks or limits</p>
        </div>
    """, unsafe_allow_html=True)

# Main upload section
uploaded_file = st.file_uploader(
    "📤 Upload Your Image", 
    type=["jpg", "jpeg", "png"],
    help="Drag and drop or click to browse"
)

# Process image
if uploaded_file:
    # Read image
    image = Image.open(uploaded_file)
    
    # Show original and result side by side (or just original if no result yet)
    has_result = 'output_image' in st.session_state
    
    if has_result:
        col1, col2 = st.columns(2)
    else:
        col1 = st.columns([1])[0]
    
    with col1:
        st.markdown("### 📷 Original Image")
        st.image(image, use_container_width=True)
    
    if has_result:
        with col2:
            st.markdown("### ✨ Result")
            st.image(st.session_state['output_image'], use_container_width=True)
    
    # Process button
    if st.button("🎨 Remove Background", use_container_width=True):
        try:
            with st.spinner("✨ Removing background... Please wait"):
                # Convert to RGB if needed
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                
                # Remove background
                output = remove(image)
                
                # Store in session state
                st.session_state['output_image'] = output
            
            st.success("✅ Background removed successfully!")
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please try with a different image or check your installation.")
    
    # Download button (below the columns)
    if has_result:
        buf = io.BytesIO()
        st.session_state['output_image'].save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="⬇️ Download Result",
            data=byte_im,
            file_name="background_removed.png",
            mime="image/png",
            use_container_width=True
        )

# Footer section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='background: rgba(255,255,255,0.1); border-radius: 15px; padding: 2rem; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.9rem;'>
            Powered by AI • Made with ❤️ using Streamlit & RemBG
        </p>
    </div>
""", unsafe_allow_html=True)