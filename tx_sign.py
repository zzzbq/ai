# 本项目为腾讯视频签到
# 其中cookie需要手机端自行签到一次进行抓包，ua最好填上自己抓包的ua
# author:zzzbq
# 本项目是我第一次写签到脚本，仅发送了最简单的get请求，利用正则提取签到获得的积分数值，最终输出出来
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
    "cookie": "RK=QfCdVbXK3u; ptcz=1bca56298bacda1d3d7066a4f85ba973c6f1d1f444d279f3ac7c54c4e69787ad; "
              "tvfe_boss_uuid=81cbad9a6e5533b5; pgv_pvid=1362624744; ied_qq=o2508573704; uin_cookie=o2508573704; "
              "sd_userid=55781616850343897; sd_cookie_crttime=1616850343898; pac_uid=1_2508573704; iip=0; o_cookie=2508573704; "
              "Qs_lvt_323937=1619002353,1621650540; Qs_pv_323937=684741769484475900,281546590864244160; video_guid=2f7f151051aed3d2; "
              "video_platform=2; _tc_unionid=ae26e68c-4ebe-4ef9-8a7e-59d4bc4cc350; pgv_info=ssid=s3056132402; _qpsvr_localtk=0.640452947898787; "
              "main_login=qq; vqq_access_token=0ED84D01F1A2EEE0C7D09B4F38AC1AD8; vqq_appid=101483052; vqq_openid=4C0583A4FDED94DB36E6B00A6BD1FF69; "
              "vqq_vuserid=342247970;",
    "referer": "https://v.qq.com/"
}

z = requests.get(url, headers=headers)
date = z.text
b = re.findall(r'"checkin_score":\s*(\d+)', date)  # 利用正则提取checkin_score内的数值
print('本次运行获得积分' + ''.join(b))
