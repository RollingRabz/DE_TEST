# In this test I use PostgreSQL as a database
## Dockerfile
* State the necessary library and python version

## docker-compose.yaml file
* State what images I used which are postgres version 13 and pgadmin
  - Create volumn for Mounts a local directory `./DB_data` to the container's PostgreSQL data directory `/var/lib/postgresql/data` with read-write access `rw`

    to ensures that database data is persisted on the host system, even if the container is stopped or removed.
  - For postgres I used port 5432 on host machine map to container port 5432(default)
  - For pgadmin I used port 8080 on host machine map to container port 80(default)
  - For easy usage, in this test I directly fill in the user and password in .yaml which can be improve by create `.env` file and store user and password in it for more security. since docker Compose automatically reads `.env` file when running and we can reference it likethis in   `.yaml` file.
    
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
* There are 2 way to access postgres in this test
  - 
