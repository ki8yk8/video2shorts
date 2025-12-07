import os
import whisper
import streamlit as st

@st.cache_data
def transcribe_audio(audio_path, size="tiny"):
	if not os.path.exists(audio_path):
		raise FileNotFoundError(f"File not found at '{audio_path}'")

	model = whisper.load_model(size)
	result = model.transcribe(audio_path)

	return result
