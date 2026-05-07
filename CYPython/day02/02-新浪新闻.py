import requests

url = "https://search.sina.com.cn/news"

headers = {
# ':authority':'search.sina.com.cn',
# ':method' : 'GET',
# ':path' :'/search?q=%E7%B1%B3%E5%93%88%E6%B8%B8&tp=news&sort=0&page=1&size=10&from=search_result',
# ':scheme':'https',
# 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# 'accept-encoding' : 'gzip, deflate, br, zstd',
# 'accept-language': 'zh-CN,zh;q=0.9',
# 'cache-control':'max-age=0',
# 'cookie' : 'UOR=search.sina.com.cn,cj.sina.com.cn,; ULV=1778160169511:1:1:1::; SINAGLOBAL=39.144.191.72_1778160169.827366; Apache=39.144.191.72_1778160169.827368; beegosessionID=0cac40d1ffc8be04c3429761e93da107',
# 'priority' : 'u=0, i',
# 'sec-ch-ua' : '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
# 'sec-ch-ua-mobile' : '?0',
# 'sec-ch-ua-platform' : '"Windows"',
# 'sec-fetch-dest' :'document',
# 'sec-fetch-mode' : 'navigate',
# 'sec-fetch-site' :'same-origin',
# 'sec-fetch-user' : '?1',
# 'upgrade-insecure-requests' : '1',
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
}

data = {
    "q":"米哈游",
    "tp":"news",
    "sort":"0",
    "page":"1",
    "size":"10",
    "from":"index",
}

response = requests.post(url,data=data,headers=headers)

print(response.content.decode(encoding="utf-8"))