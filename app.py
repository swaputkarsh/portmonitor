import boto3
import sys

apache_status = sys.argv[1]
port_status = sys.argv[2]

def send_email(apache_status, port_status):
    message = f"LIVESTAGE.SAFERWATCHAPP.COM IS DOWN.\n\n"
    if apache_status != "active":
        message += "Apache service is not running.\n"
    if "refused" in port_status:
        message += "Port 3000 is closed.\n"

    # AWS SES configuration
    client = boto3.client('ses', region_name='us-east-1')

    try:
        response = client.send_email(
            Source='no-reply@saferwatchapp.com',
            Destination={
                'ToAddresses': ['chandan@saferwatchapp.com']
            },
            Message={
                'Subject': {
                    'Data': 'Service Down Notification',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': message,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        print("Email sent! Message ID:", response['MessageId'])
    except Exception as e:
        print("Error: ", e)

# Send the email
send_email(apache_status, port_status)
