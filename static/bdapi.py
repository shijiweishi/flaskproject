import requests
import json
import base64
from flask import Flask
'''
# 通过AK,SK获取access_token:
def main():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5EMc20CDhFpaAB2SFghdeFVO&client_secret=XPPKmvfePSwoh0gKf8LcMNVqxRzCoFNM"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

if __name__ == '__main__':
    main()

'''
# app = Flask(__name__)

# 通用文字识别（高精度版）
def bdocr(file):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

    # 二进制方式打开图片文件
    f = open(file, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = '24.b92db2d28102fea62d9baf0470b6d0aa.2592000.1683428075.282335-32093637'
    #access_token = "24.df300855408cbbc3892ad0720a86b58d.2592000.1683426088.282335-32093637"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    return response.json()



# 教育场景1:试卷分析与识别
def jyocr(file):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis"
    # 二进制方式打开图片文件
    f = open(file, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img,"language_type":"CHN_ENG","result_type":"big"}
    access_token = '24.b92db2d28102fea62d9baf0470b6d0aa.2592000.1683428075.282335-32093637'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    return response.json()



# 手写文字识别
def writeocr(file):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
    # 二进制方式打开图片文件
    f = open(file, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.b92db2d28102fea62d9baf0470b6d0aa.2592000.1683428075.282335-32093637'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())          # response.json()是字典类型;
        print(type(response.json()))
    return response.json()


# 教育场景2:公式识别

def formulaocr(file):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"
    # 二进制方式打开图片文件
    f = open(file, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.b92db2d28102fea62d9baf0470b6d0aa.2592000.1683428075.282335-32093637'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    return response.json()