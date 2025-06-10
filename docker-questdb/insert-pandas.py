from datetime import datetime

import pandas as pd
from questdb.ingress import Sender

df = pd.DataFrame(
    {
        "symbol": pd.Categorical(["ETH-USD", "BTC-USD"]),
        "side": pd.Categorical(["sell", "sell"]),
        "price": [2615.54, 39269.98],
        "amount": [0.00044, 0.001],
        "timestamp": pd.to_datetime(
            ["2022-03-08T18:03:57.609765Z", "2022-03-08T18:03:57.710419Z"]
        ),
    }
)

conf = "http::addr=172.25.0.2:9000;"
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name="trades", at=datetime.now())
