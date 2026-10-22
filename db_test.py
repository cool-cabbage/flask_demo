import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()#游标

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL
        )
""")

#cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Python编程", "张三"))
#cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Flask入门", "李四"))

conn.commit()  # 提交，真正写入硬盘（和git commit一个意思）

cursor.execute("SELECT * FROM books WHERE id = ?", (2,))
row = cursor.fetchone()
print(row)

cursor.execute("UPDATE books SET title = ? WHERE id = ?", ("数据库基础", 3))
cursor.execute("DELETE FROM books WHERE id = ?", (4,))
conn.commit()

# 查询所有数据
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()  # 拿到所有结果，是一个列表
for row in rows:
    print(row)

conn.close()  # 关闭连接