#本项目为腾讯视频签到
#其中cookie需要手机端自行签到一次进行抓包，ua最好填上自己抓包的ua
#author:zzzbq
#本项目是我第一次写签到脚本，仅发送了最简单的get请求，利用正则提取签到获得的积分数值，最终输出出来
#cookie有效期尚未测试

import re
import requests

url = "https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_checkin&cmd=2&_=1646480061816&callback=Zepto1646480038503" \

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-cn",
    "Connection": "keep-alive",
    "Cookie": "    "#此处填写抓包的cookie
    "Host": "vip.video.qq.com",
    "Referer": "https://film.qq.com/x/autovue/grade/?jump_level=3&aid=V0$$1:0$2:7$3:8.4.55.25539$4:0$8:14$9:100199$12:&isDarkMode=0&uiType=REGULAR",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A465 QQLiveBrowser/8.4.55 AppType/UN WebKitCore/WKWebView iOS GDTTangramMobSDK/4.370.6 GDTMobSDK/4.370.6 cellPhone/iPhone 11",
}

z = requests.get(url,headers=headers)
date = z.text
b = re.findall(r'"checkin_score":\s*(\d+)', date)#  利用正则提取checkin_score内的数值
print('本次运行获得积分'+''.join(b))
