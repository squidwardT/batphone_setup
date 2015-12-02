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

@app.route('/setup')
def setup():
	import sys
	sys.path.append('..')
	from join_wifi import *
	from application_management import *
	from join_batman_network import *
	from post_network_device import *
	
	dev_name = request.form['name']
	longitude = request.form['longitude']
	latitude = request.form['latitude']
	description = request.form['description']
	notes = request.form['notes']
	ssid = request.form['ssid']
	mac = request.form['mac']
	wifi_ssid = request.form['wifi_ssid']
	wifi_password = request.form['password']
		
	join_wifi(ssid = wifi_ssid, password = wifi_password)
	data = database_clone()
	join_batman_network(interface = 'wlan0', network_name = ssid, ap_mac = mac)
	post_network_device(ssid = ssid, publickey = 'pgp', dev_name = dev_name,
			    IP_address = '0.0.0.0', MAC = mac, Gateway_mode = 'client', 
			    description = description, longitude = longitude, latitude = latitude,
			    notes = notes)
	host_web_app()
	populate_db(data)
	manage_db()
	return 'OK'
	 

if __name__ == '__main__':
	app.run(host='10.0.0.1')
