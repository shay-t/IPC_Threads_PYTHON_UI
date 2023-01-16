from threading import Thread
import socket
import sys,time
from PyQt5 import QtWidgets , uic,QtGui
def Send():
    msg=sc.txte.toPlainText()
    msg2=msg
    if(msg != ""):
        msg = msg.encode("utf-8")
        client.send(msg)
        sc.txte.setPlainText("")
        sys.stdout = open("output.txt", "a")
        print("<span style='color:yellow'><b>Server</b></span> :"+msg2+"<br/>")  
        sys.stdout.close()   
    f=open("output.txt",'r')
    sc.txt.setHtml(f.read())
    f.close()
def rec():
    recep.start()
def Reception():
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf-8')
        out="Client :"+str(requete_client)
Host = "127.0.0.1"
Port = 6390
#Création du socket
socket = socket.socket()

socket.bind((Host,Port))
socket.listen(1)

#Le script s'arrête jusqu'a une connection
client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")
recep = Thread(target=Reception,args=(), daemon=True)
if __name__== '__main__':
    App=QtWidgets.QApplication(sys.argv)
    sc=uic.loadUi("IPC.ui")
    sc.setWindowTitle("Server")
    sc.send_2.clicked.connect(Send)
    sc.actionreceive.triggered.connect(rec)
    sc.show()
    App.exec_()
    App.exit()
client.close()
socket.close()
