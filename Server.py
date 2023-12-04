import socket
import threading
import os
import time

#=============== File wrote by Clément MALON and Adam KHALIL ==================================
# Adam has made the broadcast/unicast function
# Clément has made the send function to send any kind of files
# Clément has merged the two functions above and made adjustments for it to work.

# Server configuration
HOST = 'localhost'
PORT = 12345

# Dictionary to store client connections
clients = {}

def send_file(file_name, connection):
    # Send the original file name first
    connection.sendall(file_name.encode('utf-8'))
    with open(file_name, 'rb') as file:
        for data in file:
            connection.sendall(data)
            
# Function to handle client connections
def handle_client(client_socket, client_address):
    try:
        while True:
            # Measure time to handle the request 
            start_time = time.time()
            
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            received_file_name = "Received_" + os.path.basename("".join(message.split(" ")[("@" in message):]))
                    
            with open(received_file_name, 'wb') as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)
                    
            print(f"Received message from {client_address}: {message}")
            
            # Delete the sender of the file to not send it his file in broadcast option
            del clients[str(client_address[1])]
            
            # Check if it's a broadcast or targeted message
            if message.startswith("@"):
                # Extract the target username
                target_username, message = message[1:].split(" ", 1)
                
                # Send the message to the specific client
                target_socket = clients.get(target_username)

                if target_socket:
                    send_file(received_file_name, target_socket)
                else:
                    print(f"User {target_username} not found.")
                    
                # Measure the time after sending the file
                end_time = time.time()
                rtt_ms = (end_time - start_time) * 1000
                print(f"Unicasting data RTT: {rtt_ms:.2f} ms")
                
            else:
                # Broadcast the message to all clients
                for username, socket in clients.items():
                    send_file(received_file_name, socket)
                    socket.close()
                    
                # Measure the time after sending the file
                end_time = time.time()
                rtt_ms = (end_time - start_time) * 1000
                print(f"Broadcasting data RTT: {rtt_ms:.2f} ms")
                    
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")


# Create and configure the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

# Main server loop
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    
    # Add the client to the dictionary
    clients[str(client_address[1])] = client_socket
    
    # Create a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

