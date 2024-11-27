CREATE TABLE user_transaction_amount(
    user_id VARCHAR(256) PRIMARY KEY, 
    total_sales INT NOT NULL, 
    average_sales NUMERIC(1000, 2) NOT NULL
    );

CREATE TABLE daily_transaction_amount(
    order_date DATE PRIMARY KEY, 
    total_sales INT NOT NULL, 
    min_sales INT NOT NULL, 
    max_sales INT NOT NULL, 
    avg_sales NUMERIC(1000, 2) NOT NULL, 
    vat NUMERIC(1000, 2) NOT NULL
    );

CREATE TABLE product_sales(
    product_id VARCHAR(256) PRIMARY KEY, 
    number_of_transactions INT NOT NULL, 
    total_sales INT NOT NULL
    );

