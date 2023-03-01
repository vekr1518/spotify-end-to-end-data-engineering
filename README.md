# Spotify end-to-end-data-engineering

### Introduction
In this Project, We will build an ETL pipeline using the Spotify API on AWS.The pipeline will retrieve data from the spotify API,transform it to a different format and load it into a AWS data store.


+ **Integrating with Spotify API and extracting Data**
+ **Deploying code on AWS Lambda for Data Extraction**
+ **Adding trigger to run the extraction automatically**
+ **Writing transformation function**
+ **Building automated trigger on transformation function**
+ **Store files on S3 properly**
+ **Building Analytics Tables on data files using Glue and Athena**

### Architecture
![This is an image](https://github.com/vekr1518/spotify-end-to-end-data-engineering/blob/main/Architecture_Spotify.jpg)

### About Dataset/API
This dataset contains information about music, artist, albums and songs - [Spotify API](https://developer.spotify.com/documentation/web-api/)

# Services Used
1. **S3 (Simple Storage Service)**
2. **AWS Lambda**
3. **Cloudwatch**
4. **Glue Crawler**
5. **Data Catalog**
6. **Amazon Athena**
