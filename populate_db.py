import sqlite3
import alpaca_trade_api as tradeapi


connection = sqlite3.connect('app.db')

cursor = connection.cursor()


api = tradeapi.REST('PKG1VWGGEU5M413AP0OC', 'ctSIUS7HX2zTaXQDmLgqZeFBiUsdwsDkoFmGOZBV', base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
assets = api.list_assets()
for asset in assets:

    try:
        cursor.execute("""
            INSERT INTO stock (symbol, name, exchange)
            VALUES (?, ?, ?)
        """, (asset.symbol, asset.name, asset.exchange))
    except Exception as e:
        print(e)
        print(asset)


connection.commit()