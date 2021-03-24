# Send email
import smtplib
my_email_id = "sender@gmail.com"
password = "test123"

connection = smtplib.SMTP("smtp.gmail.com", 587) # using the gmail smtp server as it is my email
connection.starttls() # make the connection secure
connection.login(user=my_email_id, password=password)
connection.sendmail(from_addr=my_email_id, to_addrs="addressee@gmail.com", msg="Subject: Hellow \n\n Hello  how are you? Py \n\n Sent from a python script")
connection.close()
