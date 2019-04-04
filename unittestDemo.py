import unittest

case=unittest.TestCase()

## assertEqual 断言值是否相等
print(case.assertEqual(1,2.0/2))
## assertLs  断言是否是同一对象（内存地址一样）
# print(case.assertIs(1,2.0/2))
## assertListEqual 断言列表是否相等
print(case.assertListEqual([1,2],[1,2]))

# print(case.assertIsNone({}))  # 失败
