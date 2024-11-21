from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64

# 初始化參數
data = "12345678".encode('utf-8')  # 明文
key = b'12345678'  # DES 密鑰 (必須是 8 字節長度)

# DES 加密
cipher = DES.new(key, DES.MODE_ECB)  # ECB 模式
padded_data = pad(data, DES.block_size)  # 填充明文到區塊大小的倍數
encrypted_data = cipher.encrypt(padded_data)

# 將加密結果轉為 Base64 格式
encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
print("加密結果:", encoded_data)
