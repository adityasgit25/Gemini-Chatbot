# PDF Chat Assistant

A Streamlit web application that allows you to chat with your PDF documents using Google's Gemini AI. Upload a PDF file and ask questions about its content!

## Features

- PDF text extraction using PyMuPDF
- Interactive chat interface
- Powered by Google's Gemini AI
- Simple and intuitive user interface

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   You can get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)
3. Upload a PDF file and start asking questions!

## Usage

1. Click the "Choose a PDF file" button to upload your PDF
2. Wait for the PDF to be processed
3. Type your question in the chat input at the bottom of the page
4. The AI will analyze the PDF content and provide an answer

## Note

- The application works best with text-based PDFs
- Large PDFs may take longer to process
- Make sure your Google API key has sufficient quota for your usage 