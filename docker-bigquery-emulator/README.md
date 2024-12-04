# Bigquery Emulator

## Description

Bigquery emulator docker container

## Setup

Just run docker compose

```
docker-compose up -d
```

Example with `bq` sdk 

### Create dataset

```sh
bq --api http://0.0.0.0:9050 mk  --project_id=test --dataset --description="Test dataset" dataset1
```

### Create a table

```sh
bq --api http://0.0.0.0:9050 mk --project_id=test --table --description="table1" dataset1.table1 "qtr:STRING,sales:FLOAT,year:STRING"
```

### Insert data

```sh
bq --api http://0.0.0.0:9050 query  --project_id=test "INSERT dataset1.table1(qtr,sales,year) VALUES('foo',12.3,'2024')"
```

### Query data

```sh
bq --api http://0.0.0.0:9050 query  --project_id=test "SELECT * FROM dataset1.table1"
```

## References

* https://github.com/goccy/bigquery-emulator

## Metadata

**Last Verified:** 2024/12/04