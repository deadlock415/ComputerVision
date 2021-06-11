#Server Side
import socket
import pickle
import cv2

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",2222))
s.listen()

client,addr=s.accept()

while True:
#I Use to make a msg blank everytime to avoid truncatened
    msg=b""
#Provide a Direct Buffer Size which causing so fast connection
    msg=client.recv(921767)
    client.send(b'we got frame')
    print("Converting Bytes into Frames")
    load_img=pickle.loads(msg)
    print("Downloading Frames")
#Showing Streaming    
    cv2.imshow("Server",load_img)
    if cv2.waitKey(10) == 13:
        cv2.destroyAllWindows()
        break

#Closing Connection with Client
s.close()     