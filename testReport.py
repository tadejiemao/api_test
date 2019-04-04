import unittest

## 生成文本测试报告
suite=unittest.defaultTestLoader.discover('./')

with open("result.txt","w") as f:
    unittest.TextTestRunner(stream=f,verbosity=2).run(suite)

    