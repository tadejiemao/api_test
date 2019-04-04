import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='./log/log.txt',
                    filemode='a'
                    )

## 数据库配置
db_host="10.1.198.134"
db_user="root"
db_passwd="root"
db_port=3306
db="logtrace_test"

## 邮件服务器配置
mail_host="smtp.qq.com"         #设置服务器
mail_user="812356517@qq.com"    #用户名
mail_pass="wang1219"            #口令 

sender=mail_user
receiver = '18736075564@163.com'  # 收件人
subject = '接口测试报告'  # 邮件主题


