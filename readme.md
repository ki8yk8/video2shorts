# Video2Shorts

## About the Project
Video2Shorts is a online Python tool that allows you to convert your YouTube video into smaller shorts. Here is the step by step of how it works;
1. **Uploading the video**, you can upload a video from your local machine in `.mp4` format. Alternatively, for demo purposes you can use the sample video too.
2. **Extracting the audio**, then the audio is extracted from the video,
3. **Transcription of audio**, using OpenAI's Whisper model we transcribe the audio. The transcription will be used to identify the hook segments in the video,
4. **Hooks extraction**, then Google Gemini 2.5 flash API is called to extract the hook sentences and content that can be converted into the shorts. It outputs the start and end time stamp along with suggestion of the title.
5. **Cliiping and downloading**, then each hook content is clipped to create a short and user can download the clipped content easily for the upload.

### Limitations
Due to rate limit of Free Tier of Google Gemini API, the application may not work properly when it exceeds the rate limit. Or, the audio processing part or clipping part might take time. So, alternatively you can click on `I am using Siege demo` button to load the cached content from previous iterations.

## Local Installation and Usage
If you want to setup your own site at your local computer or server,
1. Install the necessary dependency in `pyproject.toml`. I used poetry so, if you are using poetry from dependency management, you can simply do `poetry install`.
2. Run the streamlit applicaation with command,
```bash
streamlit run main.py
```

### FFMPEG
- Note, that `ffmpeg` library is required for this application to run. So, please install it in local system before use.

## Demo
To run, the application you can visit [https://video2shorts.streamlit.app/](https://video2shorts.streamlit.app/)

### Input Video
[Click this link to view input video](./assets/sample.mp4)

### Output Shorts
- [Short 1](./assets/demos/AI%20Decision%20Making_%20How%20Neural%20Networks%20Decide%20with%20a%20Surfing%20Example!.mp4)
- [Short 2](./assets/demos/Beyond%20the%20Basics_%20Different%20Types%20of%20Neural%20Networks%20(CNNs,%20RNNs).mp4)
- [Short 3](./assets/demos/Neural%20Networks%20Explained_%20The%20Basics%20of%20AI%20Brains.mp4)
- [Short 4](./assets/demos/The%20Secret%20Sauce%20of%20AI_%20How%20Neural%20Networks%20Learn%20(Cost%20Function%20&%20Gradient%20Descent).mp4)