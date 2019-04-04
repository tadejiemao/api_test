import unittest

from test_user_login import TestUserLogin


suite1=unittest.TestSuite()
suite1.addTest(TestUserLogin('test_user_login_normal'))
suite2=unittest.makeSuite(TestUserLogin,'test_user_login_password_wrong')

suite=unittest.TestSuite([suite1,suite2])
unittest.TextTestRunner(verbosity=2).run(suite)


