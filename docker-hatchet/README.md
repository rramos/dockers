# Hatchet

## Description

Hatchet is a distributed, fault-tolerant task queue designed to solve scaling problems like concurrency, fairness, and rate limiting.

## Setup

```sh
docker-compose up -d
```

One can access the frontend via <http://localhost:8080>

## Test

Create a python environment to run the worker

```sh
python -m venv venv
source venv/bin/activate
pip install python-dotenv
pip install hatchet-sdk
```

Access the frontend and generate a API token then export the following variables as the following example

```sh
export HATCHET_CLIENT_TOKEN="<Your generated API token>"
export HATCHET_CLIENT_TLS_STRATEGY=none
```

And start your test worker

```sh
python worker.py
```

## References

- <https://hatchet.run>
- <https://github.com/hatchet-dev/hatchet>

## Metadata

**Last Verified:** 2025/03/24
