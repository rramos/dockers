# PostgreSQL

## Description

PostgreSQL service and PgAdmin

## Setup

Just run docker compose

```sh
docker-compose up -d
```

## Management

Access the web interface <http://localhost:5050>

- Login with:

```sh
- username: admin@admin.com
- password: root
```

- Setup new server

- Host: postgres

- Port: 5432

- Username: admin

- Password: root

**NOTE:** Don't use this setup in live enviroments, this is only intended for local use

## Test Cli

One can test directly the connection with the psql command

```sh
psql -h localhost -p 5432 -U admin postgres
```
