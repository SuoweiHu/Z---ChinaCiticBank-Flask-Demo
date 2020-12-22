# -*- coding: utf-8 -*-

from flask import Flask, escape, request

app = Flask(__name__)

# @app.route('/')
# def index():
#     return f"Index Page"

# @app.route('/hello')
# def hello():
#     return f"Hello, World"

# ======
# 变量规则 (route('/user/<username>'))
# =======

# 通过把 URL 的一部分标记为 <variable_name> 就可以在 URL 中添加变量。
# 标记的 部分会作为关键字参数传递给函数。通过使用 <converter:variable_name> ，

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username) # 关于为什么要使用escape转义 https://www.baidu.com/link?url=bHMcu_dHUV6YW3QuTBXvqxPxSA8DCAUOezXLN_rNzq5R4O8P3-qKPadjib0S096YCANl-TXWny0LDKOMN-PdSMfieJu2FHWIKc2gKgInf_u&wd=&eqid=dc3cc1bd005ff1a2000000045fe152ec
    # 这时候如果用户访问了 http://127.0.0.1:5000/user/stuff 这个URL
    # Flask就会返回 "User stuff"


# 可以 选择性的加上一个转换器，为变量指定规则。
# Flask 中参数转换器的类型:
#     - string    （缺省值） 接受任何不包含斜杠的文本
#     - int       接受正整数
#     - float     接受正浮点数
#     - path      类似 string ，但可以包含斜杠
#     - uuid      接受 UUID 字符串

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    # 这时候如果用户访问了 hhttp://127.0.0.1:5000/post/123 这个URL
    # Flask就会返回 "Post 123"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
    # 127.0.0.1:5000/path/C://user/suowei/flask
    # Subpath C://user/suowei/flask





@app.route('/projects/')
def projects():
    return 'The project page' # 此时如果访问/projects会被Flask重新定向到/projects/

@app.route('/about')
def about():
    return 'The about page'