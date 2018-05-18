# -*- coding:utf-8 -*-

from Crypto.Cipher import AES
import json
import requests
import time
import base64
import random

class WangYi_MC(object):
    """
    网易云音乐
    """
    def __init__(self):
        self.USER_AGENT_LIST = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        ]
        user_agent = random.choice(self.USER_AGENT_LIST)

        self.headers = {
                'Accept':"*/*",
                'Accept-Encoding':"gzip, deflate",
                'Accept-Language':"zh-CN,zh;q=0.8",
                'Connection':"keep-alive",
                'Content-Length':"416",
                'Content-Type':"application/x-www-form-urlencoded",
                'Cookie':"vjuids=-8edb2aa8.161f46f5255.0.f58af4ffdc876; _ntes_nnid=53319e4cbf94ac2d28da22921a87b269,1520224391775; __gads=ID=df17e102a6101908:T=1520224401:S=ALNI_MY4XYyRebzRfi-Z5DGc1y3OGhrYGQ; _ntes_nuid=53319e4cbf94ac2d28da22921a87b269; __f_=1521088528182; UM_distinctid=16247d130f6ca1-0838f32ae68b3d-454c062c-1fa400-16247d130f7d81; vjlast=1520224392.1521623315.13; vinfo_n_f_l_n3=9da00de2d1aec9bc.1.1.1520224442091.1520224596041.1521623472288; mail_psc_fingerprint=913e54e2ff4077e3bd41fd9c9d09de21; _iuqxldmzr_=32; usertrack=ezq0pVrdTndEdk8mBBQfAg==; _ga=GA1.2.1281668850.1524452989; Province=1000; City=1000; __utmc=94650624; WM_TID=cJ1f7JtsijrzG43rKF1FK41JklB8jVJ6; __utmz=94650624.1526620611.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; NTES_SESS=w86bIYCnN3NUOcIbChCLVXkkWRvHZtHmDUGJMrLduTUeUGQvUZBPoChtjkeaTE8gEyd7n3Rw.bEbMOJ1FyuPIunyEruxxjIgod14JXtIdWDfSCAr9I9xy50SVks1_DPzuaeYkWNtJSTdvj2iHvKNOZ.o_3U9PbudcRWY4qPwz890bY3yK0XAnfCn91Wy1RzRI0n6IMh4ie5J8_hUSDfJJheZP5tGy0eF3; S_INFO=1526623153|0|3&80##|m13273023501_2; P_INFO=m13273023501_2@163.com|1526623153|0|mail163|00&99|US&1526534946&mail163#zhj&330100#10#0#0|132501&1|urs&mail163|13273023501@163.com; MUSIC_EMAIL_U=025664d32f3fd4916f06eed6a56898d899dcb9d14e06692f94e768c8dfe79cf9ea0a626b2a8e85751b627d98bb94c4c205f4ed456633e5f483ea7e982d455e74c3061cd18d77b7a0; BOX_DISABLE=true; playliststatus=visible; JSESSIONID-WYYY=54KCO%2Bdyg%2FJXg%2F%2FgDSbMk%2BMcRJK5nATgZoWW%5C2HZCrcftYXfFHoH8rEShr%2B6DMeQ4WeCjRdyqCF7u9oXIS%2F8YBn52vYMSjFkBMkfPstA5jud6Nleh7lv8Iy29OXbz%2FT52FJ1XBMfSP4XW3CpB7ldY70HpxSA10Q0H7eyE5jsBaI%5C0P46%3A1526625442106; __utma=94650624.1281668850.1524452989.1526620611.1526623796.3; __utmb=94650624.11.10.1526623796",
                'Host':"music.163.com",
                'Origin':"http://music.163.com",
                'Referer':"http://music.163.com/",

        }
        self.headers['User-Agent'] = user_agent
        self.item = {}
        self.item_list = []

        # 设置代理服务器
        self.proxies= {
            'http:':'http://127.0.0.1',
            'https:':'https://127.0.0.1'
        }

        self.url = 'http://music.163.com//weapi/v1/resource/comments/R_SO_4_516076896?csrf_token=90e04572eb42b040167323ec2fcdd79f'
        # 第二个参数
        self.second_param = "010001"
        # 第三个参数
        self.third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        # 第四个参数
        self.forth_param = "0CoJUm6Qyw8W8jud"
        
    def start_page(self):
        """抓取评论"""
        params = self.get_params(1)
        encSecKey = self.get_encSecKey()
        json_text = self.get_json(params, encSecKey)
        json_dict = json.loads(json_text)
        comments_num = int(json_dict['total'])
        if (comments_num % 20 == 0):
            page = comments_num / 20
        else:
            page = int(comments_num / 20) + 1
        print("共有%d页评论!" % page)
        
        for i in range(page):  # 逐页抓取
            print '当前%s页' % i
            params = self.get_params(i + 1)
            encSecKey = self.get_encSecKey()
            json_text = self.get_json(params, encSecKey)
            json_dict = json.loads(json_text)

            if i == 0:
                print("共有%d条评论!" % comments_num)  # 全部评论总数

            for item in json_dict['comments']:
                # 评论内容
                self.item[u'comment'] = item['content']
                # 点赞总数
                self.item[u'likedCount'] = item['likedCount']
                # 评论时间(时间戳)
                self.item[u'comment_time'] = item['time']
                # 评论者id
                self.item[u'userID'] = item['user']['userId']
                # 昵称
                self.item[u'nickname'] = item['user']['nickname']
                # 头像地址
                self.item[u'avatarUrl'] = item['user']['avatarUrl']
                self.item_list.append(self.item)

            print("第%d页抓取完毕!" % (i+1))
        self.write_page()

    def write_page(self):
        aa = json.dumps(self.item_list)
        with open('纸短情长.json', 'a+') as f:
            f.write(aa)
        print("写入文件成功!")

    def get_params(self,page):
        """获取页数,page为传入的页数"""
        iv = "0102030405060708"
        first_key = self.forth_param
        second_key = 16 * 'F'
        if (page == 1):
            # offset的取值为:(评论页数-1)*20,total第一页为true，其余页为false
            # first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}' # 第一个参数
            first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
            h_encText = self.AES_encrypt(first_param, first_key, iv)
        else:
            offset = str((page - 1) * 20)
            first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'false')
            h_encText = self.AES_encrypt(first_param, first_key, iv)
        h_encText = self.AES_encrypt(h_encText, second_key, iv)
        return h_encText

    def AES_encrypt(self,first_param,first_key,iv):
        """解密过程"""
        pad = 16 - len(first_param) % 16
        text = first_param + pad * chr(pad)
        encryptor = AES.new(first_key, AES.MODE_CBC, iv)
        encrypt_text = encryptor.encrypt(text)
        encrypt_text = base64.b64encode(encrypt_text)
        return encrypt_text

    def get_encSecKey(self):
        """获取encSecKey值"""
        encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
        return encSecKey

    def get_json(self,params,encSecKey):
        """获取评论数据(json)"""
        data = {
            "params": params,
            "encSecKey": encSecKey
        }
        response = requests.post(self.url, headers=self.headers, data=data, proxies=self.proxies)
        return response.content


if __name__ == '__main__':
    start_time = time.time()  # 开始时间
    wangyi = WangYi_MC()
    wangyi.start_page()
    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))
