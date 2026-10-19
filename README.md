# Flask Demo

学习Flask时写的练习项目，实现了一个简单的图书管理API。

## 功能

- 返回文本和JSON数据
- 查询所有图书 / 按id查询图书
- 通过POST请求添加图书，带输入检查

## 接口说明

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 返回欢迎信息 |
| GET | `/hello/<name>` | 返回问候语 |
| GET | `/add/<a>/<b>` | 计算两个数的和 |
| GET | `/user/<name>` | 返回用户信息（JSON） |
| GET | `/books` | 获取所有图书 |
| GET | `/books/<id>` | 获取指定图书，不存在返回404 |
| POST | `/books` | 添加图书，缺少字段返回400 |

### 添加图书示例

请求体：

    {
        "title": "算法导论",
        "author": "赵六"
    }

成功返回201和新书信息。

## 运行方法

    pip install flask
    python app.py

启动后访问 http://127.0.0.1:5000

## 技术栈

- Python
- Flask

## 说明

数据存在内存中，重启服务后添加的图书会丢失。
