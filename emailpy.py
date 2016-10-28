import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("abc@gmail.com", "mythoughts&ideas")
msg = "Just wrote my first little code for sending emails directly from python"
server.sendmail("abc@gmail.com", "persongetting@gmail.com", msg)
server.quit()
