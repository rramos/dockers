import polars as pl

QUESTDB_URI = "redshift://admin:quest@localhost:8812/qdb"
QUERY = "SELECT * FROM tables() LIMIT 5;"

df = pl.read_database_uri(query=QUERY, uri=QUESTDB_URI)
print("Received DataFrame:")
print(df)
