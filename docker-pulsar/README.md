# Pulsar

## Description

Run a standalone Pulsar cluster in Docker


## Setup

Just run docker compose

```
docker-compose up -d
```

# Test

Install a pulsar client to test

```
pip install pulsar-client
```

The run the producer to produce some test messages

```
python producer.py
```

In a different terminal launch a consumer
```
python consumer.py
```

Get topic statistics

```
curl http://localhost:3838/admin/v2/persistent/public/default/my-topic/stats | python -m json.tool
```


# Documentation

 * https://pulsar.apache.org
 
