import unittest 
import requests
from unittestTest.lib.db import * 
from unittestTest.readExcel import *
import json

NOT_EXIST_USER="李四"
EXIST_USER="张三"

class TestUserReg(unittest.TestCase):
#     url="http://115.28.108.130:5000/api/user/reg/"
#     
#     def test_user_reg_normal(self):
#         if check_user(NOT_EXIST_USER):
#             del_user(NOT_EXIST_USER)
#     
#         data={'name':'NOT_EXIST_USER','password':'123456'}
#         res=requests.post(url=self.url,json=data)
#         
#         except_res={ 
#                         "code": "100000",
#                         "msg": "成功",
#                         "data": {
#                                     "name": NOT_EXIST_USER,
#                                     "password": "e10adc3949ba59abbe56e057f20f883e"
#                                 }
#                     
#                     }
#         
#         self.assertDictEqual(res.json(),except_res)
#         self.assertTrue(check_user(NOT_EXIST_USER))
#         
#         del_user(NOT_EXIST_USER)
#     
#     def test_user_reg_exist(self):
#         if not check_user(EXIST_USER):
#             add_user(EXIST_USER)
#         
#         data={'name':'EXIST_USER','password':'123456'}
#         res=requests.post(url=self.url,json=data)
#         
#         except_res={ 
#                         "code": "100001",
#                         "msg": "失败，用户已存在",
#                         "data": {
#                                     "name": EXIST_USER,
#                                     "password": "e10adc3949ba59abbe56e057f20f883e"
#                                 }
#         }
# #         self.assertDictEqual(res.json(),except_res)
#         ## 断言
#         self.assertDictEqual(res.json(),except_res)
#         
    @classmethod
    def setUpClass(cls):
        cls.data_list=excel_to_list("./input/test_user_data.xlsx","TestUserReg")
    
    
    def test_user_reg_normal(self):
        case_data=get_test_data(data_list, "test_user_reg_normal")
        if not case_data:
            print("测试数据不存在")
        url=case_data.get('url')
        data=json.loads(case_data.get('data'))
        except_res=json.loads(case_data.get('except_res'))
        name=data.get('name')
        
        if check_user(name):
            del_user(name)
        
        res=requests.post(url=url,json=data)
        
        self.assertDictEqual(res.json(),except_res)
        self.assertTrue(check_user(name))
        del_user(name)
          

if __name__ == '__main__':
    unittest.main(verbosity=2)
            