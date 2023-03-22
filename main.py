import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import sys
import datetime
import os
import requests


today = datetime.datetime.now()
today_date = (today.month, today.day, today.year)


# Ask for client details
client_name_first = input('Enter the client first name: ')
client_name_last = input('Enter the client last name: ')
client_job = input('Enter the client job title: ')
client_email = input('Enter the client email: ')
company_name = input('Enter the company name: ')
industry = input('Enter the company industry: ')

# Check if client has already been emailed
already_emailed = []
with open('already_emailed.txt', 'r') as f:
    already_emailed_text_list = f.read().splitlines()
    for line in already_emailed_text_list:
        if line:
            fields = line.split(' | ')
            if len(fields) >= 3:
                email = fields[2]
                already_emailed.append(email)
            else:
                print(f"Invalid format in line: {line}")
        else:
            print("Empty line found in file")

    if client_email in already_emailed:
        print("You already emailed this client.")
        sys.exit()

# Create email message
subject = "SUBJECT OF YOUR EMAIL"
body = f'BODY OF YOUR EMAIL. Good Afternoon {client_name_first}, we believe we can help {company_name}.

message = MIMEMultipart()
from_name = "YOUR NAME"
message['From'] = f'{from_name} <youremail@email.com>'
message['To'] = client_email
message['Subject'] = subject
message.attach(MIMEText(body))

# Attach PDF file
with open('file_path.pdf', 'rb') as f:
    attach = MIMEApplication(f.read(), _subtype='pdf')
    attach.add_header('Content-Disposition', 'attachment', filename='filename.pdf')
    message.attach(attach)

# Set up server
smtp_server = 'smtpout.secureserver.net'
smtp_port = 465

sender_email = 'your outlook email address'
sender_password = os.environ.get("SENDER_PASSWORD")  # your Outlook account password

with open('already_emailed.txt', 'r') as f:
    already_emailed_text_list = f.read().splitlines()
    if client_email in already_emailed_text_list:
        print("You already emailed this client.")
        sys.exit()


# Send email
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, client_email, message.as_string())
already_emailed.append(client_email)

# Add the client's email to the already_emailed.txt document
print('Email sent!')
with open('already_emailed.txt', 'a') as f:
    f.write(f"{today_date} | {client_name_first} {client_name_last} | {client_email} | {company_name} \n")
already_emailed.append(client_email)

# Add the client's info to the Google sheet document

sheety_user = os.environ.get("SHEETY_USER")
sheety_key = os.environ.get("SHEETY_KEY")
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
prospect_endpoint = os.environ.get("PROSPECT_ENDPOINT")

today_for_sheets = datetime.datetime.now().strftime("%m/%d/%Y")


sheet_inputs = {
        "prospectList": {
            "companyName": company_name,
            "contactName": f"{client_name_first} {client_name_last}, {client_job}",
            "industry": industry,
            "companyRepresentative": "YOUR NAME",
            "clientEmail": client_email,
            "email": f"Sent on {today_for_sheets}",

        }
    }

sheety_response = requests.post(url=prospect_endpoint, json=sheet_inputs, auth=(sheety_user, sheety_key))

# print(sheety_response.text)
