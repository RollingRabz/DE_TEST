## Create table 
Create three tables in the existing `data_DB` database using the queries in `Create_tables.sql`

Table
`user_transaction_amount`

```
CREATE TABLE user_transaction_amount(
  user_id       VARCHAR(256)      PRIMARY KEY,
  total_sales   INT               NOT NULL, 
  average_sales NUMERIC(1000, 2)  NOT NULL
);
```

To store total and average sales (quantity x amount) by user.

Table
`daily_transaction_amount`  

```
CREATE TABLE daily_transaction_amount(
  order_date     DATE             PRIMARY KEY,
  total_sales    INT              NOT NULL,
  min_sales      INT              NOT NULL,
  max_sales      INT              NOT NULL,
  avg_sales      NUMERIC(1000, 2) NOT NULL,
  vat            NUMERIC(1000, 2) NOT NULL
);
```

To store total, min, max, average sales and VAT(sales x 0.07) by day.

Table
`product_sales`

```
CREATE TABLE product_sales(
  product_id             VARCHAR(256) PRIMARY KEY,
  number_of_transactions INT          NOT NULL,
  total_sales            INT          NOT NULL
);
```

To store number of transactions and Total sales per product.

## ETL_1

- Run this command in the terminal (make sure the current working directory is this folder first).

```
python ETL_1.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=data_DB 
```

- Read data from the database using the `sqlalchemy` library

```
from sqlalchemy import create_engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

query = "SELECT * FROM transaction"
df = pd.read_sql(query, con=engine)
```

This will retrieve data from the database using an SQL query, then perform a transformation process to extract the required data.

- Write the finished DataFrame back to a specific table in the database.

```
user_transaction.to_sql(name='user_transaction_amount', con=engine, if_exists='append', index=False)
daily_transaction.to_sql(name='daily_transaction_amount', con=engine, if_exists='append', index=False)
product_sale.to_sql(name='product_sales', con=engine, if_exists='append', index=False)
```

Now, the three tables we created earlier will contain data.

## ETL_2

Instead of transforming the data and loading it into the database, I will save it to two CSV files, which are

1. `transaction_by_loc_gen.csv` contain total, min, max, average transaction amount by user location and gender.
2. `top_20_cm_sales.csv` contain top 20 best sell in Chiangmai by day (require field product_id and sales (quantity x amount)).

- Run this command in the terminal (make sure the current working directory is this folder first).

```
python ETL_2.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=data_DB 
```

- Read data from database using library name `sqlalchemy`

```
from sqlalchemy import create_engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

query = "SELECT * FROM user_info JOIN transaction USING(user_id);" # will have only user who purchased at least once
df = pd.read_sql(query, con=engine)
```

This process retrieves data from the database using an SQL query by joining two tables together.

Next, it performs a transformation process to extract the required data.

- Save the final DataFrames to CSV files.

```
result_df.to_csv('transaction_by_loc_gen.csv', index=False)
cm_df.to_csv('top_20_cm_sales.csv', index=False)
```
