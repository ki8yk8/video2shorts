import streamlit as st

@st.cache_resource
def get_hook_segments(_client, transcription):
	try:
		response = _client.models.generate_content(
			model="gemini-2.5-flash",
			contents="What is your name?"
		)

		print(response.text)

		return response
	except Exception as e:
		raise e