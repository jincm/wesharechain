#coding:utf-8

from util import crypto_rc4
import time
import unittest


class CryptoTestCase(unittest.TestCase):
    def setUp(self):
        self.content = "dsfdsfsdf"
        #ts_str = str(time.time() + 3600)
        self.token = "b7957cabe762962648"
        pass

    def tearDown(self):
        pass

    def test_encrypt(self):
        """

        :return:
        """
        token = crypto_rc4.encrypt(self.content, crypto_rc4.SECRET_KEY)
        print "token"+token
        self.assertTrue(token == self.token)

    def test_decrypt(self):
        _ = crypto_rc4.decrypt(self.token, crypto_rc4.SECRET_KEY)
        self.assertTrue(_ == self.content)


if __name__ == "__main__":
    unittest.main()