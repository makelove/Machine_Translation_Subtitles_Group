# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 13:12
# @Author  : play4fun
# @File    : subtitle_translate1.py
# @Software: PyCharm

"""
subtitle_translate1.py:
"""
import os, sys
from translate_api import translate
# from youdao_translate_api import translate
from googletrans import Translator

translator = Translator()

from time import sleep
import pysrt
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print('srt_path')
    sys.exit(-1)

# p_path='/Users/play/Downloads/Justice.League.Action.S01E46.Party.Animal.720p.WEB-DL.x264.AAC/'
# srt_file='Justice.League.Action.S01E46.Party.Animal.720p.WEB-DL.x264.AAC.srt'
# srt=open(srt_path)
# path=os.path.abspath(srt_path)
# #
# srt_path.split('/')
# path=os.path.join(p_path,srt_file)
path = sys.argv[1]
if not path.endswith('.srt'):
    print('not srt !')
    # os._exit(-1)
    sys.exit(-1)

# subs = pysrt.open('/Users/play/Downloads/blue.planet.ii.s01.e07.episode.1.7.(2017).dut.1cd.(7177066)/Blue Planet II -7- Our Blue Planet. nl.srt')
# subs = pysrt.open('/Users/play/Downloads/Blue.Planet.II.S01E06.WEBRip.x264-RARBG/Subs/2_Eng.srt')
# subs = pysrt.open('/Users/play/Movies/t1/1.srt')
subs = pysrt.open(path)

# for i,y in enumerate(subs[0:100]):
for i, y in enumerate(subs):
    print(i, '------')
    s1 = y.text.strip()
    sub = ' '.join(s1.split('\n'))

    soup = BeautifulSoup(sub, 'lxml')
    sub = soup.get_text()
    print(sub)

    # 翻译
    if sub.strip() == '':
        continue

    # continue
    try:
        # tran = translate(sub, froml='en')
        tran = translate(sub, froml='spa')
        # t = translator.translate(sub, src='en', dest='zh-cn')
        # t = translator.translate(sub, src='es', dest='zh-cn')#spanish
        # tran = t.text
    except Exception as e:
        print('Exception:', e)
        continue
    print('---翻译:', tran)
    y.text = tran

    #
    sleep(1)

# 另存为
# out='/Users/play/Movies/t1/2.srt'
out = path[:-4] + '-cn' + path[-4:]
subs.save(out, encoding='utf-8')
print('另存为', out)
