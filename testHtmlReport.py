import unittest
from HTMLTestRunnerCN import HTMLTestRunner


suite=unittest.defaultTestLoader.discover('./')
f=open("report.html","wb")
HTMLTestRunner(stream=f,title="API Test",description="测试描述",tester="卡卡").run(suite)
f.close()


