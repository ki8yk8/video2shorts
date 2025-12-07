from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import tempfile

def add_subtitles(video_path, segments):
	temp_file = tempfile.NamedTemporaryFile(delete=True, suffix=".mp4")
	output_path = temp_file.name
	temp_file.close()

	clip = VideoFileClip(video_path)

	text_clips = []
	for segment in segments:
		text = TextClip(
			font="./assets/futuram.ttf",
			text=segment["text"].strip(),
			font_size=80,
			text_align="left",
			method="caption",
			size=(clip.w*2//3, None),
			color="#000000",
			bg_color="#ffffff",
			duration=segment["end"]-segment["start"],
		).with_start(segment["start"])

		# text.with_position()
		print(text.pos)
		

		print(segment["end"]-segment["start"])

		text_clips.append(text)
	
	final = CompositeVideoClip([clip, *text_clips])
	final.write_videofile(
		output_path,
		codec="libx264",
		audio_codec="aac",
		remove_temp=True,
		preset="ultrafast",
	)

	clip.close()
	final.close()

	return output_path
