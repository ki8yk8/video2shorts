import streamlit as st
import json

@st.cache_data
def get_hook_segments(_client, transcription):
	try:
		response = _client.models.generate_content(
			model="gemini-2.5-flash",
			contents=create_prompt(transcription)
		)

		return json.loads(response.text[8:-3])
	except Exception as e:
		raise e

def create_prompt(transcription):
	SYSTEM_PROMPT = """
	You are an expert content director who is going though the transcription of an speech. Your task as a content director is to extract the major hook segments from the transcription. 
	
	Here, are criterias for hook segments.
	- They should be engaging, informative and something that can be converted into short.
	- The total time for a hook segment should be greater than 30 second but less than 3 minutes.
	- There can be overlap between any two hook segements but, make sure content are not repeated the same.
	- It is not compulsory all the segments belong to atleast one hook segment. Create hook segment if and only if it can gain more views because of its richness in content.
	- You can create as many hook segment you want but it should follow all above criteria.

	The transription are array of objects in JSON with the keys;
	- id, unique transcription segment id
	- text, transcription text of that segment
	- start, duration on audio where the text starts in seconds
	- end, duration on audio where the text ends in seconds

	The output should be array of objects in JSON, where each object represents a hook segment that can be converted into shorts with keys;
	- time, total duration of the hook segment
	- ids, array of unique id that creates the hook segments
	- title, title for the given short for uploading on youtube

	Output format
	```json
	[{time: 30, ids: [1, 2, ...], title: "some title"}, ...]
	```

	Donot output anything except JSON which is strict requirement.
	"""

	return f"""
	{SYSTEM_PROMPT}
	```json
	{reformat_transcription(transcription)}
	```
	"""

def reformat_transcription(transcription):
	return json.dumps([{
		"id": s["id"],
		"start": s["start"],
		"end": s["end"],
		"text": s["text"],
	} for s in transcription["segments"]])