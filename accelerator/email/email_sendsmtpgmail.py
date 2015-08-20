#!/usr/bin/python

import smtplib

fromaddr = 'your.email@gmail.com'
toaddrs  = 'John.Do@yahoo.com'
subject = 'This is a subject'
message = 'This is the message'
msg = 'Subject: %s\n\n%s' % (subject, message)


# Gmail Credentials for smtp
username = 'your.email'
password = 'yourpassword'

# Send email
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
