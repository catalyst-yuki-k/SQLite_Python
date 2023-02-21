import sqlite3

# SQLiteデータベースに接続する
dbname = 'C:/Users/user/OneDrive/nekonoizumi/twilog_database/hoge.db'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# データを追加する
# すでに"users"というテーブルがあるものとする
sql = "INSERT INTO users (id, name, age) VALUES (4, 'Dave', 35)"
cur.execute(sql)

# データを取得する
sql = "SELECT id, name, age FROM users"
cur.execute(sql)
for row in cur:
    print("id:", row[0], ", name:", row[1], ", age:", row[2])

# データベースへコミット。これで変更が反映される。
conn.commit()

# カーソルオブジェクトを閉じる
cur.close()

# データベースを閉じる
conn.close()
