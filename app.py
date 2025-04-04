import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Set page config
st.set_page_config(
    page_title="PDF Chat Assistant",
    page_icon="📚",
    layout="wide"
)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'pdf_text' not in st.session_state:
    st.session_state.pdf_text = ""

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file."""
    try:
        # Read the PDF file
        pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        
        # Extract text from each page
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text += page.get_text()
        
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return None

def get_gemini_response(prompt, context):
    """Get response from Gemini API."""
    try:
        # Create a prompt that includes the context and user's question
        full_prompt = f"""Context: {context}

Question: {prompt}

Please provide a clear and concise answer based on the context above."""
        
        # Generate response using Gemini with the new format
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(
            contents=[{
                "parts": [{"text": full_prompt}]
            }]
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Main UI
st.title("📚 PDF Chat Assistant")
st.write("Upload a PDF and ask questions about its content!")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    if not st.session_state.pdf_text:
        with st.spinner("Extracting text from PDF..."):
            st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)
            if st.session_state.pdf_text:
                st.success("PDF processed successfully!")
            else:
                st.error("Failed to process PDF. Please try again.")

# Chat interface
if st.session_state.pdf_text:
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question about the PDF"):
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(prompt, st.session_state.pdf_text)
                st.write(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
else:
    st.info("Please upload a PDF file to start chatting.") 