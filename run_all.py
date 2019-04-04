import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from unittestTest.config.config import *
from unittestTest.Email.send_mail import send_mail

logging.info("------测试开始---------") 
suite=unittest.defaultTestLoader.discover("./")

with open("./tmp/report.html","wb") as f:
    HTMLTestRunner(stream=f,title="Api Test",description="测试藐视",tester="Venom").run(suite)


send_mail("./tmp/report.html")
logging.info("------测试结束---------") 