## Create table

Create table name `transaction` in database created from `00_Setup_DB` folder using query in `Create_transaction.sql`

Data type in `transaction` table
```
order_id     VARCHAR(256) PRIMARY KEY
user_id      VARCHAR(256) NOT NULL 
product_id   VARCHAR(256) NOT NULL
quantity     INT          NOT NULL 
amount       INT          NOT NULL
order_date   DATE         NOT NULL
```

## Ingest data to table
The python script will contain
- Load processed files log if it exists

  - This file is used to store file name that is already processed. If the file name is in the `processed_files.txt`, that file will be skipped.

  - If processed files log is not exist, it will create a new one. The first time running this script it will create a new one.
 
- Ingest data

  - Loop all file in the given directory to ingest it to database, if that file already processed it will skipped that file.

Run this command in terminal (pwd must be in this folder)

```
python ingest_data_transaction.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=data_DB \
  --table_name=transaction \
  --directory=D:/git/DE_TEST_draft/ref/sales
```
