import unittest

from test_user_login import TestUserLogin
from test_user_reg import TestUserReg

suite=unittest.TestSuite()

# 添加单个测试用例
suite.addTest(TestUserLogin('test_user_login_normal')) 
# 添加多个测试用例
suite.addTests(TestUserReg('test_user_reg_normal'),TestUserReg('test_user_reg_exist'))
unittest.TextTestRunner(verbosity=2).run(suite)


## makesuite制作用例集
suite1=unittest.makeSuite(TestUserLogin,'test_user_login_normal')
suite2=unittest.makeSuite(TestUserLogin)
unittest.TextTestRunner(verbosity=2).run(suite1)

## TestLoader（用例加载器）生成测试集
suite3=unittest.TestLoader().loadTestsFromTestCase(TestUserLogin)
unittest.TextTestRunner(verbosity=2).run(suite3)


## discover（用例发现）遍历所有测试集
suite4=unittest.defaultTestLoader.discover('./')
unittest.TextTestRunner(verbosity=2).run(suite4)



