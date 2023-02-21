import sqlite3

# SQLiteデータベースに接続する
dbname = 'C:/Users/user/OneDrive/nekonoizumi/twilog_database/hoge.db'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# データを追加する
# すでに"users"というテーブルがあるものとする
cur.execute("INSERT INTO users (id, name, age) VALUES (1, 'Alice', 25)")
cur.execute("INSERT INTO users (id, name, age) VALUES (2, 'Bob', 30)")
cur.execute("INSERT INTO users (id, name, age) VALUES (3, 'Charlie', 35)")

# 複数のレコードを一括して挿入するには、executemany()メソッドにinsert文を渡します。
sql = 'insert into users (id, name, age) values (?,?,?)'
data = [(1, 'Alice', 25), 
        (2, 'Bob', 30), 
        (3, 'Charlie', 35)]
cur.executemany(sql, data)

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
