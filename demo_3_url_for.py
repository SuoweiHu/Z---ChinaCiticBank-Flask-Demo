# -*- coding: utf-8 -*-\
from flask import Flask, escape, url_for

# =======
# URL 构建 (url_for)
# =======

# url_for 函数用于构建制定函数的URL，第一个参数为函数名字
# 还可以接受任意数量的关键词参数，每个对应URL中的变量（未知变量将被添加到URL中作为查询参数）

# 为什么？ （比起硬编码进模版的URL）
#  1. 使用反转函数 url_for() 动态构建的的 URl 可以方便后期维护
# （如果改变了函数注册的触发URL，但是没有改函数名，如果用的是getUrl就不需要到处改URL了）
#  2. url_for()函数会转义一些特殊字符和unicode字符串，这些事情url_for会自动的帮我们搞定。

# 其他原因？ （不理解的）
#  3. 生产路径一般是绝对路径。。。。可以避免绝对路径的副作用？？？？？
#  4. 如果你的Flask应用放在URL跟路径以外的地方URL_FOR可以为你妥善处理额 ？？？？？

# 新建一个Flask实例,并命名为当前主线程的名字__main__
app = Flask(__name__)

# 使用route修饰器注册函数index的触发url
@app.route('/')
def index_func():
    return "index"
# 唯一URL
@app.route('/login') 
def login_func():
    return "login"
# 使用变量规则通过URL传递参数给函数
@app.route('/profile/<string:username>')
def profile_func(username):
    return "UsrName {username}".format(username=username)

with app.test_request_context():
    print(url_for('index_func'))
    print(url_for('login_func'))
    print(url_for('profile_func', username='John Doe')) 
    print(url_for('profile_func', username='John Doe', password='123456')) 
    # /
    # /login
    # /profile/John%20Doe
    # /profile/John%20Doe?password=123456






