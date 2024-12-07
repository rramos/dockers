# Pulsar

## Description

Run a standalone Pulsar cluster in Docker

## Setup

Just run docker compose

```sh
docker-compose up -d
```

## Test

### Dependencies

```sh
python -m venv venv
source  venv/bin/activate
pip install -r requirements.txt
```

In a different terminal launch a consumer

```sh
python consumer.py
```

The run the producer to produce some test messages

```sh
python producer.py
```

Get topic statistics

```sh
curl http://localhost:3838/admin/v2/persistent/public/default/my-topic/stats | python -m json.tool
```

## Documentation

- <https://pulsar.apache.org>

## Metadata

**Last Verified:** 2024/12/07
