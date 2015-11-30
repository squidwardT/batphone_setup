def get_server_resource_header(rsc_path):
	import requests

	abs_path = 'http://batphone.co:3000/' + abs_path
	return requests.get(abs_path).headers

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()

	get_server_resource_header(args.path)