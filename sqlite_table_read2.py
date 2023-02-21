import sqlite3

# SQLiteデータベースに接続する
dbname = 'C:/Users/user/OneDrive/nekonoizumi/twilog_database/hoge.db'
conn = sqlite3.connect(dbname)
# row_factoryにsqlite3.Rowを設定
conn.row_factory = sqlite3.Row 
 
# カーソルオブジェクトを取得する
cur = conn.cursor()

sql = 'select * from users'
cur.execute(sql)
for row in cur:
    # カラム名でアクセスすることができる。
    print(row['id'],row['name'],row['age'])
  
# カーソルオブジェクトを閉じる
cur.close()

# データベースを閉じる
conn.close()