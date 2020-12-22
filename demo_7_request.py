from flask import Flask, request, render_template
import pprint

app = Flask(__name__)


# =======
# 请求对象（request.args/form）
# ======

# 在 Flask 中，请求对象有全剧对象 request来提供信息

# 0. 登陆主页面
@app.route('/')
@app.route('/index')
def main_page():
    return render_template("demo_7_index.html")


@app.route("/login", methods=["POST","GET"])
def login():
    error = None
    # 1. （POST提交表单数据）
    #  - 通过 request 的 method 属性操作当前请求方法
    #  - 通过 request 的 form 属性处理表单数据
    if request.method == "POST":
        #  (注意：当request.form[]属性 不存在要求的键时 会抛出一个KeyError
        #  如果不捕捉会导致显示一个 HTTP 400 Bad Request 的错误页面,用get方法则可以避免该情况)
        print(f"HTTP POST, form data = {request.form}")
        account  = request.form.get("account")
        password = request.form.get("password")
        return f"Form Received (Method: POST) <hr><br>Account: {account} <br>Password: {password}"

    # 2. （GET提交URL中提交的属性）
    #  - 通过 request 的 args属性操作URL中提交的参数
    elif request.method == "GET":
        print(f"HTTP GET, query param = {request.args}")
        account = request.args.get("account")
        password = request.args.get("password")
        return f"Query Received (Method: GET) <hr><br>Account: {account} <br>Password: {password}"

    else:
        return "Unknwon HTTP Request Method"

if __name__ == "__main__":
    app.run()