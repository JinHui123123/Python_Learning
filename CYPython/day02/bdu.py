
import requests

url = "https://www.baidu.com/s"

headers = {
    # 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-encoding' :'gzip, deflate, br, zstd',
    # 'accept-language' :'zh-CN,zh;q=0.9',
    # 'cache-control'  : 'max-age=0',
    # 'connection ': 'keep-alive',
    "Cookie": "BAIDUID=674A5F2E7286BDEB481F7549E947D633:FG=1; BAIDUID_BFESS=674A5F2E7286BDEB481F7549E947D633:FG=1; Hm_lvt_9f14aaa038bbba8b12ec2a4a3e51d254=1778074246,1778162672; Hm_lpvt_9f14aaa038bbba8b12ec2a4a3e51d254=1778162672; HMACCOUNT=D204A102B54EF68A; BIDUPSID=674A5F2E7286BDEB481F7549E947D633; PSTM=1778162685; H_PS_PSSID=67602_67861_68165_68297_68735_69000_69063_69163_69181_69201_69227_69245_69241_69231_69234_69292_69296_69251_69402_69396_69418_69412_69422_69432_69439_69457_69343_69339_69347_69345_69349_69351_69340_69502_69518_69554_68486_69584_69590_69613_69622_69669_69664_69661_69683_69718_69738_69745_69771_69798_69780_69807_69835; delPer=0; BD_CK_SAM=1; PSINO=7; BD_UPN=12314753; H_PS_645EC=d702uWPUoTP9d3eWZsayEMD11aEnCXXU6Vg5oYFRmPqp5IJ54cI2Eac73Uk; BA_HECTOR=2025a08lah0hak8k21a404al8gag8i1kvp6vv26; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=QR9MybZjkBQalyekoP5ohnFd9x:BUwCcKhohi5XMSNQ8:C; channel=baidusearch; baikeVisitId=7996f771-6044-49d9-bf72-af8dfdfcaa42",
    # 'host' : 'www.baidu.com',
    'referer' : 'https://www.baidu.com/more/',
    # 'sec-ch-ua' : '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    # 'sec-ch-ua-mobile' : '?0',
    # 'sec-ch-ua-platform' : '"Windows"',
    # 'sec-fetch-dest' : 'document',
    # 'sec-fetch-mode' : 'navigate',
    # 'sec-fetch-site' : 'same-origin',
    # 'sec-fetch-user' : '?1',
    # 'upgrade-insecure-requests' : '1',
    "User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

data = {
    "bs":"lv",
    "f":"8",
    "rsv_bp":"1",
    "rsv_spt":"3",
    "wd":"米哈游",
    "inputT":"1712"
}



response = requests.post(url,data=data,headers=headers)
print(response.content.decode(encoding="utf-8"))

