import socket
import sys
import argparse
import logging
import shlex, subprocess

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('tcp-ip-logs')

parser = argparse.ArgumentParser()
parser.add_argument("--host", default="127.0.0.1", type=str)
parser.add_argument("--port", default=1337, type=int)
args = parser.parse_args()
if not args.host or not args.port:
    log.critical("Nie podałeś któregoś z parametrów.")
    sys.exit(1)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (args.host, args.port)
log.info('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
log.info('waiting for a connection')
connection, client_address = sock.accept()
data = ""

#command_line = input()
#args = shlex.split(command_line)
#print(args)
#p = subprocess.Popen(args) # Success!
#print(p)

while True:
    data += connection.recv(1024).decode('utf-8')
    if data.endswith('\n'):
        print(data)
        data = ""









