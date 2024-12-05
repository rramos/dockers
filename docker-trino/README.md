# Trino

## Description

Trino sandbox - formally known as Presto

## Setup

Just run docker compose

```sh
docker-compose up -d
```

And access the web interface <http://localhost:7676> (Login: username)

This interface allows you to check the queries

## Using a client

### Requirements

Install trino-cli

```sh
pacman -S trino-cli-bin
```

Then execute

```sh
trino http://localhost:7676
```

### Check available catalogs

```sql
trino> show catalogs;
 Catalog
---------
 jmx
 memory
 system
 tpcds
 tpch
(5 rows)

Query 20241204_230349_00000_qti82, FINISHED, 1 node
Splits: 11 total, 11 done (100.00%)
1.20 [0 rows, 0B] [0 rows/s, 0B/s]
```

### Select statement

```sql
trino> select count(*) from tpch.sf1.nation;
 _col0
-------
    25
(1 row)

Query 20241204_230358_00001_qti82, FINISHED, 1 node
Splits: 13 total, 13 done (100.00%)
3.12 [25 rows, 0B] [8 rows/s, 0B/s]
```

The following section of the documentation may be usefull to setup connectors to push computation.

- <https://trino.io/docs/current/connector.html>

## Metadata

**Last Verified:** 2024/12/04
