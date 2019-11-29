import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '2e79057af25b01'
    password = 'a1038d29558b25'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'pkraja121dss@gmail.com'
    receiver_email = 'pratik@iiitkalyani.ac.in'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Honda Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    # print('sent1')
    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        # print('sent2')
        server.login(login, password)
        # print('sent3')
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print('sent')











# import smtplib
# from email.mime.text import MIMEText

# def send_mail(customer, dealer, rating, comment):
#     port = 9950
#     smtp_server = 'smtp.mailtrap.io'
#     login = '2e79057af25b01'
#     passwoed = 'a1038d29558b25'
#     message = f"<h3>New Feedback Submission</h3><ul><li>Customer:{customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

#     sender_email = 'pkraja121dss@gmail.com'
#     receiver_email = 'pratik@iiitkalyani.ac.in'
#     msg = MIMEText(message, 'html')
#     msg['Subject'] = 'Honda-Feedback'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email

#     # Send email

#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, passwoed)
#         server.sendmail(sender_email, receiver_email, msg.as_string())
