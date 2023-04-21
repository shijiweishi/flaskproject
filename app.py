# 从flask这个包中导入FLASK类;
import json
from flask import Flask,request,jsonify
# from static.bdapi import bdocr
# from static.bdapi import jyocr
# from static.bdapi import writeocr
# from static.bdapi import formulaocr
from static.bdapi import *
import os
import requests

# 使用FLASK类创建一个app对象;
# __name__表示app.py这个模块
# name的两个作用:
# 1、以后出现bug,可以帮助我们快速定位;2、对于寻找模板文件,有一个相对路径;

app = Flask(__name__)

# jsonify返回unicode编码;flask 的默认配置中使用的是ascii编码,在创建flask app时,关闭ascii编码方式.
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World 感恩的心, 感谢命运, 让我们荡起双桨'

@app.route('/profile')
def profile11():  # put application's code here
    return '个人中心'

@app.route('/profile/scde')
def profile12():  # put application's code here
    return '个人中心,sss'

# 带参数的url:将参数固定到了path中
@app.route('/blod/<id>')
def profile13(id):  # put application's code here
    return '访问的博客id是: {}'.format(id)

#查询字符串的方式传参
# /book/list:会给我返回第一页的数据# /book/list?page=2:获取第一页的数据
@app.route('/book/list')
def profile14():  # put application's code here
    page = request.args.get("page",default=1,type=int)
    return f'获取的是第{page}本书本'

@app.route('/success',methods=['GET'])
def profile22():  # put application's code here
    result_message = {
        "success": False,
        "message": "有公式识别失败",
        "texs": None
    }
    return jsonify(result_message)

@app.route('/getfile',methods=['GET'])
def getfile():  # put application's code here
    file = request.files['file']
    print(file)
    return jsonify(file)


@app.route("/sd", methods=[ "POST"])
def sd():
    if request.method == "POST":
        # 这样获取就可以了
        json_data = request.json
        return jsonify(json_data)


#构造post请求
@app.route("/login",methods=["GET","POST"])
def login():
    # 1、接受from格式传参
    # name = request.form.get("name")
    # age = request.form.get("age")

    # 2、传参用json格式，接受也用json
    name = request.json.get("name")
    age = request.json.get("age")

    # 3、request.get_data() 是获取发送post请求携带的请求参数
    data = request.get_data()
    print(data, type(data))
    data1 = json.loads(data)
    print(data1, type(data1))

    result = {
        '传进名字':name,
        "传入年龄":age
    }
    return jsonify(result)


# 构造post请求
@app.route("/writeocr", methods=["GET", "POST"])
def name_stu_ocr():
    # 1、接受from格式传参
    # file = request.form.get("name")

    # 2、传参用json格式，接受也用json
    url = request.json.get("url")

    path = r'D:\data\pic'
    # 判断目录是否存在，如果不存在建立目录
    if not os.path.exists(path):
        os.mkdir(path)

    r = requests.get(url)
    r.raise_for_status()

    # file1是图片保存地址;后缀jpg,png都可以
    file1 = r'D:\data\pic\test.jpg'

    # file2是ocr读取路径
    file2 = r'D:\data\pic\test.jpg'
    file2 = r'D:\data\Ocrpic\学号姓名11.jpg'

    # 打开要存储的文件，然后将r.content返回的内容写入文件中，因为图片是二进制格式，所以用‘wb’，写完内容后关闭文件，提示图片保存成功
    with open(file1, 'wb') as f:
        f.write(r.content)
        f.close()
        print("保存成功")

    data = writeocr(file2)
    print('data',data)
    # words_result是包含位置和内容的字典组成列表
    words_result = data['words_result']
    # ocr识别出来的所有字符串放在一个列表word_list;
    word_list = []
    for data in words_result:
        word_list.append(data['words'])
    name = ''
    stu = ''
    for i, data in enumerate(word_list):
        if data == '姓名:' or data == '姓名：' or data == '姓名':
            name = word_list[i + 1]
        if data == '考号:' or data == '考号：' or data == '考号' or data == '考生号:' or data == '考生号：' or data == '考生号' or data == '准考证号:' or data == '准考证号：' or data == '准考证号':
            stu = word_list[i + 1]
    print(name,stu)

    # 所有不正常情况都置为''
    try:
        int(stu)
        if len(name) >= 5 or len(name) <= 1:
            raise Exception
    except:
        name = ''
        stu = ''

    result = {
        "姓名": name,
        "学号": stu
    }
    return jsonify(result)


@app.route('/ocr')
def ocr_recongize():
    # file = r'D:\data\Ocrpic\0230407103539.jpg'
    file = r'D:\data\Ocrpic\学号姓名1.jpg'
    #file = 'D:\data\Ocrpic\math_20230410110432.png'
    #file = 'D:\data\Ocrpic\数学整卷_20230410140822.jpg'
    # 网络图片路径问题处理:
    result = writeocr(file)
    #result = jyocr(file)
    #result = bdocr(file)
    #result = formulaocr(file)
    # return '{}'.format(result)
    # jsonify返回unicode编码;
    return jsonify(result)


if __name__ == '__main__':
    app.run()


# 修改host就是让其他电脑访问
# 在flask中使用日志输出:app.logger.info('!!!!!!')1