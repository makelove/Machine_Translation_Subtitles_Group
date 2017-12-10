# -*- coding: utf-8 -*-
# @Time    : 2017/12/10 16:02
# @Author  : play4fun
# @File    : Google_Translate_API.py
# @Software: PyCharm

"""
Google_Translate_API.py:
https://github.com/ssut/py-googletrans
pip install googletrans
"""
from googletrans import Translator
translator = Translator()

def translate(sub, froml=None, tol='zh-cn'):
    #t=translator.translate('i love you,let us make sex',src='en', dest='zh-cn')
    t=translator.translate(sub,src=froml, dest=tol)

    return t.text