import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "richardtbrownjr@gmail.com"
toaddr = "jfarrar@structurebuildingcompanyus.com", "rbrown@theinstitutenc.org"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Tesing my code to write and send my own emails"

body = "Testing one, two three"

msg.attach(MIMEText(body, 'plain'))

filename = "rbresume.pdf"
#attachment = open("/Users/r/Desktop/", "rb")

part = MIMEBase('application', 'octet-stream')
#part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; fileman= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "passwordforemail")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
