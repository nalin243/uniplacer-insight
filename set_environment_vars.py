import os
from argparse import ArgumentParser

#add in you smtp email and password for the account that will be used to send otp for password authentication

parser = ArgumentParser()
parser.add_argument("-e","--smtp-email")
parser.add_argument("-p","--smtp-pass")

args = parser.parse_args()

os.environ["SMTP_EMAIL"] = "{}".format(args.smtp_email)
os.environ["SMTP_PASS"] = "{}".format(args.smtp_pass)