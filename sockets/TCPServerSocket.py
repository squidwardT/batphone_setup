import shlex
import select
import socket
from threading import Thread
from TCPSocket import TCPSocket


class TCPServerSocket(TCPSocket):

    '''CLASS: Representing a BATMAN-Advanced node as a server socket listening on
                      a port to take action or pass data

    FIELDS:
    @self.sock 	-- The child socket this socket has been built from.
    @self.clients	-- The list of clients that are communicating with this
                                   device in some way.
    '''

    def __init__(self, address):
        '''CONSTRUCTOR: Run parent constructor and initialize the clients array
        '''
        super(TCPServerSocket, self).__init__(address)
        self.clients = []
        self.address = address
        self.port = 55704

    def start_server(self, interpreter = None):
        '''Listen on a @port for incoming application connections. When connected to
        store the client's information and attempt to read its transmitted data.

        ARGS:
        @port		-- The port number to start the server socket on

        RETURN:
        None		-- Theoretically Endless
        '''

        # Bind this socket to port and listen for connections
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(5)

        # While the application is running attempt listen for connections and read the
        # connecting devices message.
        while True:
            # Get the connected socket and make a Batman Socket out of it
            client, address = self.sock.accept()
            tcp_client = TCPSocket(address, client)

            # Start threads to add devices to the list of clients and read
            # their messages
            read_thread = Thread(
                target=self.read_client, args=[tcp_client, interpreter])
            read_thread.start()

    def update_client(self):
        '''Update the list of known clients removing all clients that are not readable
           or writable or are in error.

        ARGS:
        None

        RETURNS:
        None
        '''
        # Check the states of clients
        ready_to_read, ready_to_write, in_error = select.select(self.clients,
                                                                self.clients,
                                                                self.clients,
                                                                60.0)
        # Remove items in error
        for item in in_error:
            self.clients.remove(item)
        # Remove items not readable or writable
        for item in self.clients:
            if item not in ready_to_read and item not in ready_to_write:
                self.clients.remove(item)
        # Read ready to read clients
        for item in ready_to_read:
            self.read_client(item)

    def add_client(self, clients):
        '''Add a client to the list of recent client. If it already exists update it.

        ARGS:
        @clients		-- The client to be added to the list

        RETURNS:
        None
        '''
        # Update client list and read out inbound messages
        client = clients
        self.update_client(client)

        # If the newly connected device is already in list update it otherwise
        # add it
        for item in self.clients:
            if item.address == client.address:
                self.clients.remove(item)
        self.clients.append(client)

    def read_client(self, clients, interpreter):
        '''Receive the client's message.

        ARGS:
        @clients		-- The client socket to be read from.
        @address		-- IGNORE. Purely for error prevention

        RETURNS:
        @args 			-- A list of arguments to be interpreted
        '''
        msg = interpreter.interpret(clients.read())

        if msg is not None:
            print msg
            respond_to_client(clients, msg)

    def respond_to_client(self, client, msg):
        from TCPSocket import TCPSocket
        port = find_tcp_port(client.address)

        responder = TCPSocket(self.address)
        responder.connect(client.address, port)
        responder.write(msg)
        responder.close()


if __name__ == '__main__':
    server = TCPServerSocket('whatever')
    server.start_server()
