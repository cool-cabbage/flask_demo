from flask import Flask, jsonify, request

app = Flask(__name__)#__name__指文件名
app.json.ensure_ascii = False

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

books = [
    {"id": 1, "title": "Python编程", "author": "张三"},
    {"id": 2, "title": "Flask入门", "author": "李四"},
    {"id": 3, "title": "数据库基础", "author": "王五"},
]

@app.route("/books")
def get_all_books():
    return jsonify(books)

@app.route("/books/<int:num>")
def get_book(num):
    for book in books:
        if book["id"] == num:
            return jsonify(book)
    return jsonify({"error": "书不存在"}),404

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()  # 拿到用户发来的JSON数据，转成字典
    if not data.get("title") or not data.get("author"):
        return jsonify({"error":"书名和作者不能为空"}), 400

    new_book = {
        "id": books[-1]["id"] + 1,  # 最后一本书的id加1
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)  # 加到列表末尾

    return jsonify(new_book), 201  # 201表示"创建成功"



if __name__ == "__main__":
    app.run(debug=True)
