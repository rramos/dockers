# Zeppelin

## description

Web-based notebook that enables data-driven, interactive data analytics and collaborative documents with SQL, Scala and more.

## Setup

Just run docker compose

```sh
docker-compose up -d
```

And access the web interface <http://localhost:8080>

## Test Spark

Create a Dataframe with People running

```scala
%spark
case class People(name: String, age: Int)
var df = spark.createDataFrame(List(People("jeff", 23), People("andy", 20)))
df.createOrReplaceTempView("people")
```

Then create a new cell to select data from the Dataframe

```scala
%spark.sql
select * from people
```

You can explore other options on the following doc <https://zeppelin.apache.org/docs/latest/interpreter/spark.html>

## Metadata

**Last Verified:** 2024/12/04
