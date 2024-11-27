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

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df=pd.read_csv('D:/git/DE_TEST_draft/ref/user_info.csv')

    df.to_sql(name = table_name, con = engine, if_exists = 'append', index = False)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')

    args = parser.parse_args()

    main(args)





    

