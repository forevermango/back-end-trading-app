import sqlite3, config
connection = sqlite3.connect('config.DF_FILE')
    
cursor = connection.cursor()
cursor.execute("""
    DROP TABLE stock_price
""")
cursor.execute("""
    DROP TABLE stock
""")
connection.commit()