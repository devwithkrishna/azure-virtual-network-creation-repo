import os
import argparse
from jinja2 import Environment, FileSystemLoader
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, Cc

def send_email(application_name:str, vnet_name: str, address_space: str, region: str, subscription_id: str, environment: str):
	"""send email to helpdesk using sendgrid"""

	# Set up the Jinja2 environment and load the template file
	env = Environment(loader=FileSystemLoader('templates'))

	template = env.get_template('email.j2')

	# Data to populate the template
	context = {
		"vnet": vnet_name,
		"cidr_range": address_space,
		"region": region,
		"environment": environment,
		"application_name": application_name,
		"subscription_name_id": subscription_id,
		"sender_name": os.getenv('GITHUB_ACTOR'),
		"team_name": "DevOps"
	}

	# Render the template
	email_content = template.render(context)

	# Output the rendered email
	print(email_content)

 
	# SendGrid variables setup
	sender_email = "krishnadhas@devwithkrishna.in"
	recipient_email = os.getenv("USER_EMAIL")
	sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
	cc_emails = ["krishnadhasnk@gmail.com"]

	# Print the values
	print(f"Sender Email: {sender_email}")
	print(f"Recipient Email: {recipient_email}")
	print(f"SendGrid API Key: {sendgrid_api_key}")
 
	if not sender_email or not recipient_email or not sendgrid_api_key:
		raise ValueError("Missing SENDGRID_SENDER_EMAIL, SENDGRID_RECIPIENT_EMAIL, or SENDGRID_API_KEY environment variable.")

	
	# Create email
	message = Mail(
		from_email=sender_email,
		to_emails=To(recipient_email),
		cc=[Cc(email) for email in cc_emails],
		subject=f"Express Route Setup Request for {application_name}",
		html_content=email_content,
	)
 
	# Send the email
	try:
		sg = SendGridAPIClient(sendgrid_api_key)
		response = sg.send(message)
		print(f"Email sent successfully! Status code: {response.status_code}")
	except Exception as e:
	    print(f"Failed to send email: {str(e)}")



def main():
	"""run the code"""
	parser = argparse.ArgumentParser("Prepare email for express route set up...")
	parser.add_argument("--application_name", help="Application name", required=True, type=str)
	parser.add_argument("--vnet_name", help="VNet name", required=True, type=str)
	parser.add_argument("--address_space", help="Address space", required=True, type=str)
	parser.add_argument("--region", help="Region", required=True, type=str)
	parser.add_argument("--subscription_id", help="Subscription ID", required=True, type=str)
	parser.add_argument("--environment", help="Environment", required=True, type=str)

	# get the args
	args = parser.parse_args()

	application_name = args.application_name
	environment = args.environment
	vnet_name = args.vnet_name
	address_space = args.address_space
	region = args.region
	subscription_id = args.subscription_id

	send_email(application_name=application_name, region=region, vnet_name=vnet_name, address_space=address_space, environment=environment, subscription_id=subscription_id)

if __name__ == "__main__":
	main()