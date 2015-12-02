def database_clone():
	import sys
	sys.path.append('..')
	(from server_communication.post_resource_to_server 
	 import *)

	args = { 'timestamp' : 0,
		 'users'     : None,
		 'networks'  : None,
		 'devices'   : None }
	session, response = post_resource_to_server('/db_manage', args,
						     server = 'batphone.co')
	return response.json()

	
