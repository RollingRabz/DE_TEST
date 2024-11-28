## Create table

Create a table named `transaction` in the `data_DB` database, using the query from `Create_transaction.sql` located in the  `01-setup-database` folder.

Data type in `transaction` table
```
CREATE TABLE transaction(
  order_id     VARCHAR(256) PRIMARY KEY,
  user_id      VARCHAR(256) NOT NULL, 
  product_id   VARCHAR(256) NOT NULL,
  quantity     INT          NOT NULL, 
  amount       INT          NOT NULL,
  order_date   DATE         NOT NULL
);
```

## Ingest data to table
The python script will contain
- Load the processed files log, if it exists.

  - This file is used to store the names of files that have already been processed. If a file name is found in `processed_files.txt`, that file will be skipped.

  - If the processed files log does not exist, a new one will be created. The first time the script is run, it will create a new log file.
 
- Ingest data

  - Loop through all the files in the given directory to ingest them into the database. If a file has already been processed, it will be skipped.

Run this command in the terminal (make sure the current working directory is this folder first).

```
python ingest_data_transaction.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=data_DB \
  --table_name=transaction \
  --directory=D:/git/DE_TEST/ref/sales
```
