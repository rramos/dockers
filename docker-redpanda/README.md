# Redpanda

## description

Redpanda is a simple, powerful, and cost-efficient streaming data platform that is compatible with Kafka® APIs while eliminating Kafka complexity. Choose from our fully-managed cloud service or self-hosted platform.

## Setup

Just run docker compose

```
docker-compose up -d
```

Check status with

```
docker exec -it redpanda-0 rpk cluster info
```

Create topic chat-room with

```
docker exec -it redpanda-0 rpk topic create chat-room
```

The following article provides more info:
* https://rramos.github.io/2024/02/14/redpanda


