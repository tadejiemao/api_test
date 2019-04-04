import unittest
import requests
from unittestTest.readExcel import *
import json
from unittestTest.config.config import *
from unittestTest.case_log import *

class TestUserLogin(unittest.TestCase):
    
#     url = 'http://115.28.108.130:5000/api/user/login/'
#     def test_user_login_normal(self):
#         data={'name':'张三','password':'123456'}
#         res=requests.post(url=self.url,data=data)
#         self.assertIn('登录成功',res.text)  #断言
#             
#         
#     def test_user_login_password_wrong(self):
#         data={'name':'张三','password':'1234567'}
#         res=requests.post(url=self.url,data=data)
#         self.assertIn('失败，用户名或密码错误',res.text)
#     
#     ##assertIn(a,b)/assertNotIn(a,b) # b中是否包含a
#         
    @classmethod
    def setUpClass(cls):
        cls.data_list=excel_to_list("./input/test_user_data.xlsx","TestUserLogin")
    
    def test_user_login_normal(self):
        case_data=get_test_data(self.data_list,"test_user_login_normal")
        url=case_data.get('url')
        data=case_data.get('data')
        except_res=case_data.get('except_res')
        res=requests.post(url=url,data=json.loads(data))
        logging.info("测试用例：{}".format("test_user_login_normal"))
        logging.info("url:{}".format(url))
        logging.info("请求参数：{}".format(data))
        logging.info("期望结果:：{}".format(except_res))
        logging.info("实际结果：{}".format(res.text))
        self.assertEqual(res.text,except_res)      
    
    def test_user_login_password_wrong(self,encoding=None):
        case_data=get_test_data(self.data_list,"test_user_login_password_wrong")
        url=case_data.get('url')
        data=case_data.get('data')
        except_res=case_data.get('except_res')
        res=requests.post(url=url,data=json.loads(data))
        res_text=res.text
#         logging.info("测试用例：{}.".format("test_user_login_normal"))
#         logging.info("url:{}".format(url))
#         logging.info("请求参数：{}".format(data))
#         logging.info("期望结果:：{}".format(except_res))
#         logging.info("实际结果：{}".format(res.text))
        log_case_info("test_user_login_normal",url,data,except_res,res_text)
        self.assertEqual(res.text,except_res)  
           
           
if __name__ == '__main__':
    unittest.main(verbosity=2)   