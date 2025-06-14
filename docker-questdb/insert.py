from questdb.ingress import Sender, TimestampNanos

conf = "http::addr=172.25.0.2:9000;"
with Sender.from_conf(conf) as sender:
    sender.row(
        "trades",
        symbols={"symbol": "ETH-USD", "side": "sell"},
        columns={"price": 2615.54, "amount": 0.00044},
        at=TimestampNanos.now(),
    )
    sender.row(
        "trades",
        symbols={"symbol": "BTC-USD", "side": "sell"},
        columns={"price": 39269.98, "amount": 0.001},
        at=TimestampNanos.now(),
    )
    sender.flush()
