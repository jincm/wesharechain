#coding:utf-8

from util import crypto_rc4
import time
from operation.user import UserOp
from operation.verify_manage import VerifyOp
import unittest
from util import common_util
import time
from datetime import datetime


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.op = UserOp()
        self.code = VerifyOp()
        pass

    def tearDown(self):
        pass

    def test_02_login(self):
        """

        :return:
        """
        _ = self.op.login("1748593217")
        self.user_id = _.get("id")
        self.time = int(time.time())
        self.token = common_util.gen_token(_.get("id"), self.time)
        #self.assertTrue(True)

    def test_03_token(self):
        content = ":".join((self.user_id, self.time))
        _ = crypto_rc4.decrypt(self.token, crypto_rc4.SECRET_KEY)
        self.assertTrue(_ == content)

    def test_01_create(self):
        code_create = self.code.create(phone="1748593217", verify_code="888888")
        self.assertTrue(code_create is not None)
        verify_re = self.code.verify_code_phone(phone="1748593217", code="888888")
        self.assertTrue(verify_re == True)
        user_create = self.op.create(phone="1748593217", referrer_id='')
        self.assertTrue(user_create is not None)

    def test_04_update(self):
        update_dict = {
            "phone": "13225004810",
            "sex": 0,
            "birthday": datetime.now(),
            "nick_name": "ahahah",
        }
        self.op.update(id=self.user_id, **update_dict)

        ph = self.op.info(id=self.user_id).get('phone')

        self.assertTrue("13225004810" == ph)

if __name__ == "__main__":
    unittest.main()