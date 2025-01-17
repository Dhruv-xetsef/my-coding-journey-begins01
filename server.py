import socket
import threading

HOST = '127.0.0.1'
PORT = 7249  # some lam=ndom number between  0 to 65000s
SERVER_LIMIT = 3
active_clients = []  # it is the list of all the connected users to the chat app madeit empty so that later the usrs can be added thrugh the property os the list


def listen_for_messages(client, username):  # this function will read all the messages that will be comming from the users
    while True:
        try:
            message = client.recv(2048).decode('utf-8') 
            if message != "":
                final_message = f"{username} --> {message}"
                send_messages_to_all(final_message, client)
            else:
                print(f"The message sent by the other user {username} is as empty")
        except Exception as e:
            print(f"Error receiving message from {username}: {e}")
            remove_client(client)
            break


def send_message_to_client(client, message):  # functiion to send message to single client instead of sending to everone on the server
    try:
        client.sendall(message.encode())
    except Exception as e:
        print(f"Error sending message to client: {e}")


def send_messages_to_all(message, sender_client):  # send the message to all the clients that has beem connected to the server
    for user in active_clients:
        if user[1] != sender_client:  # Avoid sending the message back to the sender
            send_message_to_client(user[1], message)


def remove_client(client):  # Remove a client from the active clients list when they disconnect
    for user in active_clients:
        if user[1] == client:
            active_clients.remove(user)
            break


def client_handler(client):  # function to handle the client side data
    while True:  # this loop is for reading the user messages that contains a valid user name here just the valid user is anything accept a empty log but one can use contxt variacle for checkind of valid database
        try:
            username = client.recv(2048).decode('utf-8') 
            if username != "":
                active_clients.append((username, client))
                prompt_message = f"The user named {username} has successfully registered to the server."
                send_messages_to_all(prompt_message, client)
                break
            else:
                print("Client name is empty. Please provide a valid name.")
        except Exception as e:
            print(f"Error handling client: {e}")
            return

    threading.Thread(target=listen_for_messages, args=(client, username)).start()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # here the AF_NET  is used to take ipv4 address one can use ipv6 also and the sock_stream is for tcp packets of communication
    try:  # here try blockis made to handle and catch error
        server.bind((HOST, PORT))  # here the server is being provided with the server address in form of host ip and port 
        print(f"The server is running on the host {HOST} and the port {PORT}")
    except Exception as e:
        print(f"Unable to connect to the user to the host {HOST} AND THE PORT {PORT}: {e}") 
        return

    server.listen(SERVER_LIMIT)  # here the server limit is being added to theb code throught the variable server_limit that is the variable that is been passed above
    print(f"Server is listening with a limit of {SERVER_LIMIT} connections.")

    while True:  # reads the client connections communication through this whil loop
        try:
            client, address = server.accept()
            print(f"The connection has been set up to client {address[0]} {address[1]}")
            threading.Thread(target=client_handler, args=(client,)).start()
        except Exception as e:
            print(f"Error accepting client connection: {e}") 


if __name__ == "__main__":
    main()

