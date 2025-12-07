from video2shorts.video import get_video_metadata, trim_video
from video2shorts.whisper import transcribe_audio
from video2shorts.llm import get_hook_segments

import json
import os
import tempfile

from dotenv import load_dotenv
from google import genai
import streamlit as st

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
	st.error("Couldn't load the gemini api key needed for the program")
	raise Exception("Couldn't load the gemini api key needed for the program")

client = genai.Client(api_key=GEMINI_API_KEY)

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
if st.session_state["step"] >= 1:
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
		
		# adding the tempfile name into the session state
		st.session_state["video_url"] = tfile.name

		st.success("Uploaded video successfully")
	
	if is_demo:
		st.session_state["video_url"] = "./assets/sample.mp4"

	if "video_url" in st.session_state and st.session_state["video_url"]:
		st.video(st.session_state["video_url"])

		metadata = get_video_metadata(st.session_state["video_url"])
		st.success(f"Loaded video of duration {metadata["duration"]} seconds.")

		if not metadata["audio"]:
			st.error("The file has no audio")
		else:
			st.session_state["metadata"] = metadata
			st.session_state["step"] = 2

if st.session_state["step"] >= 2:
	st.write("## Step 2: Extracting Audio from the Video")

	st.session_state["audio_url"] = st.session_state["video_url"].replace(".mp4", ".mp3")

	audio = st.session_state["metadata"]["audio"]
	audio.write_audiofile(st.session_state["audio_url"])

	st.success("Audio extracted successfully")
	st.audio(st.session_state["audio_url"])

	st.session_state["step"] = 3

if st.session_state["step"] >= 3:
	st.write("## Step 3: Transcribing Audio through Whisper")

	st.write("If you have loaded the demo video, then you can skip the transcription and load the one already generated.")
	skip_transcription = st.button("Skip transcription")

	try:
		if not skip_transcription:
			transcription = transcribe_audio(st.session_state["audio_url"])
		else:
			with open("./assets/transcription.json", "r") as fp:
				transcription = json.load(fp)
	except Exception as e:
		st.error(e)

	if transcription:
		st.success("Completed the transcription for given audio")

		with st.container(height=400):
			st.write(transcription["text"])

		st.session_state["transcription"] = transcription
		st.session_state["step"] = 4
	else:
		st.error("Unknown error occured while performing the transcription. Please try again later")

if st.session_state["step"] >= 4:
	st.write("## Step 4: Using LLM to extract hooks from the audio transcription")

	st.write("To save the token, we have saved the result of LLM for the demo. So, click the respective button.")
	demo_button = st.button("Are your running siege demo video?", type="primary")
	non_demo_button = st.button("Are you running other video?", type="secondary")

	llm_output = None
	if non_demo_button:
		try:
			llm_output = get_hook_segments(client, st.session_state["transcription"])
			llm_output = json.loads(llm_output)
		except Exception as e:
			st.error(e)
			st.write("You can however run the demo version as each step is cached for demo purposes")
	
	if demo_button:
		with open("./assets/llm.json", "r") as fp:
			llm_output = json.load(fp)

	if llm_output is not None:
		# preparing hooks for display and saving
		hooks = []
		for hook in llm_output:
			start = st.session_state["metadata"]["duration"]
			end = 0
			text = ""

			for id in hook["ids"]:
				segment = st.session_state["transcription"]["segments"][id]
				start = min(start, segment["start"])
				end = max(end, segment["end"])
				text += segment["text"]
			
			hooks.append({
				"start": start,
				"end": end,
				"text": text,
			})

		st.session_state["hooks"] = hooks

		for id, hook in enumerate(hooks):
			with st.container(height=200):
				st.write(f"### Hook-{id+1}")
				st.write(f"**Time = {hook['end']-hook['start']:.1f} seconds**")
				st.write(hook["text"])
		st.session_state["step"] = 5

if st.session_state["step"] >= 5:
	st.write("## View and Download Clips")
	hooks = st.session_state["hooks"]
	
	for i, hook in enumerate(hooks):
		clip_path = trim_video(st.session_state["video_url"], hook["start"], hook["end"])
		st.success(f"Created shorts-{i+1} from the video")
		st.video(clip_path)

		with open(clip_path, "rb") as fp:
			st.download_button(
				label=f"Download short-{i+1}",
				data = fp,
				file_name=f"short-{i+1}.mp4",
				mime="video/mp4"
			)

	st.write("# Thanks for using")
