import streamlit as st

"""
# Video2Short

Convert your youtube video automatically to shorts using GenAI tools
"""

"""
## Insert your YouTube Video URL
The url is in the format: `https://www.youtube.com/watch?v=...`
"""
youtube_video_url = st.text_input(
	"YouTube Video URL", 
	placeholder="https://www.youtube.com/watch?v=jmmW0F0biz0"
)

if youtube_video_url:
	st.write("The video URL is", youtube_video_url)