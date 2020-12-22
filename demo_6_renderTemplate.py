from flask import Flask, render_template, send_file, request

app = Flask(__name__)

index_page = """
    <h1>Static Page</h1>
    <form action="/dynamic" method="get">
        <input type="submit" value="Go">
    </form>

    <h1>Dynamic Page</h1>
    <form action="/dynamic" method="get">
        <input type="submit" value="Go">
    </form>

    <h1>Dynamic Page (With HTTP "Get" method passing param)</h1>
    <form action="/dynamic_param" method="get">
        First Name: <input type="text" name="f_name" id=""><br>
        Last Name: <input type="text" name="l_name" id=""><br>
        <input type="submit" value="Go">
    </form>
    """


# =======
# 渲染模版
# =======

# 在 Python 内部写 HTML 文件并不简单，你需要自己做 HTML 转义
# Flask 卫东配置了 Jinja2 的模版引擎，HTML 转义的例子如下
# 转义前 escaped_string  = "<p>请在输入框内贴入你需要转换的HTML代码</p> <p>HTML转换工具，可以将HTML代码转换为HTML转义字符串</p> <p>直接将你所要用程序输出的大串HTML代码贴到输入框中，即可一键生成</p> <p>如果您觉得好用，请记得收藏我们的地址！</p>" 
# 转义后 unescape_string = "&lt;p&gt;请在输入框内贴入你需要转换的HTML代码&lt;/p&gt; &lt;p&gt;HTML转换工具，可以将HTML代码转换为HTML转义字符串&lt;/p&gt; &lt;p&gt;直接将你所要用程序输出的大串HTML代码贴到输入框中，即可一键生成&lt;/p&gt; &lt;p&gt;如果您觉得好用，请记得收藏我们的地址！&lt;/p&gt;"

# 你虽然可以使用 Flask APP对象的 send_static_file()       （没有尝试成功）
# 可以返回一个静态的 HTML 文件，但下面的方法更加强大          （没有尝试成功）

# 使用render_template（）的方法渲染模版，
# 提供 模版名称 和 键值对 作为就可以生成网页
# （如果在render_template参数中以key=value形式传入变量，
#   rende_template可以根据传递参数的不同显示不同的内容）


@app.route('/')
def index():
    return index_page

# 1: 简单模版
@app.route('/static')
def render_static():
    # Flask 会在 templates 文件夹中寻找该文件
    # （"path = templates/demo_6_index.html" ）
    return render_template("demo_6_static.html")

# 2. 入参模版
@app.route('/dynamic')
def render_dynamic():
    # 要使用模板，在render_template参数中以key=value形式传入变量，
    # 在html中使用{{key}}来显示传入的变量
    return render_template("demo_6_dynamic.html",  # HTML 模版文件   
        f_name="Simon", l_name="Hamston")  # 刚刚从 GET 请求获得的字段

# 2. 入参模版 (类)
@app.route('/dynamic/classParam')
def remder_dynamic_classParam():
    # 也可以将一个类的实例传过去，然后在模版中访问类的属性
    return render_template("demo_6_dynamic.html")


# （等到学会了Request再回来弄这个）
# # 2. 入参模版
# @app.route('/dynamic', methods=["GET", "POST"])
# def render_dynamic():
#     print(request.form)
#     print("-"*20)
#     input_f_name = request.form["f_name"]   
#     input_l_name = request.form["l_name"]
#     print("="*20)
#     return input_f_name
#     # return render_template("demo_6_dynamic.html",  # HTML 模版文件   
#         # f_name=input_f_name, l_name=input_l_name)  # 刚刚从 GET 请求获得的字段

if __name__ == '__main__':
    app.run()




# 1：简单模版的HTML文件
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <p>请在输入框内贴入你需要转换的HTML代码</p>
#     <p>HTML转换工具，可以将HTML代码转换为HTML转义字符串</p>
#     <p>直接将你所要用程序输出的大串HTML代码贴到输入框中，即可一键生成</p>
#     <p>如果您觉得好用，请记得收藏我们的地址！</p>
# </body>
# </html>

# 2：入参模版的HTML文件
