def host_ap():
	import sys
	sys.path.append('..')
	from threading import Thread
	from run_command import run_command

	rails_home = find_rails_home()
	rails_thread = Thread(target=run_command, 
		args=('cd ' + rails_home + '; rails s -p 3000'))
	rails_thread.start()