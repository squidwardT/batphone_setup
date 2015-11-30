def post_resource_to_server(rsc_path, payload, session = None, auth = None, cookie = None):
    '''POST something to the server.

    ARGS:
    @rsc_path 		-- The path from the root of the application to the
                                       resource to post.
    @payload 		-- The data to write to the resource.

    RETURNS:
    @request 		-- If the data was not received it is False, otherwise it
                                       is the request object returned by the post.
    '''
    import json
    import requests
    from BeautifulSoup import BeautifulSoup
    from get_auth_token import get_auth_token

    # Build the path to the resource.
    # This is the path to the root of the application plus the action to be
    # performed. For example to create a new user rsc_path can be set to
    # 'users'.
    abs_path = 'http://batphone.co:3000/' + rsc_path
    print 'Posting to ' + abs_path

    # GET an authenticity token
    # This starts a session and does a GET on the login page of our application
    # From the HTML received we can then parse for the csrf-token. Once way
    # have the csrf-token we can add it to the dictionary we're POSTing.
    if session is None:
        session = requests.Session()

    if cookie is not None:
        session.cookies = cookie

    if auth == None:
        payload['authenticity_token'] = get_auth_token(session)
    else:
        payload['authenticity_token'] = auth

    # Define a JSON header
    # This tells the server we're passing it JSON
    header = {'content-type': 'application/json'}

    # Post data in JSON format with the JSON header
    # Convert our data to JSON and POST bothe the header and data.
    response = session.post(abs_path,
                            headers=header,
                            data=json.dumps(payload))
    print str(requests.utils.dict_from_cookiejar(response.cookies))
    # Check whether the POST was successful
    if response.status_code == 200:
        print 'Success'
        return session, response
    else:
        print str(response.status_code)
    return False

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # parser.add_argument('path')
    # parser.add_argument('payload')
    args = parser.parse_args()

    path = 'users'
    data = {'user': {'name': 'crazy chris',
                     'email': 'crazy_chris@bananas.com',
                     'password': 'itsmechris',
                     'password_confirmation': 'itsmechris'},
            'commit': 'Create my account'}
    post_resource_to_server(path, data)
