import sqlite3

# SQLiteデータベースに接続する
conn = sqlite3.connect('C:/Users/user/OneDrive/nekonoizumi/twilog_database/hoge.db')

# テーブルからデータを取得する
sql = "SELECT id, name, age FROM users"
cursor = conn.execute(sql)
for row in cursor:
    print("id:", row[0], ", name:", row[1], ", age:", row[2])

# データベースを閉じる
conn.close()
