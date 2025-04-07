# Cockroach

## Description

Cockroach database docker container

## Setup

Just run docker compose

```sh
docker-compose up -d
```

## Connect

Get the Id of the cockroach docker with `docker ps`

Then connect to it eg

```sh
docker exec -ti eb25ce3ef695 ./cockroach sql --insecure
```

## Metadata

**Last Verified:** 2025/04/07
