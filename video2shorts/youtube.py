def is_yt_link_valid(link):
	# TODO: only for first phase 
	if link.startswith("https://www.youtube.com/"):
		return True
	
	return False

def get_yt_video_metadata(url):
	return {
		"title": "Some title", 
		"thumbnail": "some thumbnail", 
		"length": 10
	}