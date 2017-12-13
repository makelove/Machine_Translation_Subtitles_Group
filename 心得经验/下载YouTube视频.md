##下载YouTube视频
- 参考
    - [Linux 常用工具之 youtube-dl](https://blog.huzhifeng.com/2015/01/28/youtube-dl/)
    - https://github.com/rg3/youtube-dl

- youtube-dl比you-get下载要快！！
- 首先得用[Lantern](https://github.com/getlantern/forum)翻墙
- 安装youtube-dl
    - pip install youtube-dl
- 设置代理
    alias yd="youtube-dl --proxy http://127.0.0.1:1080"
- 下载
    - 同时下载视频和中文字幕,720p:-f 22
        - youtube-dl -f 22 --write-auto-sub --sub-lang zh-Hans https://www.youtube.com/watch?v=Rl77FVobxVI
    - 只下载中文字幕
        - youtube-dl --write-auto-sub  --skip-download   --sub-lang zh-Hans https://www.youtube.com/watch?v=Rl77FVobxVI
- 转换vtt字幕为srt
    - ffmpeg -i The\ farming\ robots\ of\ tomorrow\ are\ here\ today\ _\ The\ Future\ IRL-Rl77FVobxVI.zh-Hans.vtt farm.srt
- 合并字幕到视频里
    - ffmpeg -i ../The\ farming\ robots\ of\ tomorrow\ are\ here\ today\ -\ The\ Future\ IRL.mp4 -vf subtitles=farm.srt farm.mp4    