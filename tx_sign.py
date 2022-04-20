# 本项目为腾讯视频签到
# 其中cookie需要手机端自行签到一次进行抓包，ua最好填上自己抓包的ua
# author:zzzbq
# 1.谷歌浏览器打开https://v.qq.com;
# 2.登录自己的腾讯视频账号;
# 3.按F12后Filter搜索框左侧选择all，搜索框输入auth，按F5刷新
# 4.cookie删除“vqq_vusession=”以后的内容

import re
import requests

url = "https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_checkin&cmd=2&_=1646480061816&callback=Zepto1646480038503"
headers = {
    "accept": "*/*",
    "accept-Encoding": "gzip, deflate, br",
    "accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie": ""
              "vqq_vuserid=342247970;",
    "referer": "https://v.qq.com/"
}

z = requests.get(url, headers=headers)
date = z.text
b = re.findall(r'"checkin_score":\s*(\d+)', date)  # 利用正则提取checkin_score内的数值
print('本次运行获得积分' + ''.join(b))
