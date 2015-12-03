def database_clone():
	import sys
	sys.path.append('..')
	from server_communication import post_resource_to_server

	args = { 'timestamp' : 0,
		 'users'     : None,
		 'networks'  : None,
		 'devices'   : None }
	session, response = post_resource_to_server.post_resource_to_server('/db_manage', args,
						     server = 'batphone.co')
	return response.json()

	
