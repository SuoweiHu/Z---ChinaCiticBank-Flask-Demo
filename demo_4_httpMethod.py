from flask import Flask, request

app = Flask(__name__)


# =======
# HTTP 请求方法(route('/',methods=['GET','POST']))
# =======

# Web应用会通过不同的HTTP方法发送请求（不同的HTTPo方法处理URL）
# 当缺省时，一个路由只会响应GET请求。若要设置Flask响应POST请哦求
# 则需要用route（）装饰器的method参数来处理不同的HTTP方法


# Form from W3C: 
#   https://www.w3schools.com/tags/att_form_method.asp
index_page = """
    <h2>GET FORM</h2>
    <form action="/login" method="get">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname"><br><br>
    <input type="submit" value="Submit">
    </form>
    <br><hr><br>
    <h2>POST FORM</h2>
    <form action="/login" method="post">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname"><br><br>
    <input type="submit" value="Submit">
    </form>
    <br><hr><br>
    <h2>HEAD FORM</h2>
    <form action="/login" method="head">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname"><br><br>
    <input type="submit" value="Submit">
    </form>
    <br><hr><br>
    <h2>OPTION FORM</h2>
    <form action="/login" method="option">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname"><br><br>
    <input type="submit" value="Submit">
    </form>
    <br><hr><br>

    &lt;p&gt;请在输入框内贴入你需要转换的HTML代码&lt;/p&gt; &lt;p&gt;HTML转换工具，可以将HTML代码转换为HTML转义字符串&lt;/p&gt; &lt;p&gt;直接将你所要用程序输出的大串HTML代码贴到输入框中，即可一键生成&lt;/p&gt; &lt;p&gt;如果您觉得好用，请记得收藏我们的地址！&lt;/p&gt;
    """

# 初始页面（要体验实例请先访问这个页面）
@app.route('/')
def index_func():
    return index_page
    
# Method参数来处理不同的HTTP方法
# （如果添加了处理GET方法的修饰起，Flask会自动添加HEAD方法支持，OPTION也会自动实现）
@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if(request.method == 'POST'):
        return "POST METHOD DETECTED"
    elif(request.method == 'GET'):
        return "GET METHOD DETECTRED"