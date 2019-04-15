#coding:utf-8

from util import crypto_rc4
import time
from operation.user import UserOp
from operation.verify_manage import VerifyOp
import unittest
from util import common_util, convert
import time
from datetime import datetime


class UserTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        UserTestCase.user_id = ""
        UserTestCase.time = 0
        UserTestCase.code_id = ""
        UserTestCase.token = None

    def setUp(self):
        self.op = UserOp()
        self.code = VerifyOp()

    def tearDown(self):
        # self.op.delete(id=UserTestCase.user_id)
        # self.code.delete(id=UserTestCase.code_id)
        pass

    def test_01_create(self):
        print "test_01_create"

        code_create = self.code.create(phone="1748593217", verify_code="888888")
        print "code_create=%s" % code_create
        self.assertTrue(code_create is not None)
        UserTestCase.code_id = convert.bs2utf8(code_create.get("id"))
        verify_re = self.code.verify_code_phone(phone="1748593217", code="888888")
        self.assertTrue(verify_re==False)
        user_create = self.op.create(phone="1748593217", referrer_id='')
        self.assertTrue(user_create is not None)

    def test_02_login(self):
        print "test_02_login"
        _ = self.op.login("1748593217")
        print("login_re=%s"%_)
        UserTestCase.user_id = convert.bs2utf8(_.get("id"))
        UserTestCase.time = int(time.time())
        print "user_id=%s,type=%s"%(UserTestCase.user_id, type(UserTestCase.user_id))
        UserTestCase.token = common_util.gen_token(UserTestCase.user_id, UserTestCase.time)
        print "token=%s" % UserTestCase.token
        #self.assertTrue(True)

    def test_03_token(self):
        print "test_03_token"
        print "user_id=%s,type=%s" % (UserTestCase.user_id, type(UserTestCase.user_id))
        content = ":".join((UserTestCase.user_id, str(UserTestCase.time)))
        print "content=%s" % content
        _ = crypto_rc4.decrypt(UserTestCase.token, crypto_rc4.SECRET_KEY)
        print "_=%s" % _
        self.assertTrue(_ == content)

    def test_04_update(self):
        print "test_04_update"

        update_dict = {
            "phone": "13225004810",
            "sex": 0,
            "birthday": datetime.now(),
            "nick_name": "ahahah",
        }
        self.op.update(id=UserTestCase.user_id, **update_dict)

        ph = self.op.info(id=UserTestCase.user_id).get('phone')

        self.assertTrue("13225004810" == ph)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(UserTestCase("test_01_create"))
    suite.addTest(UserTestCase("test_02_login"))
    suite.addTest(UserTestCase("test_03_token"))
    suite.addTest(UserTestCase("test_04_update"))
    unittest.TextTestRunner(verbosity=3).run(suite)