from moviepy import VideoFileClip

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

def trim_video(url):
	pass