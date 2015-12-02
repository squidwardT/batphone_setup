def clone_web_app():
	import sys
	sys.path.append('..')
	from run_command import run_command
	from server_communication.post_resource_to_server import post_resource_to_server

	run_command('git clone https://github.com/elevati0n/batphoneWebApp.git')
	run_command('cd batphoneWebApp; sudo bundle install')

