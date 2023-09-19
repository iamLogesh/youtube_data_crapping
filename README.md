# YouTube Data Scraping and Analysis

This project is designed to scrape data from YouTube using the YouTube Data API, store it in both MongoDB and PostgreSQL databases, and perform data analysis using Python. The data analysis includes various queries and visualizations to gain insights into YouTube channels, playlists, videos, and comments.

## Prerequisites

Before running the scripts, make sure you have the following dependencies installed:

- Python 3.x
- `pymongo` package (for MongoDB interaction)
- `psycopg2` package (for PostgreSQL interaction)
- `pandas` package (for data manipulation and analysis)
- `streamlit` package (for UI and interactive data visualization)
- `Google Client` Library for YouTube Data API

You can install the required Python packages using pip:
```
pip install pymongo psycopg2 pandas streamlit google-api-python-client
```

To use the YouTube Data API, you will need to set up credentials and obtain an API key. Follow the steps below:

1. Create a new project on the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the [YouTube Data API](https://console.cloud.google.com/apis/library) for your project.
3. Create credentials for the API by following the instructions provided by Google. Select the appropriate credentials type for your project.

This allows the Google Client Library to authenticate with the YouTube Data API using your project's credentials.

4. Finally, make sure you have a running MongoDB server and a PostgreSQL database set up with the necessary connection details.

## Project Structure

The project consists of the following files:

- `app.py`: Streamlit application for interactive data visualization and exploration.
- `main.py`: Main script that orchestrates the data scraping and analysis process.
- `MongoDB_Upload.py`: Script to upload data from the YouTube Data API to MongoDB.
- `fetchData_from_MongoDB.py`: Script to fetch data from MongoDB and perform data transformation.
- `migrate_to_SQL.py`: Script to migrate data from MongoDB to PostgreSQL.
- `channel_analysis.py`: Script with various queries to analyze the YouTube data stored in PostgreSQL.

## Usage

1. Clone the repository:
```
git clone https://github.com/iampraveens/Youtube-Data-Scraping.git
```
2. Install the required Python packages:
```
pip install pymongo psycopg2 pandas streamlit google-api-python-client
```
3. Also install the required dependencies:
```
pip install -r requirements.txt
```
or

```
pip3 install -r requirements.txt
```
4. Set up the Google Cloud credentials by following the instructions provided in the `Prerequisites` section.
5. Make sure you have a running MongoDB server and a PostgreSQL database with the necessary connection details. Update the connection parameters in the relevant scripts if needed.
6. To perform data analysis and visualization, run the Streamlit application in your terminal:

```
streamlit run app.py
```
The application will open in your browser, allowing you to explore the data and view visualizations.

7. To perform custom queries and analysis, refer to the `channel_analysis.py` script and execute the desired functions.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create an issue or submit a pull request.

## License

- This project is `Un-Licensed`
- Feel free to use, modify, and distribute this project as needed.

## Acknowledgements

- This project utilizes the YouTube Data API to scrape YouTube data. Make sure to comply with YouTube's terms of service and API usage policies.
- If you have any questions or need assistance, please don't hesitate to [contact me](https://www.linkedin.com/in/iampraveens/).

## Conclusion

- In this project, we have developed a YouTube data scraping and analysis pipeline using the YouTube Data API, MongoDB, and PostgreSQL. We have successfully gathered data on YouTube channels, playlists, videos, and comments, and stored it in both NoSQL (MongoDB) and relational (PostgreSQL) databases.

- The project showcased the capabilities of using Python and the Google Client Library to interact with the YouTube Data API, enabling us to retrieve and process large amounts of data efficiently. We leveraged the power of MongoDB to store the raw scraped data, allowing for flexibility and easy scalability. We also utilized PostgreSQL to transform the data and perform complex queries and analysis.

- The combination of MongoDB and PostgreSQL provided us with a comprehensive approach to data management, allowing us to leverage the strengths of both databases. MongoDB's document-oriented model facilitated the storage and retrieval of unstructured data, while PostgreSQL's relational capabilities allowed us to perform advanced analytics and join data across multiple tables.

- We also built an interactive data visualization application using Streamlit, providing an intuitive interface for users to explore and analyze the scraped YouTube data. The application allowed for dynamic filtering, sorting, and visual representation of the data, enhancing the data exploration experience.

- Overall, this project has demonstrated the power of leveraging various technologies and tools to scrape, store, and analyze YouTube data. It provides a foundation for further research and analysis of YouTube trends, content creators, user engagement, and more. The flexibility of the pipeline allows for easy customization and extension to cater to specific research or business needs.

- By combining the insights gained from the data analysis with domain knowledge and context, stakeholders can make informed decisions, identify popular channels and videos, understand user engagement patterns, and uncover valuable insights for content creators, marketers, and business strategists.

## Video Presentation
- [Part 1](https://www.linkedin.com/posts/iampraveens_data-share-like-activity-7071564603813498880-2qQL?utm_source=share&utm_medium=member_desktop)
- [Part 2](https://www.linkedin.com/posts/iampraveens_data-share-like-activity-7071567796836450305-3vW_?utm_source=share&utm_medium=member_desktop)
