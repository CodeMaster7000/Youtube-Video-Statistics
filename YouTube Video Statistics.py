from tkinter import *
from googleapiclient.discovery import build
def video_details():
	if "youtube" in video_url.get():
		video_id = video_url.get()[len("https://www.youtube.com/watch?v="):]
	else:
		video_id = video_url.get()
	youtube = build('youtube','v3',developerKey='Enter API Key: ')
	video_request=youtube.videos().list(
		part='snippet,statistics',
		id=video_id
	)
	video_response = video_request.execute()
	title = video_response['items'][0]['snippet']['title']
	likes = video_response['items'][0]['statistics']['likeCount']
	views = video_response['items'][0]['statistics']['viewCount']
	details.config(text=f"Title: {title}\nLikes: {likes}\nViews: {views}")
root = Tk()
root.geometry("500x300")
Label(root,text="Title, Views & Likes of a YouTube Video", fg="red",
	font=("Helvetica 18 bold"),relief="solid",bg="white").pack(pady=10)
Label(root,text="Enter video URL/ID:", font=("10")).pack()
video_url = Entry(root,width=40,font=("15"))
video_url.pack(pady=10)
Button(root,text="Fetch Details" ,font=("Helvetica 15 bold"),command=video_details).pack()
details = Label(root,text="")
details.pack(pady=10)
root.mainloop()
