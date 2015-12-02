from datetime import datetime

from flask import (
	Flask,
	abort,
	flash,
	redirect,
	render_template,
	request,
	url_for,
)
from flask.ext.stormpath import (
	StormpathError,
	StormpathManager,
	User,
	login_required,
	login_user,
	logout_user,
	user,
)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'nananananananana'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey-YVVIY4R3LM986736KU1OS4LNX.properties'
app.config['STORMPATH_APPLICATION'] = 'batphone_setup'

stormpath_manager = StormpathManager(app)

@app.route('/')
def show_index():
	return render_template('index.html')

@app.route('/setup', methods=['POST'])
def setup():
	import sys
	sys.path.append('..')
	import application_management
	import threading
	from sockets import TCPServerSocket
	from join_wifi import join_wifi
	from join_batman_network import join_batman_network
	from post_network_device import post_network_device
	
	# Pull info from form
	dev_name = request.form['name']
	longitude = request.form['longitude']
	latitude = request.form['latitude']
	description = request.form['description']
	notes = request.form['notes']
	ssid = request.form['ssid']
	mac = request.form['mac']
	
	# Join the BATMAN network in the DHCP/Web App Host spot
	join_batman_network(interface = 'wlan0', network_name = ssid, ap_mac = mac)

	# Creates a thread to manage new network devices and 
        # dish out open IP addresses.           
        socket = TCPSocketServer.TCPSocketServer('192.168.2.4')
        dhcp_thread = threading.Thread(target = socket.start_server)
        dhcp_thread.start()
	
	# Get the data from the server
	data = application_management.database_clone.database_clone()
	
	# Add the device's information to the database
	post_network_device(ssid = ssid, publickey = 'pgp', dev_name = dev_name,
			    IP_address = '192.168.2.4', MAC = mac, Gateway_mode = 'client', 
			    description = description, longitude = longitude, latitude = latitude,
			    notes = notes)
	
	# Start hosting the web app, add the info to the database
	# Start managing the database syncing
	application_management.host_web_app.host_web_app()
	application_management.populate_db.populate_db(data)
	application_management.manage_db.manage_db()
	return 'OK'
	 

if __name__ == '__main__':
	app.run(host='10.0.0.1')
