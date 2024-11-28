## Folder Structure
Each folder contains its own README.md file, which explains the process of the code.

- `01-setup-database` folder contains the database setup tasks.

- `02-incremental-data-load-test` folder contains the solution for the Incremental Data Load question.

- `03-complex_data_transformation_test` folder contains the solution for the Complex Data Transformation with Aggregation question.

## Data Engineer Skill Tests

### *** Setup database ***

Initialize database using Dockerfile or docker-compose file, 
you can choose any database you want e.g. PostgreSQL, MySQL, etc.

_Write some explanation such as which port that you use to connect or expose your database. <br>
Keep it simple, don't take too much time to do this step, we just make sure you understand docker technology._

### Extract User Info

We provide sample user info in `./ref/user_info.csv`.

#### What you have to do:
1. Write SQL statement to create `user_info` table
2. Implement an ELT process that:
    - Extract data from `user_info.csv`
    - Save extracted data in database


---


### Question for Incremental Data Load 

We provide sample 7 days sale transactions in `./ref/sales` folder. Place your result in `incremental_data_load_test` folder

#### What you have to do:
1.  Create `transaction` table with SQL statement for save raw data 
    - Fields: 
        - order_id (string)
        - user_id (string)
        - product_id (string)
        - quantity (number)
        - amount (number)
        - order_date (date)

2.  Implement an ELT process that:
    - Extracts data from csv files in `./ref/sales` folder.
    - Loads the daily transaction into a transaction table (without re-processing old files.)

_Tips you can track old transaction from order id_ 


#### Expectation:
1.  SQL statement file for create database table with given fields
2.  Python script for ELT process


### Question for Complex Data Transformation with Aggregation 

From last question you will have transaction table, it'll be used in this question, Place your result in `complex_data_transformation_test` folder

#### What you have to do:
1.  Create `user_transaction_amount`, `daily_transaction_amount` and `product_sales` tables with SQL statement for save calculated data

2.  Implement an ETL process that:
    - Extract: raw data from `transaction` table.
    - Transform: Group and aggregate the data to calculate:
        - Total and average sales (quantity x amount) by user.
        - Total, min, max, average sales and VAT(sales x 0.07) by day.
        - Number of transactions and Total sales per product.
    - Load: Save each aggregation as a separate table in database.

    You can decide field and type for created table

3.  Implement an ETL process that:
    - Extract: raw data from `user_info`, `transaction` or other table.
    - Transform: Group and aggregate the data to calculate:
        - Total, min, max, average transaction amount by user location and gender
        - Top 20 best selle in Chiangmai by day (require field product_id and sales (quantity x amount) )


#### Expectation:
1.  SQL statement file for create database tables
2.  Python script for ETL process
