#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine
import argparse

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db

    # Create database engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Load data from the database
    query = "SELECT * FROM user_info JOIN transaction USING(user_id);" # will have only user who purchased at least once
    df = pd.read_sql(query, con=engine)
    # Calculate spending column
    df['spending'] = df['quantity'] * df['amount']

    # Group by location and gender, calculate the aggregates
    result_df = (
        df.groupby(['location', 'gender'])
        .agg(
            total_spending=('spending', 'sum'),
            min_spending=('spending', 'min'),
            max_spending=('spending', 'max'),
            average_spending=('spending', lambda x: round(x.mean(), 2))
        )
        .reset_index()
        .sort_values(by=['location', 'gender'])
    )

    # Filter for location = 'Chiangmai'
    chiangmai_df = df[df['location'] == 'Chiangmai']

    # Group by order_date and product_id, calculate total sales
    cm_df = (
        chiangmai_df.groupby(['order_date', 'product_id'])
        .agg(sales=('spending', 'sum'))
        .reset_index()
        .sort_values(by='sales', ascending=False)
        .head(20)  # Select top 20 rows
    ).reset_index(drop=True)

    # show sample result
    print(result_df.head(10))
    print('Only first 10 rows shown')
    print(cm_df.head(10)) 
    print('Only first 10 rows shown')
     # save result as csv file
    result_df.to_csv('transaction_by_loc_gen.csv', index=False)
    cm_df.to_csv('top_20_cm_sales.csv', index=False)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate and save sales data to Postgres.')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')

    args = parser.parse_args()

    main(args)
