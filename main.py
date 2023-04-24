import os
import math
import random
import requests

from datetime import date, datetime
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate

today = datetime.now()

# 微信公众测试号ID和SECRET
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

# 可把os.environ结果替换成字符串在本地调试
user_ids = os.environ["USER_ID"].split(',')
template_ids = os.environ["TEMPLATE_ID"].split(',')

# 字体随机颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)
wm = WeChatMessage(client)

msg_title = '测试标题'
msg_content = '测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容'

for i in range(len(user_ids)):
    data = {
        "title1": {"value": "{}".format(msg_title), "color":"#A8A8A8"},
	"title2": {"value": "通知内容:\t\t\t\t", "color":"#A8A8A8"},
	"title3": {"value": "通知时间:\t\t\t\t", "color":"#A8A8A8"},
	"title4": {"value": "备注:\t\t\t\t", "color":"#A8A8A8"},
	"content1": {"value": "{}\n".format(msg_content)},
	"content2": {"value": "{}\n".format(today)},
	"content3": {"value":"本次推送由yangqu支持\n"}
    }
    res = wm.send_template(user_ids[i], template_ids[i], data)
    print(res)
    
    try:
    	res1 = wm.send_text(user_ids[i], "打卡成功\n内容1\n内容2")
    except WeChatClientException, e:
    	print e
