from main import bind_data
from MongoDB_Upload import *
from fetchData_from_MongoDB import *
from migrate_to_SQL import *
from channel_analysis import *
import streamlit as st
import time


def main():
    
    st.set_page_config(
            page_title="Youtube Scraping",
            page_icon= ":desktop_computer:",
            layout="wide"
    )
    
    
    st.title("YouTube Data Scraping")

    
    
    # Input fields for API key and Channel ID
    #api_key = st.text_input("Enter your API Key:", type="password", key="api_key")
    api_key = "AIzaSyD61NMSE0SRVg2xL2KYYGABGBB5nd1Vy8w"
    channel_id = st.text_input("Enter the Channel ID:", key="channel_id")
        
    
    fetch_json, fetch_text, upload_data, view_channel, migrate_sql, channel_anlysis = st.tabs([" Fetch Json Data ", " Fetch Text Data ", 
                                                                                            " Upload To MongoDB ", " View Channel Tables", 
                                                                                            " Migrate To SQL ", " Channel Analysis "])
    
    st.markdown(
    """
    <style>
    div[data-baseweb="input"] {
        width: 500px !important;
    }
    </style>
    """,
    unsafe_allow_html=True)
    
    
    with fetch_json:
    # Button to fetch JSON data
        if st.button("Fetch JSON Data"):
            try:
                # Call the get_channel_stats function and display the results as JSON
                data = bind_data(api_key, channel_id)
                st.json(data)
                st.success("Successfully fetched Json")
            except:
                st.error("An error occurred. Please check your API Key or Channel ID.")

    with fetch_text:
    # Button to fetch data and display as text
        if st.button("Fetch Text Data"):
            try:
                # Call the get_channel_stats function and display the results as text
                data = bind_data(api_key, channel_id)
                text_output = format_data_as_text(data)
                st.text(text_output)
            except:
                st.error("An error occurred. Please check your API Key or Channel ID.")
    
    with upload_data:
        if st.button("Upload To MongoDB"):
            with st.spinner("Uploading data to MongoDB..."):
                try:
                    upload_to_MongoDB(api_key, channel_id)
                    time.sleep(3)
                    st.success("Data uploaded successufully")
                except:
                    st.error("An error occurred while uploading data to MongoDB")
                
    with view_channel:
        
        Document_list = view_channel_name()
        selected_channel = st.selectbox("Select a channel", Document_list)
        
        if selected_channel:
            
            view_table =  st.button("View Table")
            
            if view_table:
                with st.spinner("Fetching data from MongoDB..."):
                    try:
                        channel_stats = channelStats_from_MongoDB()  # Convert DataFrame only once
                        playlist_stats = playlistStats_from_MongoDB()
                        comment_stats = commentStats_from_MongoDB()
                        video_stats = videoStats_from_MongoDB()
                        selected_channelStats = channel_stats[channel_stats["channel_name"] == selected_channel]
                        selected_playlistStats = playlist_stats[playlist_stats["channel_name"] == selected_channel]
                        selected_commentStats = comment_stats[comment_stats["channel_name"] == selected_channel]
                        selected_videoStats = video_stats[video_stats["channel_name"] == selected_channel]
                        
                        if not selected_channelStats.empty:
                            st.write("Table: Channel")
                            st.dataframe(selected_channelStats)
            
                        if not selected_playlistStats.empty:
                            st.write("Table: Playlist")
                            st.dataframe(selected_playlistStats)
                            
                        if not selected_commentStats.empty:
                            st.write("Table: Comment")
                            st.dataframe(selected_commentStats)
                            
                        if not selected_videoStats.empty:
                            st.write("Table: Video")
                            st.dataframe(selected_videoStats)
                            st.success("Successfully fetched data from MongoDB!")    
                                                   
                    except Exception as e:
                        st.error(f"An error occurred while fetching data to MongoDB: {str(e)}")
                        
    with migrate_sql:
        
        st.write('Click to migrate entire tables to PostgreSQL: ')
        migrate_SQL = st.button("Migrate To SQL")
               
        if migrate_SQL:
            with st.spinner("Uploading data to PostgreSQL..."):
                try:
                    create_channel_table()
                except Exception as e:
                    st.error(f"An error occurred while uploading data to PostgreSQL: {str(e)}")
                
                try:
                    create_playlist_table()
                except Exception as e:
                    st.error(f"An error occurred while uploading data to PostgreSQL: {str(e)}")
                    
                try:
                    create_video_table()
                except Exception as e:
                    st.error(f"An error occurred while uploading data to PostgreSQL: {str(e)}")
                    
                try:
                    create_comment_table()
                    st.success("Data uploaded successfully to PostgreSQL!") 
                except Exception as e:
                    st.error(f"An error occurred while uploading data to PostgreSQL: {str(e)}")
    
    with channel_anlysis:
        select_question =  st.selectbox("Select the question to analyse: ", ('Tap to view',
                            '1. What are the names of all the videos and their corresponding channels?',
                            '2. Which channels have the most number of videos, and how many videos do they have?',
                            '3. What are the top 10 most viewed videos and their respective channels?',
                            '4. How many comments were made on each video, and what are their corresponding video names?',
                            '5. Which videos have the highest number of likes, and what are their corresponding channel names?',
                            '6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?',
                            '7. What is the total number of views for each channel, and what are their corresponding channel names?',
                            '8. What are the names of all the channels that have published videos in the year 2022?',
                            '9. What is the average duration of all videos in each channel, and what are their corresponding channel names?',
                            '10. Which videos have the highest number of comments, and what are their corresponding channel names?'))
        
        if select_question == '1. What are the names of all the videos and their corresponding channels?':
            st.dataframe(question1())
        
        elif select_question == '2. Which channels have the most number of videos, and how many videos do they have?':
            st.dataframe(question2())
            
        elif select_question == "3. What are the top 10 most viewed videos and their respective channels?":
            st.dataframe(question3())
            
        elif select_question == "4. How many comments were made on each video, and what are their corresponding video names?":
            st.dataframe(question4())
            
        elif select_question == "5. Which videos have the highest number of likes, and what are their corresponding channel names?":
            st.dataframe(question5())
            
        elif select_question == "6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?":
            st.dataframe(question6())
            
        elif select_question == "7. What is the total number of views for each channel, and what are their corresponding channel names?":
            st.dataframe(question7())
            
        elif select_question == "8. What are the names of all the channels that have published videos in the year 2022?":
            st.dataframe(question8())
            
        elif select_question == "9. What is the average duration of all videos in each channel, and what are their corresponding channel names?":
            st.dataframe(question9())
        
        elif select_question == "10. Which videos have the highest number of comments, and what are their corresponding channel names?":
            st.dataframe(question10())
    
def format_data_as_text(data):
    
    text_output = ""

    def format_comments(comments):
        if not comments:
            return "No comments available"

        comments_text = ""
        for comment_id, comment in comments.items():
            comments_text += f"{comment_id}\n"
            comments_text += f"Comment ID: {comment['Comment_Id']}\n"
            comments_text += f"Text: {comment['Comment_Text']}\n"
            comments_text += f"Author: {comment['Comment_Author']}\n"
            comments_text += f"Published At: {comment['Comment_PublishedAt']}\n\n"
        return comments_text.strip()

    for key, value in data.items():
        if key.startswith("Video_Id_"):
            video_output = ""
            video_output += f"{key}\n"
            video_output += f"Video ID: {value['Video_Id']}\n"
            video_output += f"Title: {value['Video_Name']}\n"
            description = value['Video_Description'].replace('\n', ' ')
            video_output += f"Description: {description}\n"
            video_output += f"Published At: {value['PublishedAt']}\n"
            video_output += f"Views: {value['View_Count']}\n"
            video_output += f"Likes: {value['Like_Count']}\n"
            video_output += f"Dislikes: {value['Dislike_Count']}\n"
            video_output += f"Favorites: {value['Favorite_Count']}\n"
            video_output += f"Comments: {value['Comment_Count']}\n"
            video_output += f"Duration: {value['Duration']}\n"
            video_output += f"Thumbnail: {value['Thumbnail']}\n"
            video_output += f"Caption Status: {value['Caption_Status']}\n"
            video_output += f"\nComments:\n{format_comments(value['Comments'])}\n\n"
            text_output += video_output
        elif key == "Channel_Name":
            channel_output = "\n"
            channel_output += f"Channel Name: {value['Channel_Name']}\n"
            channel_output += f"Channel ID: {value['Channel_Id']}\n"
            channel_output += f"Subscription Count: {value['Subscription_Count']}\n"
            channel_output += f"Channel Views: {value['Channel_Views']}\n"
            channel_output += f"Channel Description: {value['Channel_Description']}\n"
            channel_output += f"Playlist ID: {value['Playlist_Id']}\n"
            channel_output += f"Channel Status: {value['Channel_Status']}\n"
            channel_output += f"Channel Type: {value['Channel_Type']}\n\n"
            text_output += channel_output

    return text_output.strip()



if __name__ == "__main__":
    main()
