import streamlit as st

# sets the title before any st.title is called
st.set_page_config(page_title="Video2Shorts")

# setting the page title
"""
# Video2Short

Convert your youtube video automatically to shorts using GenAI tools.

**Note** that the application uses some models like Whisper which requires GPU but, we cannot provide you that at the moment since, this is a demo only. So, to use the app fully, look for the options in page to load the demo defaults only. 

**Note** if you are running this app locally then, you can ignore the last note. Just run the pipeline as usual.
"""

# the app is multistep application with following steps;
# 1. Get youtube video url and extract its metadata
# 2. Download the youtube video
# 3. Extract the audio from video
# 4. Transcribe the audio
# 5. Extract hooks for the video from the audio
# 6. Crop the videos into small hook segments
# 7. Download the YT shorts
if "step" not in st.session_state:
	st.session_state["step"] = 1

# 1. Get Youtube video url and extract its metadata
if st.session_state["step"] == 1:
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

if st.session_state["step"] == 2:
	pass
if st.session_state["step"] == 3:
	pass
if st.session_state["step"] == 4:
	pass
if st.session_state["step"] == 5:
	pass
if st.session_state["step"] == 6:
	pass
if st.session_state["step"] == 7:
	pass