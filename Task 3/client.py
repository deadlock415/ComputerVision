#CLient Side
import socket
import pickle
import cv2
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",2222))

cap=cv2.VideoCapture(0)

while True:
    ret,photo=cap.read()
    picb=pickle.dumps(photo)
    s.send(picb)
    cv2.imshow("Client",photo)
    if cv2.waitKey(10) == 13:
        cv2.destroyAllWindows()
        cap.release()
        break
    print("Sending Frame")