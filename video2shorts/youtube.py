import re
from pytube import YouTube

def is_yt_link_valid(link):
	pattern = r"(https?://)?(www\.)?youtube\.com/watch\?v=[\w-]+"

	return re.match(pattern, link)

def get_yt_video_metadata(url):
	yt = YouTube(url)

	return {
		"yt": yt,
		"title": yt.title,
		"author": yt.author,
		"length": yt.length,
		"thumbnail_url": yt.thumbnail_url,
	}