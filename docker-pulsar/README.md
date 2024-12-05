# Pulsar

## Description

Run a standalone Pulsar cluster in Docker

## Setup

Just run docker compose

```sh
docker-compose up -d
```

## Test

Install a pulsar client to test

```sh
pip install pulsar-client
```

The run the producer to produce some test messages

```sh
python producer.py
```

In a different terminal launch a consumer

```sh
python consumer.py
```

Get topic statistics

```sh
curl http://localhost:3838/admin/v2/persistent/public/default/my-topic/stats | python -m json.tool
```

## Documentation

- <https://pulsar.apache.org>
