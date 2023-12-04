import socket
import threading
import time
import os

#=============== File wrote by Clément MALON ==================================

# Client configuration
HOST = 'localhost'
PORT = 12345

# Function to handle receiving messages from the server
def receive_messages(sock):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        
        message = data.decode('utf-8')
        received_file_name = 'Another' + os.path.basename("".join(message.split(" ")[("@" in message):]))
        print(f"File '{received_file_name}' received successfully")
 
        with open(received_file_name, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        
def send_file(file_name, connection):
    # Send the original file name first
    connection.sendall(file_name.encode('utf-8'))
    file_name = "".join(file_name.split(" ")[("@" in file_name):])
    with open(file_name, 'rb') as file:
        for data in file:
            connection.sendall(data)
    print(f"File '{file_name}' sent successfully")
            
# Create and configure the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Main client loop
while True:
    # Measure time to send the file
    start_time = time.time()
    
    file_name = input("Which file do you want to send ?\n")
    send_file(file_name, client_socket)
    
    # Measure the time after sending the file
    end_time = time.time()
    
    # Calculate the Round Trip Time (RTT) in milliseconds
    rtt_ms = (end_time - start_time) * 1000
    print(f"Sending data RTT: {rtt_ms:.2f} ms")
    
    time.sleep(1)   # Break of 1 second for more clarity in console
    client_socket.close()
    
