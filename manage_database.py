def manage_database(timestamp):
	import time
	import requests
	from server_communication.post_resource_to_server import *
	from read_ip_address import read_ip_address

	# Initialize array of delays and find the IP address of the interface that
	# the LAN host should be operating on
	index = 0
	delay = [300, 300, 300, 600, 600, 1200]
	ip = read_ip_address('wlan0')

	# This loop will run until application termination to continuously sync
	# the local and remote databases
	while True:
		# Reset whether the DB has changed and define an empty dict, which
		# represents no changes in the current DB (this is so no data is 
		# written to the local DB, but changes from it can still be
		# received)
		changed = False
		args = { 'timestamp' : timestamp,
				 'users' 	 : None,
				 'networks'  : None,
				 'devices'	 : None }
		session, response = post_resource_to_server('/db_manager', args, 
													server = ip + ':3000')

		# NEED TO PARSE RESULT FOR PROPER DATABASE ENTRIES

		# Check for changes from the LAN host. If some exist flag that there
		# has been a change and store changes in dict.
		if users is not None or networks is not None or devices is not None:
			changed = True
			args['users'] = 
			args['networks'] = 
			args['devices'] = 

		# Send the additions to the central server
		session, response = post_resource_to_server('/db_manager', args, 
													server = 'batphone.co')
		
		# NEED TO PARSE RESULT FOR PROPER DATABASE ENTRIES AND TIMESTAMP
		timestamp = 

		# Check for changes from the server. If some exist flag that there
		# has been a change, store changes in a dict, and add them to the
		# LAN host.
		if users is not None or networks is not None or devices is not None:
			changed = True
			args['users'] = 
			args['networks'] = 
			args['devices'] = 
			session, response = post_resource_to_server('/db_manager', args, server = ip + ':3000')

		if not changed and index != 5:
			index = index + 1
		time.sleep(delay)


