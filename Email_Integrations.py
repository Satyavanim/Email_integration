import smtplib
import ssl
from PIL import Image
from email.message import EmailMessage


# Create the email message
sender_email = 'sender@gmail.com'
sender_password = ''   #give your App Password ,don't give your google Account password,in my github account i sent how to create the App Password 
Receiver_email = 'receiver@gmail.com'
subject="No face detected"
body = """
there is no faces infront of camera
"""
                
print("Sending email......")
em = EmailMessage()            
em['From'] = sender_email
em['To'] = Receiver_email
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
            
# attach the saved image to the email message
with open('detected_face.jpg', 'rb') as f:
    img_data = f.read()
em.add_attachment(img_data, maintype='image', subtype='jpg', filename='detected_face.jpg')
# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(sender_email,sender_password)
    smtp.sendmail(sender_email,Receiver_email, em.as_string())
    print("mail sent successfully")
