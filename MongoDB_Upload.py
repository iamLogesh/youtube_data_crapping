from pymongo import MongoClient
from main import bind_data



def upload_to_MongoDB(api_key, channel_id):
    
    
    client = MongoClient(f"mongodb+srv://logeshwaran1478:UXZWAevabU4H6ufW@cluster0.hynp83x.mongodb.net/?retryWrites=true&w=majority")
    
    upload = bind_data(api_key, channel_id)
    
    database = client.project_testing
    collection = database.channel_data
    
    try:
        existing_document = collection.find_one({"Channel_Name.Channel_Id": channel_id})
        if existing_document is None:
            collection.insert_one(upload)
            print("Data uploaded successfully")
        else:
            print("Channel ID already exist")
    except Exception as e:
        print(f"Error occurred while uploading data: {str(e)}")
        
    client.close()
    

def view_channel_name():
    
    client = MongoClient(f"mongodb+srv://logeshwaran1478:UXZWAevabU4H6ufW@cluster0.hynp83x.mongodb.net/?retryWrites=true&w=majority")
    
    database = client.project_testing
    collection = database.channel_data
    
    try:
        names = []
        for i in collection.find({}):
            channel_name = i["Channel_Name"]["Channel_Name"]
            names.append(channel_name)
    except Exception as e:
        print(f"{str(e)}")
        
    client.close()
    
    return names

