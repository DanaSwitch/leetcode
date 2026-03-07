def encode_int(n):
    n = int(n)
    result = []
    
    while True:
        # Take the lowest 7 bits
        byte = n & 0x7F
        n >>= 7
        if n > 0:  # 还有数字, 最高位拼1
            byte |= 0x80
        result.append(byte)
        if n == 0:  # 没有数字, 直接结束
            break

    return ''.join(f'{b:02X}' for b in result)

n = input().strip()
print(encode_int(n))