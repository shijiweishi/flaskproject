import base64
import requests
import time
import json
import urllib.request
from flask import Flask,request,jsonify
import os
class Token():
    def __init__(self):
        self.born_time = time.time()
        self.token = self.calculate_token()

    def get_token(self):
        age = time.time() - self.born_time
        expire_time = 28 * 24 * 60 * 60  # 28天
        # expire_time=5#5秒
        if age > expire_time:
            self.token = self.calculate_token()
            self.born_time = time.time()
        return self.token

    def calculate_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=cWaOfCZ8yPdXwElPlk1bfsOv&client_secret=9qG8VmiAd32OBb5w9sCkKGXHYGhknHjl'
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        token = json.loads(bytes.decode(response.read()))
        return token['access_token']

token = Token()


# 此代码加到baidu_ocr文件
def writeocr(file):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
    # 二进制方式打开图片文件
    f = open(file, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = token.get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    return response.json()


# file = r'D:\data\Ocrpic\shouxie2_20230410101823.jpg'
# result = writeocr(file)
# print(result)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# 此代码加到app文件:
#from ocr.baidu_ocr import writeocr
@app.route("/writeocr",methods=["GET","POST"])
def name_stu_ocr():
    # 1、接受from格式传参
    # name = request.form.get("name")
    # age = request.form.get("age")

    # 2、传参用json格式，接受也用json
    # name = request.json.get("name")
    # age = request.json.get("age")

    url = request.json.get("url")
    path = r'D:\data\pic'
    # 判断目录是否存在，如果不存在建立目录
    if not os.path.exists(path):
        os.mkdir(path)

    r = requests.get(url)
    r.raise_for_status()

    # file1是图片保存地址
    file1 = r'C:\data\pic\test.jpg'
    # file2是ocr读取路径
    file2 = r'C:\data\pic\test.jpg'

    # 打开要存储的文件，然后将r.content返回的内容写入文件中，因为图片是二进制格式，所以用‘wb’，写完内容后关闭文件，提示图片保存成功
    with open(file1, 'wb') as f:
        f.write(r.content)
        f.close()
        # print("保存成功")

    data = writeocr(file2)
    # print('data', data)
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
    # print(name, stu)

    # 所有不正常情况都置为''
    try:
        int(stu)
        if len(name) >= 5 or len(name) <= 1:
            raise Exception
    except:
        name = ''
        stu = ''

    result = {
        "name": name,
        "stu": stu
    }
    return jsonify(result)

# 提交到github,更新测试
