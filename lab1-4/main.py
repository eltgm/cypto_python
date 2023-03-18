from DESCrypto import DESCrypto

if __name__ == '__main__':
    key = "hahahha"
    md = DESCrypto()
    print('Зашифрованные данные DES: ' + md.encode('hello', key))
    print('Расшифрованные данные: ' + md.decode('0x5c3e79c0f18c5760', key))
