def read_ip_address(interface):
	'''Read a interface's IP address.

	ARGS:
	@interface 		-- The interfaces IP to be read. Ex Bat0, Eth0

	RETURNS:
	@ip 			-- The IP address of the interface as a STRING
	'''
	import netifaces
	if interface not in netifaces.interfaces():
		return None

	return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('interface')
	args = parser.parse_args()

	print read_ip_address(args.interface)
