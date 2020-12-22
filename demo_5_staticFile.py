from flask import Flask, url_for


# ============
# 静态文件（url_for('static',filename=)）
# ============

# 动态的文件一般也需要静态文件，例如CSS样式表和JavaScript文件。
# 理想情况中服务器已经配置好了为你的提供静态文件的服务。但是在开发过程中， 
# Flask 也能做好 这项工作。

# 只要在你的包或模块旁边创建一个名为 static 的文件夹就行了。 
# 静态文件一般位于应用的 /static 中。 使用特定的 'static' 
# 端点（endpoint）就可以生成相应的 URL

app = Flask(__name__)
@app.route('/')
def index_func():
    return "index"

with app.test_request_context():
    print(url_for('static', filename="demo_5_style.css"))