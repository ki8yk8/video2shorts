from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import tempfile

margin = 40

def add_subtitles(video_path, segments):
	temp_file = tempfile.NamedTemporaryFile(delete=True, suffix=".mp4")
	output_path = temp_file.name
	temp_file.close()

	clip = VideoFileClip(video_path)

	text_clip = add_simple_subtitles(clip, segments)
	final = CompositeVideoClip([clip, text_clip])
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
	max_width = clip.w * 2//3
	x, y = 0, 0

	for segment in segments:
		for text in segment["text"].split(" "):
			if len(text.strip()) == 0:
				continue

			text_clip = TextClip(
				font="./assets/futuram.ttf",
				text=text.strip(),
				font_size=80,
				margin=(20, 20),
				text_align="left",
				method="caption",
				size=(100, None),
				color="#000000",
				bg_color="#ffffff",
			)

			x += text_clip.w

			if x > max_width:
				x = 0
				y += text_clip.h

			text_clip = text_clip.with_duration(segment["end"]-segment["start"])
			text_clip = text_clip.with_start(segment["start"])
			text_clip = text_clip.with_position((x, y))

			text_clips.append(text_clip)

	composite_clip = CompositeVideoClip(text_clips)
	composite_clip = composite_clip.with_position((margin, clip.h-margin-composite_clip.h))

	return composite_clip
	