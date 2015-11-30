def get_resource_from_server(rsc_path, payload = None):
	'''Hit the server with a GET command.

	ARGS:
	@rsc_path 		-- The path from the application root to find the resource.
	@payload 		-- Any necessary arguments like authentication information.

	RETURNS:
	@request 		-- The python request object with the received data.
	'''
	import requests

	# Build the path to the resource
	abs_path = 'http://batphone.co:3000/' + rsc_path

	# Do the GET with or without payload
	if payload is None:
		return requests.get(abs_path)
	return request.get(abs_path, payload)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()

	get_resource_from_server(args.path)