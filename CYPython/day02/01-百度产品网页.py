from http.client import responses

import requests



# 声明爬取的网站地址 <Respons [200]> 表示获取数据成功
url = "https://www.baidu.com/more/"

# 对地址发起请求
response = requests.get(url)
# 一般情况下使用 text
# html = response.text

#对文件进行解码  有的网站编码时gbk，gbk-2321
html = response.content.decode('utf-8')

print(html)

with open("./html/baidu.html","w",encoding="utf-8") as f:
    f.write(html)