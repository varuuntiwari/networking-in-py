from email.mime.base import MIMEBase
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def assignSMTPserver(opt):
    if opt == 1:
        return ["smtp.gmail.com", 465]
    elif opt == 2:
        return ["smtp.mail.yahoo.com", 465]
    elif opt == 3:
        server = input("Enter your server name: ")
        port = int(input("Specify the port number: "))
        return [server, port]

def attachFile(msg, f):
    binaryFile = open(f, "rb")
    payload = MIMEBase('application', 'octet-stream')
    payload.set_payload(binaryFile.read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', f'attachment; filename={f}')
    msg.attach(payload)

def sendMail():
    print("1. Gmail\n2. Yahoo\n3. Use your own SMTP server\n")
    opt = int(input("Enter your email service: "))
    serverName, serverPort = assignSMTPserver(opt)
    print(serverName, serverPort)
    server = smtplib.SMTP_SSL(serverName, serverPort)
    server.ehlo()

    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        server.login(email, password)
    except:
        print("[-] Login failed, please your server settings")
        return
    
    body = MIMEMultipart('alternative')
    body["From"] = input("From? ")
    body["To"] = input("To? ")
    body["Subject"] = input("Enter subject: ")
    mes = input("Enter your message: ")
    body.attach(MIMEText(mes, "html"))

    if input("Attach file?(y/n)") == "y":
        filename=input("Path of file: ")
        attachFile(body, filename)

    finalMessage = body.as_string()
    receiverMail = input("Enter email of receiver: ")
    try:
        server.sendmail(email, receiverMail, finalMessage)
        print("[+] Email sent successfully")
    except:
        print("[-] Email failed to send")
        return

sendMail()
