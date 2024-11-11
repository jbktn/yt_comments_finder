from googleapiclient.discovery import build
import html
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')

def get_comments(youtube, video_id, comments=[], token=''):   
    video_response = youtube.commentThreads().list(part='id,snippet,replies', videoId=video_id, pageToken=token).execute()
    
    for item in video_response['items']:
        user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment = item['snippet']['topLevelComment']
        text = html.unescape(comment['snippet']['textDisplay'])
        comments.append({'user': user, 'comment': text})
    
    if "nextPageToken" in video_response:
        return get_comments(youtube, video_id, comments, video_response['nextPageToken'])
    else:
        return comments



def run():
    youtube = build('youtube', 'v3', developerKey=api_key)
    comment_threads = get_comments(youtube, video_id)

    for comment in comment_threads:
        if comment['user'] == user:
            return comment['comment']

if __name__ == '__main__':
    # video_id = 'd9ngRnSm210'
    # user = '@wezyr81_'
    video_id = input('Enter the video id: ')
    user = input('Enter the username: ')
    comments = run()
    print(comments)