from Crypto.Cipher import AES

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
