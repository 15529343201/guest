from Crypto.Cipher import AES

# 加密
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
print(ciphertext)

# 解密
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
s = obj2.decrypt(ciphertext)
print(s)
