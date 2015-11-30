def get_auth_token(session):
	'''Go to the login page and get the auth token to use in the future.

	ARGS:
	Session @session 	-- The HTTP session occupoed by the user.

	RETURNS:
	STRING @auth 	-- The auth token for the users session.
	'''
	from BeautifulSoup import BeautifulSoup
	html = BeautifulSoup(session.get('http://batphone.co:3000/login').text)
	return html.head.find('meta', attrs={'name': 'csrf-token'})['content']
