import smtplib
from email.mime.text import MIMEText
from email.header import Header
from emailPython.testEmail import receivers


# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="812356517@qq.com"    #用户名
mail_pass="wang1219"   #口令 
 
 
sender = '812356517@qq.com'
receivers = ['18736075564@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Test Report.', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
#  

subject = "测试报告"
message['Subject'] = Header(subject, 'utf-8')
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
    