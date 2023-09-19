import psycopg2 as pg2
import pandas as pd

hostname = 'localhost'
dbname = 'postgres'
username = 'postgres'
pwd = '1478'
port_id = '5432'

connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)

database = connection.cursor()
print("successful")

def question1():
    database.execute("SELECT channel.channel_name, video.video_name FROM channel JOIN video ON channel.channel_name = video.channel_name;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'video_name']).reset_index(drop=True)
    df.index += 1
    return df

def question2():
    database.execute("SELECT channel.channel_name, COUNT(video.video_id) AS video_count FROM channel JOIN video ON channel.channel_name = video.channel_name GROUP BY channel.channel_name ORDER BY video_count DESC;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'video_count']).reset_index(drop=True)
    df.index += 1
    return df

def question3():
    database.execute("SELECT video.video_name, channel.channel_name, video.view_count FROM video JOIN channel ON video.channel_name = channel.channel_name ORDER BY video.view_count DESC LIMIT 10;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'video_name', 'View count']).reset_index(drop=True)
    df.index += 1
    return df

def question4():
    database.execute("SELECT video_name, comment_count from video ORDER BY comment_count DESC;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['video Name', 'comment count']).reset_index(drop=True)
    df.index += 1
    return df

def question5():
    database.execute("SELECT video.video_name, channel.channel_name, video.like_count FROM video JOIN channel ON video.channel_name = channel.channel_name ORDER BY video.like_count DESC;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'video_name', 'like_count']).reset_index(drop=True)
    df.index += 1
    return df

def question6():
    database.execute("SELECT video_name, like_count, dislike_count FROM video ORDER BY like_count DESC, dislike_count ASC;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['video_name', 'like_count', 'dislike_count']).reset_index(drop=True)
    df.index += 1
    return df

def question7():
    database.execute("SELECT channel_name, channel_views FROM channel ORDER BY channel_views DESC;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'total_number_of_views']).reset_index(drop=True)
    df.index += 1
    return df

def question8():
    database.execute("SELECT channel.channel_name, video_name, video.published_date FROM channel JOIN video ON channel.channel_name = video.channel_name WHERE EXTRACT(YEAR FROM video.published_date) = 2022;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'video_name', 'Year_2022']).reset_index(drop=True)
    df.index += 1
    return df

def question9():
    database.execute("SELECT channel.channel_name, AVG(video.duration) AS average_duration FROM channel JOIN video ON channel.channel_name = video.channel_name GROUP BY channel.channel_name;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'average_duration_of_videos']).reset_index(drop=True)
    df['average_duration_of_videos'] = df['average_duration_of_videos'].astype(float)
    df['average_duration_of_videos'] = df['average_duration_of_videos'].round(2)
    df.index += 1
    return df

def question10():
    database.execute("SELECT channel_name, video_name, comment_count FROM video ORDER BY comment_count DESC;")
    result = database.fetchall()
    df = pd.DataFrame(result, columns=['channel_name', 'video_name', 'number_of_comments']).reset_index(drop=True)
    df.index += 1
    return df
