CREATE TABLE transaction(
    order_id VARCHAR(256) PRIMARY KEY,
    user_id VARCHAR(256) NOT NULL, 
    product_id  VARCHAR(256) NOT NULL, 
    quantity  INT NOT NULL, 
    amount INT NOT NULL,
    order_date DATE NOT NULL
    );


python ingest_data_transaction.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=data_DB \
  --table_name=transaction \
  --directory=D:/git/DE_TEST_draft/ref/sales