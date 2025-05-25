YouTube & Website URL Content Summarization
This project provides a tool to summarize content from YouTube videos and website URLs. By extracting transcripts from YouTube videos or text from web pages, it generates concise summaries to help users quickly grasp the main points.

Features
YouTube Video Summarization: Extracts transcripts from YouTube videos and summarizes the content.
Website URL Summarization: Fetches and summarizes text content from web pages.
Streamlit Interface: User-friendly web interface for inputting URLs and viewing summaries.

Installation
git clone https://github.com/Shyamal1508/youtube_website_url_content_summarization.git
cd youtube_website_url_content_summarization

Create a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Usage
Run the Streamlit Application:
streamlit run app.py
Interact with the Application:
Enter a YouTube video URL or a website URL into the provided input field.
Click the "Summarize" button.
View the generated summary below the input field.

Project Structure
youtube_website_url_content_summarization/
├── app.py             # Main application script
├── README.md   
