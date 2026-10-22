import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)#__name__指文件名
app.json.ensure_ascii = False


DB_PATH = "books.db"


def get_db():
    """连接数据库，查询结果可以像字典一样按列名取值"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """建表，如果表是空的就放几本示例书"""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
    count = conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]
    if count == 0:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Python编程", "张三"))
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Flask入门", "李四"))
        conn.commit()
    conn.close()

@app.route("/")
def hello():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_name(name):
    return f"你好，{name}！"

@app.route("/add/<a>/<b>")
def add(a, b):
    return f"{a} + {b} = {int(a)+int(b)}"

@app.route("/user/<name>")
def get_user(name):
    user = {
        "name": name,
        "age": 18,
        "language": "Python"
    }
    return jsonify(user)

@app.route("/books")
def get_all_books():
    conn = get_db()

    rows = conn.execute("SELECT * FROM books").fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])


@app.route("/books/<int:num>")
def get_book(num):
    conn = get_db()

    row = conn.execute("SELECT * FROM books WHERE id = ?", (num,)).fetchone()#不加fetchone返回的只是游标
    conn.close()

    if row is None:
        return jsonify({"error": "书不存在"}), 404
    
    return jsonify(dict(row))

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()  # 拿到用户发来的JSON数据，转成字典

    if not data.get("title") or not data.get("author"):#get是为了判断这个键存不存在
        return jsonify({"error":"书名和作者不能为空"}), 400
    
    conn = get_db()
    cursor = conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (data["title"], data["author"]))
    conn.commit()

    new_id = cursor.lastrowid

    conn.close()

    return jsonify({"id" : new_id, "title" : data["title"], "author" : data["author"]}), 201  # 201表示"创建成功",且不能只返回状态码



if __name__ == "__main__":
    init_db()
    app.run(debug=True)

