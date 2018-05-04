from Crypto.Cipher import AES
from django.http import JsonResponse
import json
from sign.models import Event, Guest
from django.core.exceptions import ObjectDoesNotExist

# =======AES 加密算法===============
BS = 16
unpad = lambda s: s[0: - ord(s[-1])]


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)


def decryptAES(src, key):
    """
    解析 AES 密文
    """
    src = decryptBase64(src)
    iv = b"1172311105789011"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text)


def aes_encryption(request):
    app_key = 'W7v4D60fds2Cmk2U'
    if request.method == 'POST':
        data = request.POST.get("data", "")
    else:
        return "error"
    # 解密
    decode = decryptAES(data, app_key)
    # 转化为字典
    dict_data = json.loads(decode)
    return dict_data


# 嘉宾查询接口----AES 算法
def get_guest_list(request):
    dict_data = aes_encryption(request)

    if dict_data == "error":
        return JsonResponse({'status': 10011, 'message': 'request error'})

    eid = dict_data['eid']
    phone = dict_data['phone']

    if eid == '':
        return JsonResponse({'status': 10021, 'message': 'eid cannot be empty'})
    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status': 200, 'message': 'success', 'data': guest})
