from app import Application

from argparse import ArgumentParser

if __name__ == '__main__':

	parser = ArgumentParser()
	parser.add_argument("-d","--dev",action="store_true")

	args = parser.parse_args()

	application = Application(args)