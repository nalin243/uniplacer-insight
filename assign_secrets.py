from argparse import ArgumentParser

#used to assign secrets to the application

parser = ArgumentParser()
parser.add_argument("-e","--smtp-email")
parser.add_argument("-p","--smtp-pass")

args = parser.parse_args()

with open("src/uniplacerinsight/data/appsecrets.py","w") as secrets:
	newsecrets = """SMTP_EMAIL="{}"
SMTP_PASS="{}" """.format(args.smtp_email,args.smtp_pass)
	

	secrets.write(newsecrets)