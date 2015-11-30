def post_network_device(ssid, publickey, dev_name, IP_address, MAC, Gateway_mode, 
	      description, longitude, latitude, notes):
	import json
	from string import split
	from threading import Thread
	from server_communication import post_resource_to_server

	network_settings = { 'ssid' : ssid,
						 'publickey' : publickey,
						 'dev_name' : dev_name, 
						 'MAC' : MAC,
						 'IP_address' : IP_address }
	with open('resources/network_settings.json', 'w') as settings_file:
		json.dump(network_settings, settings_file)

	net_info = { 'name' : ssid,
				 'publickey' : publickey }
	network_payload = { 'network' : net_info,
						'commit' : 'Add Network'}
	session, response = post_resource_to_server.post_resource_to_server('networks', network_payload)
	network_id = split(response.url, '/')[-1]

	dev_info = { 'name' : dev_name,
				 'IP_address' : IP_address,
				 'MAC' : MAC,
				 'AP_SSID' : ssid,
				 'Gateway_mode' : Gateway_mode,
				 'description' : description,
				 'longitude' : longitude,
				 'latitude' : latitude,
				 'notes' : notes }
	device_payload = { 'device' : dev_info,
					   'network_id' : network_id,
					   'commit' : 'Add Device' }
	session, repsonse = post_resource_to_server.post_resource_to_server('devices', device_payload, session)

if __name__ == '__main__':
	setup('roxbury', 'hill', 'mine', '66.66.56.66', '11:22:33:DD:EE:FF', 
		  'server', '-#-#-', 'the palace', 'what?')
