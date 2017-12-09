# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 15:54
# @Author  : play4fun
# @File    : combile_cn_eng_subtitle_to_one.py
# @Software: PyCharm

"""
combile_cn_eng_subtitle_to_one.py:

运行：
python /Users/play/github/Machine_Translation_Subtitles_Group/src/combile_cn_eng_subtitle_to_one.py ./Ch4.The.Mega.Brothel.720p.HDTV.x264.AAC.MVGroup.org.srt ./Ch4.The.Mega.Brothel.720p.HDTV.x264.AAC.MVGroup.org-cn.srt

另存为 ./Ch4.The.Mega.Brothel.720p.HDTV.x264.AAC.MVGroup.org-中文-英文.srt
"""
from time import sleep
import pysrt, sys

if len(sys.argv) < 2:
    print('eng_srt cn_srt')
    sys.exit(-1)

# f1 = '/Users/play/Downloads/Blue.Planet.II.S01E06.WEBRip.x264-RARBG/Subs/2_Eng.srt'
# f2 = 'Blue.Planet.II.S01E06.WEBRip.x264-RARBG.srt'
f1 = sys.argv[1]
f2 = sys.argv[2]
if not f1.endswith('.srt') or not f2.endswith('.srt'):
    print('not srt !')
    # os._exit(-1)
    sys.exit(-1)
color = sys.argv[3]  # TODO

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
    s22 = sub2 + '\n' + '<font color="blue" size="20px">' + sub + '</font>' #只能是20px，因为FFmpeg合并字幕和视频时，20px是最合适的
    y.text = s22

# 另存为
# subs.save('s06_cn_eng.srt', encoding='utf-8')

out = f1[:-4] + '-中文-英文' + f1[-4:]
print('另存为', out)
subs.save(out, encoding='utf-8')
