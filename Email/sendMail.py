import smtplib
from email.mime.text import MIMEText
from unittestTest.config import *
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="812356517@qq.com"    #用户名
mail_pass="wang1219"   #口令 

sender = '812356517@qq.com'
receivers = ['18736075564@163.com'] 

# msg=MIMEText("this is a test email","plain","utf-8")

report_file="F://myeclipse/PythonLearn/unittestTest/tmp/report.html"
with open(report_file,encoding="utf-8") as f:  # 打开html报告
    email_body = f.read()  # 读取报告内容

print(email_body)
msg=MIMEMultipart()
msg.attach(MIMEText(email_body,"html","utf-8"))

msg['From']="812356517@qq.com"
msg['To']="18736075564@163.com"
#     msg['Subject']="Api test Report"
msg['Subject'] = Header("接口测试报告'","utf-8")
    
    
att1=MIMEText(open(report_file,"rb").read(),"base64","utf-8")
att1['Content-Type']="application/octet-stream"
att1["Content-Disposition"] = 'attachment; filename="report.html"'
msg.attach(att1)


msg['From']="812356517@qq.com"
msg['To']="18736075564@163.com"
msg['Subject']="Api test Report"

# try:
#     smtpObj = smtplib.SMTP() 
#     smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
#     smtpObj.login(mail_user,mail_pass)  
#     smtpObj.sendmail(sender, receivers, msg.as_string())
# #     print("邮件发送成功")
#     logging.info("邮件发送成功")
# except smtplib.SMTPException as e:
# #     print("Error: 无法发送邮件")
#     logging.error(str(e))
# finally:
#     smtpObj.quit()

try:
    smtp=smtplib.SMTP_SSL(mail_host)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail("812356517@qq.com", "18736075564@163.com", msg.as_string())
    logging.info("邮件发送成功")
except smtplib.SMTPException as e:
    logging.error(str(e))
finally:    
    smtp.quit()
        
    


