# Send Cold Emails to Prospects

This repository contains a Python script for sending emails to clients and updating prospect information in a Google Sheets document. 
The script utilizes the 'smtplib' library for email functionality and the 'requests' library for interacting with the Google Sheets API.

# Prerequisites

Before running the script, ensure that you have the following prerequisites:

1. Python installed on your system.
2. Required Python libraries: 'smtplib', 'email.mime.text', 'email.mime.multipart', 'email.mime.application', and 'requests'.
3. Access to an email account for sending emails.
4. Credentials and API access for the Google Sheets API.

## Getting Started

To use this script, follow these steps:

1. Clone the repository to your local machine.

2. Install the required libraries by running the following command:
   
   pip install -r requirements.txt
  
3. Set up your email account details and credentials by modifying the script file. Replace the following placeholders with your own information:
   - 'subject': Replace with the subject of your email.
   - 'body': Replace with the body of your email, customized with the necessary variables.
   - 'from_name': Replace with your name or the desired sender name.
   - 'smtp_server': Replace with the SMTP server address for your email provider.
   - 'smtp_port': Replace with the SMTP port number for your email provider.
   - 'sender_email': Replace with your email address.
   - 'sender_password': Replace with your email account password or retrieve it securely using environment variables.

4. Prepare the PDF file you want to attach to the email. Make sure to replace 'file_path.pdf' with the actual path to your PDF file in the following code block:
   
   'python
   with open('file_path.pdf', 'rb') as f:
       ...
   '

5. Set up the required environment variables for interacting with the Google Sheets API:
   - 'SHEETY_USER': Replace with your Sheety API username.
   - 'SHEETY_KEY': Replace with your Sheety API key.
   - 'SHEETY_ENDPOINT': Replace with the Sheety API endpoint for updating the Google Sheets document.
   - 'PROSPECT_ENDPOINT': Replace with the endpoint for adding prospect information to the Google Sheets document.

6. Run the script
   
   
# Usage

When running the script, it will prompt you to enter the necessary details for the email and client information. Follow the instructions provided in the terminal to input the required information.

The script checks if the client has already been emailed by comparing the provided email address with the list of previously emailed clients stored in the 'already_emailed.txt' file. If the client has already been emailed, the script will exit.

Once the email is sent successfully, the client's email address will be added to 
the 'already_emailed.txt' file to track the sent emails. Additionally, the client's information will be added to 
the Google Sheets document specified by the 'SHEETY_ENDPOINT'. The prospect information will include 
details such as the company name, contact name, industry, and email status.

# License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize the script to suit your specific requirements and enhance its functionality as needed.
