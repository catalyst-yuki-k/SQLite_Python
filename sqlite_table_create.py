import sqlite3

# SQLiteデータベースに接続する
dbname = 'C:/Users/user/OneDrive/nekonoizumi/twilog_database/hoge.db'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# テーブル"users"を作成する
# 既にある場合、
# sqlite3.OperationalError: table users already exists
# と表示される。
# テーブルを作成
sql = '''CREATE TABLE users
    (id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL)'''
cur.execute(sql)

# データベースへコミット。コミットしなくてもテーブルの作成自体は反映される。
conn.commit()

# カーソルオブジェクトを閉じる
cur.close()

# データベースを閉じる
conn.close()
