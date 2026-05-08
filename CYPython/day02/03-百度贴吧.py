import requests

class Tieba:
    def __init__(self,page):
        # 爬取的页面个数
        self.page = page
        self.url = "https://tieba.baidu.com/f"
        self.run()

    def run(self):
        i = 0 # i 从0-4
        while i < self.page:
            payload = {
                "kw":"mhy",
                "ie":"utf-8",
                "pn": i * 50
            }
            headers = {
               # 'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.7',
               #  'cookie': 'BAIDUID=674A5F2E7286BDEB481F7549E947D633:FG=1; BAIDUID_BFESS=674A5F2E7286BDEB481F7549E947D633:FG=1; BIDUPSID=674A5F2E7286BDEB481F7549E947D633; PSTM=1778162685; BA_HECTOR=2025a08lah0hak8k21a404al8gag8i1kvp6vv26; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=QR9MybZjkBQalyekoP5ohnFd9x:BUwCcKhohi5XMSNQ8:C; H_PS_PSSID=67602_67861_68165_68297_68735_69000_69063_69163_69181_69201_69227_69245_69241_69231_69234_69292_69296_69251_69402_69396_69418_69412_69422_69432_69439_69457_69339_69349_69502_69518_69554_68486_69584_69590_69613_69622_69669_69664_69661_69683_69718_69738_69745_69771_69798_69780_69807_69835; delPer=0; PSINO=7; USER_JUMP=-1; BAIDU_WISE_UID=wapp_1778238170865_295; __bid_n=19e074132db2304a0293f9; TIEBAUID=cb23caae14130a0d384a57f1; ab_sr=1.0.1_M2ViNTc1MWJmNzMyNThhMzFkODJiYmQ3OWZlZGFlODgyZmIxNzE1YmEyNDNmNzMwZDhmMzU2ZmZmMWE3M2IwZGNhYzI5OGVjNmE3ZDgyNjU3ODMyMzdjODAyYzVmYmYzYzgxM2MxZjhmOTQ0MTgzNmI3ZjhkZWU5MjU1OTBkYjgzNDg1YWIyNWYyZWE3MjVjZWI5MDcxMjg4ZTRjNjI5Yw==',
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
            }

            response = requests.get(self.url,params=payload,headers=headers)
            html = response.content.decode(encoding="utf-8")
            print(html)

            with open(f"./sina/{i+1}-mhy.html",'w',encoding="utf-8") as f:
                f.write(html)

            i += 1

if __name__ == '__main__':
   Tieba(1)