# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 15:54
# @Author  : play4fun
# @File    : combile_cn_eng_subtitle_to_one.py
# @Software: PyCharm

"""
combile_cn_eng_subtitle_to_one.py:
"""
from time import sleep
import pysrt

f1 = '/Users/play/Downloads/Blue.Planet.II.S01E06.WEBRip.x264-RARBG/Subs/2_Eng.srt'
f2 = 'Blue.Planet.II.S01E06.WEBRip.x264-RARBG.srt'

subs = pysrt.open(f1)
subs2 = pysrt.open(f2)

for i, y in enumerate(subs):
    #
    y2 = subs2[i]
    s1 = y2.text.strip()
    sub2 = ' '.join(s1.split('\n'))
    print(sub2)
    #
    print(i, '------')
    s1 = y.text.strip()
    sub = ' '.join(s1.split('\n'))
    print(sub)
    #
    s22 = sub2 + '\n' + '<font size="20px">' + sub + '</font>'
    y.text = s22

# 另存为
subs.save('s06_cn_eng.srt', encoding='utf-8')
