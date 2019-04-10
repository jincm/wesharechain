#coding:Utf-8


from Crypto.Cipher import ARC4
import binascii

SECRET_KEY = 'd15d67922dd241cdbfc355d1ab44d6757dc759e60b3c4b74b868704c8a37b897'

def encrypt(plain, key, b2a=binascii.b2a_hex):
    """
    RC4加密不需要补齐操作
    
    :param key: rc4密钥
    :param b2a: binary转ascii函数
    """
    assert isinstance(plain, str)
    assert key and isinstance(key, str)

    if b2a:
        assert callable(b2a)

    _ = ARC4.new(key).encrypt(plain)
    return _ if b2a is None else b2a(_)

    
def decrypt(cipher, key, a2b=binascii.a2b_hex):
    """
    :param a2b: ascii转binary函数
    """
    if not (isinstance(cipher, str) and key and isinstance(key, str)):
        raise ValueError('cipher/key invalid: %r, %r' % (cipher, key))

    if a2b:
        assert callable(a2b)
        cipher = a2b(cipher)

    return ARC4.new(key).decrypt(cipher)
