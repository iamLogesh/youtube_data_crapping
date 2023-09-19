import psycopg2 as pg2
from fetchData_from_MongoDB import *



hostname = 'localhost'
dbname = 'postgres'
username = 'postgres'
pwd = '1478'
port_id = '5432'

connection = pg2.connect(
            host= hostname,
            database=   dbname,
            user= username,
            password= pwd,
            port= port_id)

database = connection.cursor()
print("successful")

def create_channel_table():
    
    database.execute('DROP TABLE IF EXISTS channel CASCADE')
    
    database.execute('''CREATE TABLE IF NOT EXISTS channel(
                                    channel_id          VARCHAR(255) PRIMARY KEY,
                                    channel_name        VARCHAR(255),
                                    channel_type        VARCHAR(255),
                                    channel_views       INT,
                                    channel_description TEXT,
                                    channel_status      VARCHAR(255))'''
                                )

    query = '''
            INSERT INTO channel (channel_id, channel_name, channel_type, channel_views, channel_description, channel_status)
            VALUES (%s, %s, %s, %s, %s, %s)

            '''
    channel_df = channelStats_from_MongoDB()

    for _, row in channel_df.iterrows():
        values = tuple(row)
        database.execute(query, values)
        
    connection.commit()
    
def create_playlist_table():
    
    database.execute('DROP TABLE IF EXISTS playlist CASCADE')
        
    database.execute('''CREATE TABLE IF NOT EXISTS playlist(
                                    channel_name        VARCHAR(255),
                                    playlist_id         VARCHAR(255) PRIMARY KEY,
                                    channel_id          VARCHAR(255) REFERENCES channel(channel_id))'''
                                )
    
    query = '''
                INSERT INTO playlist (channel_name, playlist_id, channel_id) 
                VALUES (%s, %s, %s)
                
            '''
    
    channel_df = playlistStats_from_MongoDB()

    for _, row in channel_df.iterrows():
        values = tuple(row)
        database.execute(query, values)
        
    connection.commit()
    
def create_video_table():
    
    database.execute('DROP TABLE IF EXISTS video CASCADE')
    
    database.execute('''CREATE TABLE IF NOT EXISTS video(
                                    channel_name        VARCHAR(255),
                                    video_id            VARCHAR(255) PRIMARY KEY,
                                    playlist_id         VARCHAR(255),
                                    video_name          VARCHAR(255),
                                    video_description   TEXT,
                                    published_date      TIMESTAMP,
                                    view_count          INT,
                                    like_count          INT,
                                    dislike_count       INT,
                                    favorite_count      INT,
                                    comment_count       INT,
                                    duration            INT,
                                    thumbnail           VARCHAR(255),
                                    caption_status      VARCHAR(255),
                                    FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id) )'''
                                )
    
    query = '''
                INSERT INTO video (channel_name, video_id, playlist_id, video_name, video_description, published_date, view_count, like_count, dislike_count, favorite_count, comment_count, duration, thumbnail, caption_status)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 

            '''
            
    channel_df = videoStats_from_MongoDB()

    for _, row in channel_df.iterrows():
        values = tuple(row)
        database.execute(query, values)
        
    connection.commit()
    
def create_comment_table():
    
    database.execute('DROP TABLE IF EXISTS comment CASCADE')

    database.execute('''CREATE TABLE IF NOT EXISTS comment(
                                channel_name            VARCHAR(255),
                                comment_id              VARCHAR(255) PRIMARY KEY,
                                video_id                VARCHAR(255) REFERENCES video(video_id),
                                comment_text            TEXT,
                                comment_author          VARCHAR(255),
                                comment_published_date  TIMESTAMP)'''
                            )

    query = '''
            INSERT INTO comment (channel_name, comment_id, video_id, comment_text, comment_author, comment_published_date)
            VALUES (%s,%s,%s,%s,%s,%s)

            '''
    channel_df = commentStats_from_MongoDB()

    for _, row in channel_df.iterrows():
        values = tuple(row)
        database.execute(query, values)       
    
    connection.commit()
