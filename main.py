import streamlit as st
import tempfile
# from video2shorts.youtube import is_yt_link_valid, get_yt_video_metadata
from video2shorts.video import get_video_metadata

# sets the title before any st.title is called
st.set_page_config(page_title="Video2Shorts")

# setting the page title
"""
# Video2Short

Convert your video automatically to shorts using GenAI tools.

**Note** that the application uses some models like Whisper which requires GPU but, we cannot provide you that at the moment since, this is a demo only. So, to use the app fully, look for the options in page to load the demo defaults only. 

**Note** if you are running this app locally then, you can ignore the last note. Just run the pipeline as usual.
"""

# the app is multistep application with following steps;
# 1. Upload video and extract its metadata
# 2. Extract the audio from video
# 3. Transcribe the audio
# 4. Extract hooks for the video from the audio
# 5. Crop the videos into small hook segments
# 6. Download the YT shorts
if "step" not in st.session_state:
	st.session_state["step"] = 1

# 1. Upload video and extract its metadata
if st.session_state["step"] == 1:
	"""
	## Step 1: Upload your video

	If you are running the app on Streamlit, use the demo video as heavy processing has already been completed for it.
	"""
	
	is_demo = st.button("Load demo video for Siege", type="primary")
	uploaded_file = st.file_uploader(
		label="Upload your video here",
		accept_multiple_files=False,
		type="mp4",
	)

	if uploaded_file is not None:
		tfile = tempfile.NamedTemporaryFile(delete=False)
		tfile.write(uploaded_file.read())

		st.success("Uploaded video successfully")
		st.video(tfile.name)

		# adding the tempfile name into the session state
		st.session_state["video_url"] = tfile.name

		metadata = get_video_metadata(tfile.name)
		st.success(f"Loaded video of duration {metadata["duration"]} seconds.")

		if not metadata["audio"]:
			st.error("The file has no audio")
		else:
			st.session_state["metadata"] = metadata
			st.session_state["step"] = 2

if st.session_state["step"] == 2:
	st.write("## Step 2: Extracting Audio from the Video")

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