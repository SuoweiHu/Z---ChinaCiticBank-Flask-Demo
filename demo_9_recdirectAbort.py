from flask import Flask, abort, redirect, url_for, render_template, make_response, flash

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# ======
# 重新定向和错误 redirect abort 
# ======

# 如果不用 error_handler(error_code) 定制出错页面
# 在缺省情况下每种出错代码都会对应显示一个黑白的出错页面
# 例如：
#   以下为错误401的页面
#                           Unauthorized
#       The server could not verify that you are authorized 
#       to access the URL requested. You either supplied the 
#       wrong credentials (e.g. a bad password), or your browser 
#       doesn't understand how to supply the credentials required.

# 1.
#  - 简单重新定向
#  - 简单错误
@app.route('/')
def index_func():
    flash("Now redirecting...")
    return "<h1>A</h1>"
    return redirect(url_for('login_func'))
@app.route('/login')
def login_func():
    abort(401)
    print("THIS LINE WILL NEVER BE EXECUTED !")
    return

# 2.
#  - 使用 error_handler(401) 定制出错页面
@app.errorhandler(401)
def page_note_found_error(error):
    # 注意错误函数需要有一个错误入参
    resp = make_response(render_template('demo_9_errorPage.html'), 401)
    return resp
    # render template后面跟着的401 表示错误代码401会作为StatusCode给到浏览器



if __name__ == "__main__":
    app.run()
