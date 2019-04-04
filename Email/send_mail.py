import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from unittestTest.config.config import *

# mail_host="smtp.qq.com"         #设置服务器
# mail_user="812356517@qq.com"    #用户名
# mail_pass="wang1219"            #口令 


# sender = "812356517@qq.com"
# receivers = ['18736075564@163.com'] 

## 读取config配置
mail_host=mail_host
mail_user=mail_user
mail_pass=mail_pass

sender=mail_user
receivers=receiver


def send_mail(report_file):
    msg=MIMEMultipart()
    msg.attach(MIMEText(open(report_file,encoding="utf-8").read(),"html","utf-8"))
    
    
    msg['From']="812356517@qq.com"
    msg['To']="18736075564@163.com"
#     msg['Subject']="Api test Report"
    msg['Subject'] = Header(subject,"utf-8")
    
    att1=MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att1['Content-Type']="application/octet-stream"
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)

#     try:
#         smtpObj = smtplib.SMTP() 
#         smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
#         smtpObj.login(mail_user,mail_pass)  
#         smtpObj.sendmail(sender, receivers, msg.as_string())
# #     print("邮件发送成功")
#         logging.info("邮件发送成功")
#     except smtplib.SMTPException as e:
# #     print("Error: 无法发送邮件")
#         logging.error(str(e))
#     finally:
#         smtpObj.quit()
    try:
        smtp=smtplib.SMTP_SSL(mail_host)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(mail_user, receiver, msg.as_string())
        logging.info("邮件发送成功")
    except smtplib.SMTPException as e:
        logging.error(str(e))
    finally:    
        smtp.quit()


send_mail("F://myeclipse/PythonLearn/unittestTest/tmp/report.html")