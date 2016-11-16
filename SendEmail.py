import smtplib
import getpass

try:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
except:
  print("Somthing went wrong")

# make connection secure
server.starttls()

mypwd = getpass.getpass('Enter your password: ')  

myemail = "djauregui@csumb.edu"

recip = "djauregui@csumb.edu"

server.login(myemail, mypwd)

msg = "HELLO!"

server.sendmail(myemail, recip, msg)
server.quit()