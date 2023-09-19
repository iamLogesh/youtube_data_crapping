from pymongo import MongoClient
import pandas as pd
import re



def convert_duration(duration):
    regex = r'PT(\d+H)?(\d+M)?(\d+S)?'
    match = re.match(regex, duration)
    if not match:
        return '00:00:00'
    hours, minutes, seconds = match.groups()
    hours = int(hours[:-1]) if hours else 0
    minutes = int(minutes[:-1]) if minutes else 0
    seconds = int(seconds[:-1]) if seconds else 0
    total_seconds = hours * 3600 + minutes * 60 + seconds
    # print(total_seconds)
    return total_seconds
    # return '{:02d}:{:02d}:{:02d}'.format(int(total_seconds / 3600), int((total_seconds % 3600) / 60), int(total_seconds % 60))


def connect_MongoDB():
    
    client = MongoClient("mongodb+srv://logeshwaran1478:UXZWAevabU4H6ufW@cluster0.hynp83x.mongodb.net/?retryWrites=true&w=majority")
    
    database = client.project_testing
    collection = database.channel_data
    
    result = collection.find({})
    
    return result

def channelStats_from_MongoDB():
    
    channel_stats = connect_MongoDB()
    data_list = []
    
    if channel_stats:
        for document in channel_stats:
            Channel_Id = document.get('Channel_Name', {}).get('Channel_Id')
            Channel_name = document.get('Channel_Name', {}).get('Channel_Name')
            Channel_Type = document.get('Channel_Name', {}).get('Channel_Type')
            Channel_Views = document.get('Channel_Name', {}).get('Channel_Views')
            Channel_Description = document.get('Channel_Name', {}).get('Channel_Description') or None
            Channel_Status = document.get('Channel_Name', {}).get('Channel_Status')
            
            data = {"channel_id": Channel_Id,
                    "channel_name": Channel_name,
                    "channel_type": Channel_Type,
                    "channel_views": Channel_Views,
                    "channel_description": Channel_Description,
                    "channel_status": Channel_Status}
            
            data_list.append(data)
            
        return pd.DataFrame(data_list)
        

def playlistStats_from_MongoDB():
    
    playlist_stats = connect_MongoDB()
    
    data_list = []
    
    if playlist_stats:
        for document in playlist_stats:
            Channel_name = document.get('Channel_Name', {}).get('Channel_Name')
            Playlist_Id = document.get('Channel_Name', {}).get('Playlist_Id')
            Channel_Id = document.get('Channel_Name', {}).get('Channel_Id')
            
            data = {
                    "channel_name": Channel_name,
                    "playlist_id": Playlist_Id,
                    "channel_id": Channel_Id
                    }
            
            data_list.append(data)
            
        return pd.DataFrame(data_list)
   

def commentStats_from_MongoDB():
    
    comment_stats = connect_MongoDB()
    
    data_list = []

    for document in comment_stats:
        
        Channel_name = document.get('Channel_Name', {}).get('Channel_Name')
        
        
        for key, value in document.items():
            if key.startswith('Video_Id_'):
                video_id = value
                comments = video_id.get('Comments', {})
                for comment_id, comment in comments.items():
                    data = {
                        'channel_name': Channel_name,
                        'comment_id': comment.get('Comment_Id'),
                        'video_id': video_id.get('Video_Id'),
                        'comment_text': comment.get('Comment_Text'),
                        'comment_author': comment.get('Comment_Author'),
                        'commentPublishedAt': pd.to_datetime(comment.get('Comment_PublishedAt'))
                    }
                    
                    data_list.append(data)
               
    return pd.DataFrame(data_list) 


def videoStats_from_MongoDB():
    
    video_stats = connect_MongoDB()
    
    data_list = []
    
    for document in video_stats:
        
        channel_name = document.get('Channel_Name', {}).get('Channel_Name')
        Video_id = document.get('Channel_Name', {}).get('Playlist_Id')
        
        for key, value in document.items():
            if key.startswith('Video_Id_'):
                video_id = value
                duration = video_id.get('Duration')
                
                data = {
                        'channel_name': channel_name,
                        'video_id': video_id.get('Video_Id'),
                        'playlist_id': Video_id,
                        'video_name': video_id.get('Video_Name'),
                        'video_description': video_id.get('Video_Description'),
                        'published_date': video_id.get('PublishedAt'),
                        'view_count': video_id.get('View_Count'),
                        'like_count': video_id.get('Like_Count'),
                        'dislike_count': video_id.get('Dislike_Count'),
                        'favourite_count': video_id.get('Favorite_Count'),
                        'comment_count': video_id.get('Comment_Count'),
                        'duration': convert_duration(duration),
                        'thumbnail': video_id.get('Thumbnail'),
                        'caption_status': video_id.get('Caption_Status')
                        }
                
                data_list.append(data)
                
    return pd.DataFrame(data_list)



