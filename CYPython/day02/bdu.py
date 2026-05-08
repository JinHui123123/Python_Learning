import requests

url = "https://www.baidu.com/s"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-encoding': 'gzip, deflate, br, zstd',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # 'cache-control': 'max-age=0',
    # 'connection': 'keep-alive',
    # "cookie":"BIDUPSID=4B384A38AD7DCF2F9E791FA5EE2741EE; PSTM=1778209044; H_PS_PSSID=60272_63142_67862_68166_68297_68739_69001_69071_69155_69175_69204_69242_69229_69241_69230_69236_69295_69251_69397_69417_69412_69423_69443_69432_69452_69342_69339_69347_69344_69349_69351_69341_69491_69499_69517_69558_69554_69591_69581_69614_69666_69663_69659_69671_69735_69719_69745_69767_69797_69778_69712_69808_69836; BAIDUID=4B384A38AD7DCF2F9E791FA5EE2741EE:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=68fasKPVYXmVRxBo4krsvfRE%2BOhEB3fZ4Tp4oz7499wdy0eub3Z1fvEu3M0; BA_HECTOR=a12g2ga0252hagak8h002h2l252la31kvqkdi26; BAIDUID_BFESS=4B384A38AD7DCF2F9E791FA5EE2741EE:FG=1; ZFY=M:AohfiEiiLq9CaStEqB1EpyzVbXh2xMBMQPP5SozDYo:C; baikeVisitId=8957fd57-f0e8-4135-a37d-4c5ccec6f45e",
    # 'host': 'www.baidu.com',
    # 'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'document',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',   # 修正拼写
    # Cookie 可以保留，但注意隐私和有效性
}

data = {
    # "ie": "lv",
    # "f": "8",
    # "rsv_bp": "1",
    # "rsv_idx": "1",
    # "tn": "baidu",
    "wd": "米哈游",
    # "fenlei": "256",
    # "rsv_pg": "0x9b41f1b80048698d",
    # "rsv_t": "cf8bW2lNqw2u61PEK3yr57dPkR5Nx8DWDMyPJkGWpYI84VQRJ+cU62zwiwD6",
    # "rqlang": "en",
    # "rsv_enter": "1",
    # "rsv_dl": "tb_enter",
    # "rsv_sug3": "9",
    # "rsv_sug1": "7",
    # "rsv_sug7": "100",
    # "rsv_btype": "t",
    # "inputT": "1650",
    # "rsv_sug4": "1650"
}

response = requests.get(url,params=data,headers=headers)

html = response.content.decode(encoding='utf-8')

with open('./html/baiduMiHoyo.html','w',encoding='utf-8') as f:
    f.write(html)