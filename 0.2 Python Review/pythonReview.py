#creatng videos function

def create_youtube_video(title, description):
	new_youtube_vid = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return new_youtube_vid

def like(new_youtube_vid):
	if "likes" in new_youtube_vid:
		new_youtube_vid["likes"]+=1
		return new_youtube_vid

def dislike(new_youtube_vid):
	if "dislikes" in new_youtube_vid:
		new_youtube_vid["dislikes"]+=1
		return new_youtube_vid

def add_comment(new_youtube_vid, username, comment_text):
	new_youtube_vid["comments"][username] = comment_text
	return new_youtube_vid

youtube_diction = create_youtube_video("mewo", "A mewoing cat")
print(add_comment(youtube_diction, "Liya", "wow!"))

for i in range (495):
	like(youtube_diction)


print(youtube_diction)

