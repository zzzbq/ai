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
    "Cookie": "app_ver=8.4.55.25539; call_type=1; ctime=1646480038000; "
              "guid=b8cb3a4fc96111ea981ca0424b63310a; isDarkMode=0; main_login=qq; "
              "pgv_pvid=9731473475; plat_bucketid=50400; "
              "teenGuardSessionCode=19EAA8B4D12AC3AE17EF93D6C4ED6E2B2BAE519B43E1D398517E29355A42880DE156A3A9B9883CB5732CC014AF606C5924247AB81B0806D969BB22719A63E04357909EDA8B9EC064E303D0D13B67238C6166FC5C1CA9625533C03B3053A9418838A0AFDD909928831570A372; "
              "us_stamp=1646480004000; usid=1646480004000165; ussn=1614586979000322; vdevice_qimei36=ff2374fc59fb302070880dbb000017514808; "
              "video_appid=1000005; video_omgid=39653be5dcc4c14833d94bbccfc1078602550010115613; video_platform=5; "
              "vqq_access_token=A3CA03B85BE65225C4A0735C4DA81858; vqq_appid=101795054; vqq_openid=D542A6BA2AF0BA0799DF784DA8D351B6; "
              "vqq_vuserid=342247970; vqq_vusession=jWJtJO_cmTOoWXRmpkLygQ..; zdtime=1646480037504; ilive_a2=3d5bef2e52a0cf2bd3c25271de9f13c6f852a682d56097136f127a763615cbffa096fec5be4b309e80d16bf748db4fa364eb263b52fd25b358a223686dd48843592b1a8a4265fa62; "
              "ilive_tinyid=144115225431839312; ilive_uid_type=0; ilive_uin=4350970381; originalId=342247970; originalKey=oaZMx7GFMqSEgJdaivZERQ..; "
              "original_auth_appid=101860969; original_id_type=1; original_key_type=37; __client_type=16529; "
              "ilive_deviceID=91B91995-4770-4F34-9F4B-9E3FBD476EA0; versioncode=10902; versionname=1.9.2.62; "
              "mobileUV=1_175ce7dff74_9351f; video_guid=36eb98ed41c8b9d0; tvfe_boss_uuid=c66bcc708a9b5de2",
    "Host": "vip.video.qq.com",
    "Referer": "https://film.qq.com/x/autovue/grade/?jump_level=3&aid=V0$$1:0$2:7$3:8.4.55.25539$4:0$8:14$9:100199$12:&isDarkMode=0&uiType=REGULAR",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A465 QQLiveBrowser/8.4.55 AppType/UN WebKitCore/WKWebView iOS GDTTangramMobSDK/4.370.6 GDTMobSDK/4.370.6 cellPhone/iPhone 11",
}

z = requests.get(url,headers=headers)
date = z.text
b = re.findall(r'"checkin_score":\s*(\d+)', date)#  利用正则提取checkin_score内的数值
print('本次运行获得积分'+''.join(b))