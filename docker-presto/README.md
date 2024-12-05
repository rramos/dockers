# Presto

## Description

Presto sandbox

## Setup

Just run docker compose

```sh
docker-compose up -d
```

And access the web interface <http://localhost:7575>

## Presto vs Trino

I would recommend that you check the following article to better understand the differences between Presto and Trino.

- <https://medium.com/@isa-rota/presto-and-trino-comparison-1c6c828b7c50>

There is also a `docker-trino` sample that you can explore.

I would pick Trino specially due to the image sizing

```sh
trinodb/trino      - 1.52GB
prestodb/presto    - 5.43GB
```

## Metadata

**Last Verified:** 2024/12/04
