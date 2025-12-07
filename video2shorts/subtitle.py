from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import tempfile

margin = 40

def add_subtitles(video_path, segments):
	temp_file = tempfile.NamedTemporaryFile(delete=True, suffix=".mp4")
	output_path = temp_file.name
	temp_file.close()

	clip = VideoFileClip(video_path)

	text_clips = add_simple_subtitles(clip, segments)
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


def add_simple_subtitles(clip, segments):
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
		)

		text = text.with_duration(segment["end"]-segment["start"])
		text = text.with_start(segment["start"])
		text = text.with_position((margin, clip.h-text.h-margin))

		text_clips.append(text)

	return text_clips
	