from flask import Flask, request, render_template

app = Flask(__name__)

# ========
# 文件上传 (request.files)
# ========

@app.route('/')
def index():
    return render_template('demo_8_fileUpload.html')

# 用 Flask 处理文件上传很容易，只要确保不要忘记在你的 HTML 表单
# 中设置 enctype="multipart/form-data" 属性就可以了。
# 否则浏览器将不会传送你的文件

# 已上传的文件被存在内存或文件系统中的临时位置
# 可以通过请求对象的 files属性访问上传的文件
# （每隔上传的文件都存在files字典属性中，其中的每个文件和python的file对象差不多）


@app.route('/upload', methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        f = request.files.get("stuff_file")
        # filename 提取文件名（但是牢记这个名字可以伪造，不要信任这个值）
        f_name = f.filename
        # 使用 save（）方法可以保存文件
        f.save(f'./src/uploads/{f_name}')
        return "<h2> Upload file is a success !! <h2>"


if __name__ == "__main__":
    app.run()


# 对应的HTML文件
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <form action="/upload" method="post" enctype="multipart/form-data">
#         File upload portal <br>
#         <hr>
#         <input type="file" name="stuff_file"  id=""><br>
#         <input type="submit" value="Upload File">
#     </form>
# </body>
# </html>