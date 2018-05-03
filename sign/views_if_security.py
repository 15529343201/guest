import time, hashlib
from django.http import JsonResponse


# 用户签名+时间戳
def user_sign(request):
    if request.method == 'POST':
        client_time = request.POST.get('time', '')  # 客户端时间戳
        client_sign = request.POST.get('sign', '')  # 客户端签名
    else:
        return "error"
    if client_time == '' or client_sign == '':
        return "sign null"
    # 服务器时间
    now_time = time.time()  # 1466426831
    server_time = str(now_time).split('.')[0]
    # 获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return "timeout"
    # 签名检查
    md5 = hashlib.md5()
    sign_str = client_time + "&Guest-Bugmaster"
    sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    sever_sign = md5.hexdigest()
    if sever_sign != client_sign:
        return "sign error"
    else:
        return "sign right"


# 添加发布会接口---增加签名+时间戳
def add_event(request):
    sign_result = user_sign(request)  # 调用签名函数
    if sign_result == "error":
        return JsonResponse({'status': 10011, 'message': 'request error'})
    elif sign_result == "sign null":
        return JsonResponse({'status': 10012, 'message': 'user sign null'})
    elif sign_result == "timeout":
        return JsonResponse({'status': 10013, 'message': 'user sign timeout'})
    elif sign_result == "sign error":
        return JsonResponse({'status': 10014, 'message': 'user sign error'})
