def join_wifi(ssid = None, password = None):
	'''Joins a wifi network via editing wpa config files and cycling wlan0.

	ARGS:
	@ssid		-- The name of the network intended to be joined.
	@password    -- The password to the network with the corresponding ssid.

	RETURN:
	None
	'''
	import sys
	import time
	sys.path.append('..')
	from run_command import run_command

	# If ssid is none then no network can be joined, therefore return None
	if ssid == None:
		return None

	# Appends network configuration lines to the end of 
	# /etc/wpa_supplicant/wpa_supplicant.conf
	# Ex.
	# network={
	#     ssid="example"
	#     psk="example_password"
	# }
	with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a') as myfile:
		myfile.write('\n')
		myfile.write('network={\n')
		myfile.write('    ssid="' + ssid + '"\n')
		if password:
			myfile.write('	  psk="' + password + '"\n')
		myfile.write('}\n')


	# Cycle the wlan0 interface so that the device joins the network																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																				q
	run_command('sudo ifdown wlan0')
	time.sleep(1)
	run_command('sudo ifup wlan0')

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--network', '-n','ssid')
	parser.add_argument('--password', '-p', 'password')
	args = parser.parse_args()

	join_wifi(args.ssid, args.password)
