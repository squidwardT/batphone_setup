def populate_database(data):
	import sys
	sys.path.append('..')
	from read_ip_address import *
	(from server_communication 
		import 	post_resource_to_server)

	ip = read_ip_address('wlan0')
	session, response = post_resource_to_server('/db_manage', args,
						    server = ip)
	
		
