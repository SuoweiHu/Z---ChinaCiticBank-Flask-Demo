from flask import Flask


# 创建一个Flask类的实例,构造器使用参数如下:
#   1. 应用模块/包的名称(这里使用一个单一模块所以使用__name__)
app = Flask(__name__)

# 使用 Route 装饰器告知 Flask 触发函数的URL(注册触发函数的URL)
# 函数将会由 http://127.0.0.1:5000/ 触发
@app.route('/')
def hello_world():
    return f'Hello, World!' #函数最后返回需要在用户浏览器中显示的信息。

# 注册触发函数的URL
# 函数将会由 函数将会由 http://127.0.0.1:5000/ 触发 触发
@app.route('/name')
def print_name():
    name = "Simon"
    return f'Hello {name} !'


# 运行该Flask应用
# MAC (Flask)
#   export FLASK_APP=hello.py   # 在 FLASK_APP 环境变量中储存的是模块的名称
#   flask run                   # 运行该 Flask 应用
# MAC (Python)
#   export FLASK_APP=hello.py
#   python -m flask run
# WIN (Command Prompt)
#   C:\path\to\app>set FLASK_APP=hello.py
# WIN (Power Shell)
#   PS C:\path\to\app> $env:FLASK_APP = "hello.py"
#
# 应该得到的返回
#   Running on http://127.0.0.1:5000/



# 内部可见服务器: 刚刚的方法就创建了一个内部的,可用于测试,但是网络中的其他电脑并不可见
# 外部可见服务区: 如果你关闭了调试器或信任你网络中的用户，那么可以让服务器被公开访问。 只要在命令行上简单的加上 --host=0.0.0.0 即可:
#               flask run --host=0.0.0.0 这行代码告诉你的操作系统监听所有公开的 IP 。
