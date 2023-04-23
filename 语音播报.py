 # -*- coding: utf-8 -*-

import time
import pyttsx3  # 语音播报库
import datetime


now = datetime.datetime.now()
print(now)

engine = pyttsx3.init()

# 设置要播报的文本
text = '时间到了'

while True:
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min

    now = datetime.datetime.now()
    #print(now)

    # 报时
    if hour == 13 and minute == 0:
        engine.say(text)
        engine.runAndWait()
        time.sleep(5)
    else:
        # 等待1分钟
        now = datetime.datetime.now()
        now_str = now.strftime('现在是：%Y-%m-%d %H:%M:%S')
        print(now_str)
        # engine.say(now_str)
        # engine.runAndWait()
        
        time.sleep(1)







# 设置指定的时间，这里设置为10秒后
# target_time = time.time() + 10


# now = datetime.datetime.now()
# print(now)
# 等待时间到达指定时间
# while time.time() < target_time:
#     time.sleep(0.01)

# 时间到了，播报文本


