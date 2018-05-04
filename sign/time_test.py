import time

# 当前时间戳
now_time = time.time()
print('当前时间戳:' + str(now_time))
# 将时间戳转化为字符串类型,并截取小数点前的时间
print(str(now_time).split('.')[0])
# 转换成日期格式
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))
print('日期格式:' + str(otherStyleTime))
"""
D:\Python35\python3.exe C:/Users/Administrator/git/guest/sign/time_test.py
当前时间戳:1525352026.589537
1525352026
日期格式:2018-05-03 20:53:46
"""