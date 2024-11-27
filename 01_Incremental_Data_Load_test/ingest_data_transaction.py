#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine
import argparse
import os
import psycopg2

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    directory = params.directory
    processed_files_log = 'processed_files.txt'

    # Create database engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Load processed files log if it exists
    if os.path.exists(processed_files_log):
        with open(processed_files_log, 'r') as f:
            processed_files = set(f.read().splitlines())
    else:
        processed_files = set()

    # Loop all file in directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if file.endswith('.csv') and file_path not in processed_files:   # scan only csv file type
            print(f'Processing file: {file}')
          
            df = pd.read_csv(file_path)

            df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

            with open(processed_files_log, 'a') as f:   # Write file name that already read and load to table
                f.write(file_path + '\n')
        else:
            print(f'Skipping already processed file: {file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--directory', help='directory containing CSV files')

    args = parser.parse_args()

    main(args)
