#sending mail using python



import smptlib

s=smptlib.SMPT('smpt.gmail.com','587')
s.starttls()
sender='sender@gmail.com'
receiver='receiver@gmail.com'
msg="hlo"
s.login(sender,'password')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()