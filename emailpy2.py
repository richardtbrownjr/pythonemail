import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "abc@gmail.com"
toaddr = "cdef@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Message has From To & Subject all from python"
body = "Here lies the body of the message, for all to see."
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "hearts&minds")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# message runs in python2.7 not python3 what gives?
