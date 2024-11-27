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
    query = "SELECT * FROM transaction"
    df = pd.read_sql(query, con=engine)

    # Perform calculations: Total and Average Sales by User
    user_transaction = (
        df.assign(sales=df['quantity'] * df['amount'])
          .groupby('user_id')['sales']
          .agg(total_sales='sum', average_sales='mean')
          .reset_index()
    )

    # Write the result back to a PostgreSQL table
    user_transaction.to_sql(name='user_transaction_amount', con=engine, if_exists='append', index=False)

    # Calculate the total sales (quantity * amount)
    df['total_sales'] = df['quantity'] * df['amount']

    # Group by 'order_date' and apply the necessary aggregation functions

    daily_transaction = df.groupby('order_date').agg(
        total_sales=('total_sales', 'sum'),
        min_sales=('total_sales', 'min'),
        max_sales=('total_sales', 'max'),
        avg_sales=('total_sales', 'mean')
    ).reset_index()
    # Add VAT as 7% of the total sales
    daily_transaction['vat'] = daily_transaction['total_sales'] * 0.07

    daily_transaction.to_sql(name='daily_transaction_amount', con=engine, if_exists='append', index=False)

    # Group by 'product_id' and perform the aggregations
    product_sale = (
        df.groupby('product_id')
        .agg(
            number_of_transactions=('order_id', 'count'),  # Count the number of unique order_id (transactions) per product
            total_sales=('total_sales', 'sum')  # Sum the total sales for each product
        )
        .reset_index()
    )

    product_sale.to_sql(name='product_sales', con=engine, if_exists='append', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate and save sales data to Postgres.')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')

    args = parser.parse_args()

    main(args)
