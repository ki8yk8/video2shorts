from moviepy import VideoFileClip
import tempfile

def download_video_from_yt(url):
	pass

def get_video_metadata(path):
	clip = VideoFileClip(path)

	return {
		"duration": clip.duration,
		"fps": clip.fps,
		"width": clip.w,
		"height": clip.h,
		"audio": clip.audio
	}

def trim_video(path, start, end):
	temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
	output_path = temp_file.name
	temp_file.close()

	clip = VideoFileClip(path)
	trimmed_clip = clip.subclipped(start, end)

	trimmed_clip.write_videofile(
		output_path,
		codec="libx264",
		audio_codec="aac",
		remove_temp=True,
		preset="ultrafast",
	)
	clip.close()
	trimmed_clip.close()

	return output_path