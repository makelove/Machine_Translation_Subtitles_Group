# 下载字幕网站
- 写爬虫
    - 抓取-字幕库https://www.zimuku.la/
    
    
```python
#scrapyshellpc https://www.zimuku.cn/
response.xpath('//td[@class="first"]/a/@title')
for href in response.xpath('//td[@class="first"]/a/@href').extract():
    url=response.urljoin(href)
    print(url)
    
#scrapyshellpc https://www.zimuku.cn/detail/102286.html
In [2]: response.xpath('//a[@id="down1"]/@href').extract_first()
Out[2]: 'http://www.subku.net/dld/102286.html'
     
# scrapyshellpc http://www.subku.net/dld/102286.html
In [3]: response.xpath('//a[@rel="nofollow"]/@href').extract()
Out[3]:
['http://www.subku.net/download/MTAyMjg2fDc4NTZjZmY5NGM2NDdkYWIzZTYzMTc1ZXwxNTIyNjc1MjgyfGQ1NjVkNzUyfHJlbW90ZQ%3D%3D/svr/dx1',
 'http://www.subku.net/download/MTAyMjg2fDc4NTZjZmY5NGM2NDdkYWIzZTYzMTc1ZXwxNTIyNjc1MjgyfGQ1NjVkNzUyfHJlbW90ZQ%3D%3D/svr/dx2',
 'http://www.subku.net/download/MTAyMjg2fDc4NTZjZmY5NGM2NDdkYWIzZTYzMTc1ZXwxNTIyNjc1MjgyfGQ1NjVkNzUyfHJlbW90ZQ%3D%3D/svr/lt1',
 'http://www.subku.net/download/MTAyMjg2fDc4NTZjZmY5NGM2NDdkYWIzZTYzMTc1ZXwxNTIyNjc1MjgyfGQ1NjVkNzUyfHJlbW90ZQ%3D%3D/svr/lt2',
 'http://www.subku.net/download/MTAyMjg2fDc4NTZjZmY5NGM2NDdkYWIzZTYzMTc1ZXwxNTIyNjc1MjgyfGQ1NjVkNzUyfHJlbW90ZQ%3D%3D/svr/yd1',
 'http://www.subku.net/download/MTAyMjg2fDc4NTZjZmY5NGM2NDdkYWIzZTYzMTc1ZXwxNTIyNjc1MjgyfGQ1NjVkNzUyfHJlbW90ZQ%3D%3D/svr/yd2']     
```    