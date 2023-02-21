import sqlite3

# SQLiteデータベースに接続する
dbname = 'C:/Users/user/OneDrive/nekonoizumi/twilog_database/hoge.db'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()
 
# テーブル一覧を取得する
sql = "select * from sqlite_master where type='table'"
cur.execute(sql)
for row in cur.fetchall():
    print(row)

# テーブルを削除する
sql = "drop table person;"
cur.execute(sql)

# テーブル一覧を取得する
sql = "select * from sqlite_master where type='table'"
cur.execute(sql)
for row in cur.fetchall():
    print(row)

# カーソルオブジェクトを閉じる
cur.close()

# データベースを閉じる
conn.close()