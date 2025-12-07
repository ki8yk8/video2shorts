import streamlit as st
from video2shorts.youtube import is_yt_link_valid, get_yt_video_metadata

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
	
	is_demo = st.button("Load demo URL for Siege", type="primary")
	youtube_video_url = st.text_input(
		"YouTube Video URL", 
		placeholder="https://www.youtube.com/watch?v=jmmW0F0biz0"
	)

	if is_demo:
		youtube_video_url = "https://www.youtube.com/watch?v=jmmW0F0biz0"

	if youtube_video_url:
		if not is_yt_link_valid(youtube_video_url):
			st.error("Invalid Youtube link detected! Please check your link...", icon="🔴")
		else:
			if is_demo:
				st.write("**Using demo Youtube link** ", youtube_video_url)
			else:
				st.write("**Using Youtube link** ", youtube_video_url)
			
			video_metadata = get_yt_video_metadata(youtube_video_url)
			st.write("**Title** ", video_metadata["title"])
			st.write("**Author** ", video_metadata["author"])
			st.write("**Length** ", video_metadata["length"])
			st.image(video_metadata["thumbnail_url"], "Thumbnail for loaded video")

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