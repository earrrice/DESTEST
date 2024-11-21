from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# 確保輸入的字符串是有效的十六進制
def validate_hex_string(hex_string):
    try:
        int(hex_string, 16)
    except ValueError:
        raise ValueError(f"{hex_string} 不是一個有效的十六進制字符串")

# 使用 pycryptodome 的 DES 加密
def des_encrypt_with_pycryptodome(data, key):
    # 將數據轉換為字節
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8').ljust(8, b'\x00')[:8]  # 確保密鑰為8字節

    # 創建 DES 加密器
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    
    # 填充明文
    padded_data = pad(data_bytes, DES.block_size)
    
    # 加密
    encrypted_data = cipher.encrypt(padded_data)
    
    # 將加密結果轉換為二進制字符串
    encrypted_hex = binascii.hexlify(encrypted_data).decode('utf-8').upper() 
    return encrypted_hex
# 示例數據和密鑰
data = "113121002"  # 明文
key = "13121002"  # 密鑰

# 調用加密函數
encrypted_bin = des_encrypt_with_pycryptodome(data, key)
print("Encrypted (bin):", encrypted_bin)
