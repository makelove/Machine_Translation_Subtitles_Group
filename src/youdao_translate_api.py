# -*- coding: utf-8 -*-
# @Time    : 2017/12/9 17:30
# @Author  : play4fun
# @File    : youdao_translate_api.py
# @Software: PyCharm

"""
youdao_translate_api.py:
"""
import requests,json

url='http://fanyi.youdao.com/openapi.do?keyfrom=YCTSAPP&key=618284456&type=data&doctype=json&version=1.1&q='


def translate(sub, froml=None, tol='zh'):
    q='+'.join(sub.split())
    url2=url+q
    print(url2)

    rs = requests.get(url2)
    # print(rs.text)
    js = json.loads(rs.text)
    return js['translation'][0]

    q = sub
    if froml is None:
        froml = 'auto'
    # toLang=tol

    sign = appid + q + str(salt) + secretKey
    # m1 = md5.new()
    m1 = md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    myurl = myurl + '?appid=' + appid + '&q=' + quote(q) + '&from=' + froml + '&to=' + tol + '&salt=' + str(salt) + '&sign=' + sign
    # print(myurl)

    #
    rs = requests.get(myurl)
    # print(rs.text)
    js = json.loads(rs.text)
    return js['trans_result'][0]['dst']


def test():
    # sub = 'Zeker, we hebben de verantwoordelijkheid om voor onze blauwe planeet te zorgen.'
    # rs = translate(sub, froml='nl')  # 荷兰
    # sub = 'She must leave the safety of her marine world'
    sub = 'How do I determine why unittest is my only option for a python script? I just want to run the script?'
    rs = translate(sub, froml='en')

    print('翻译结果：', rs)


if __name__ == '__main__':
    test()
