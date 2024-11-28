# In this test I used PostgreSQL as a database
## Dockerfile
* State the required library and the Python version.

## docker-compose.yaml file
* Specify the Docker images I used, which include PostgreSQL version 13 and pgAdmin.
  - Create a volume to mount the local directory `./DB_data` to the container's PostgreSQL data directory `/var/lib/postgresql/data` with read-write `rw` access. This ensures that database data is persisted on the host system, even if the container is stopped or removed.
  - For PostgreSQL, I mapped port 5432 on the host machine to the container's default port 5432.
  - For pgAdmin, I mapped port 8080 on the host machine to the container's default port 80.
  - For simplicity in this test, I directly specified the username and password in the `.yaml` file. However, this can be improved by creating a `.env` file to store the credentials for better security. Since Docker Compose automatically reads the `.env` file when running, we can reference the variables in the `.yaml` file.
    
  ```
  FROM

  environment:
  - POSTGRES_USER=root
  - POSTGRES_PASSWORD=root
  - POSTGRES_DB=data_DB

  TO
  
  environment:
  - POSTGRES_USER=${POSTGRES_USER}
  - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
  - POSTGRES_DB=${POSTGRES_DB}

  ```

## Access postgres
* There are two ways to access PostgreSQL in this test.
  
1. Terminal
 
```
pgcli -h localhost -p 5432 -u root -d data_DB
```

2. pgAdmin (a GUI tool for managing the PostgreSQL database, which is easier to use than the terminal).

```
http://localhost:8080/
```

## Create table

The query used to create the table is in `Create_userinfo.sql`

## Ingest data to database

Using python script

Run this command in the terminal (make sure the current working directory is this folder first).

```
python ingest_data_user.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=data_DB \
  --table_name=user_info
```
