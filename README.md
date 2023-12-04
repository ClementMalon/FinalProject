# FinalProject
Codes for the Computer Network Final Project directed by Mr.Pirahandeh

Concerning Python  Codes (Adam KHALIL and Clément MALON)

The two Python codes files allow a client to send a file to one or many other clients.
If the sender wants to broadcast the file, just enter the name of the file and press Enter. The broadcast is set by default.
However, if the sender wants to send the file to a specific client, he can do that by typing : @{SerialNumber of the user} {name of file}.
The server will make a copy of the file and send it to the specific user.

In the example below, we have tested the send file function with a jpg file.
![CaptureSendingJPG](https://github.com/ClementMalon/FinalProject/assets/92983136/9de672f1-5fa8-4e57-96ac-d63a9e2284c7)

In the example below, we have tested the broadcast/unicast function with messages.
![CaptureBroadcastMessages](https://github.com/ClementMalon/FinalProject/assets/92983136/8980ae1b-6326-4d55-8c4b-c37c7825c2dd)

Final Result : In the example below, the sender has broadcast a JPG file and we can see that the two other clients received it.
![CaptureBroadcastJPG](https://github.com/ClementMalon/FinalProject/assets/92983136/565cc9a5-d748-4eac-9c00-3096c9e818af)

=================================================================================================================================================

Concerning Packet Tracer (Maxime JIN and Pierre COURTEMANCHE)

This is the schema of our Packet Tracer architecture with 2 rooms, each have 2 rooms with 2 computers and an open space with 5 computers.
![SchemaPacketTracer](https://github.com/ClementMalon/FinalProject/assets/92983136/6080e677-7011-40dc-bca9-17997f4f5153)

Example of Unicast 
![UnicastPacketTracer](https://github.com/ClementMalon/FinalProject/assets/92983136/61de1922-00ab-49c9-9930-863c680755b0)

Example of Broadcast
![BroadcastPacketTracer](https://github.com/ClementMalon/FinalProject/assets/92983136/bd0c7b0e-a33f-4dc2-9ee7-56ef6843a3ab)

=================================================================================================================================================

Concerning Packet Tracer (Clément MALON)

Here are the results of sending a JPG file from a client to the server.
We can see a lot of TCP segments of a reassembled PDU because the JPG file is send by chunks of data.
At the end, we can see a line with 'FIN' confirming that the entirety of the file has been received.
![Wireshark](https://github.com/ClementMalon/FinalProject/assets/92983136/6760099d-f896-471e-8655-2b1ac4668505)
