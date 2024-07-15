def create_youtube_video(title, description):
	Youtube_Video={"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return Youtube_Video


def like(Youtube_Video):
	if "likes" in Youtube_Video:
		Youtube_Video["likes"] += 1
	return Youtube_Video

def dislike(Youtube_Video):
	if "dislikes" in Youtube_Video:
		Youtube_Video["dislikes"] += 1
	return Youtube_Video


def add_comment(Youtube_Video,username,comment_text):
	Youtube_Video["comments"][username] = comment_text
	
	return Youtube_Video


Video = create_youtube_video("Blabla", "welcome to my video")

like(Video)
dislike(Video)
add_comment(Video,"Jhon11", "nice video")

print(Video)