import sqlite3

# SQLiteデータベースに接続する(ない場合は作られる)
dbname = 'C:/SQLite/hoge.db'
conn = sqlite3.connect(dbname)

# データベースを閉じる
conn.close()