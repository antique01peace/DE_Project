import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

#AWS Access And Secret key
# aws_access_key = "AKIA4IUNEVRNMLTGCNNF"
# aws_secret_key = "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"
aws_access_key = "BoDD3/AeLUlf6/nzioHdA5X/qL6piMZkOEZSw7+YowE="
aws_secret_key = "Mg/SlmX7IpPUyyyEOnaLCtXH03UPBJ36UJnwLmx8RQqkWp+63JDeLFBeZKZfyqib"
bucket_name = "youtube-project-testing"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties
database_name = "youtube_project"
url = f"jdbc:mysql://localhost:3306/{database_name}"
properties = {
    "user": "root",
    "password": "password",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\file_from_s3\\"
customer_data_mart_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\customer_data_mart\\"
sales_team_data_mart_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\sales_partition_data\\"
error_folder_path_local = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\error_files\\"