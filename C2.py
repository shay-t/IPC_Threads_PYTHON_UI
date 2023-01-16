from threading import Thread
import socket
import sys,time
from PyQt5 import QtWidgets , uic,QtGui
def Send():
    msg=sc2.txte.toPlainText()
    msg2=msg
    if(msg != ""):
        msg = msg.encode("utf-8")
        socket.send(msg)
        sc2.txte.setPlainText("")
        sys.stdout = open("output.txt", "a")
        print("<span style='color:red'><b>Client</b></span>:"+msg2+"<br/>")  
        sys.stdout.close()  
    f=open("output.txt",'r')
    sc2.txt.setHtml(f.read())
    f.close()
def rec():
    recep.start() 
def Reception():
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode("utf-8")   
        out="Server :"+str(requete_server)
        #sys.stdout = open("output.txt", "a")
        #print(out)  
        #sys.stdout.close() 
Host = "127.0.0.1"
Port = 6390
#Création du socket
socket = socket.socket()
socket.connect((Host,Port))
recep = Thread(target=Reception,args=(), daemon=True)
if __name__== '__main__':
    App=QtWidgets.QApplication(sys.argv)
    sc2=uic.loadUi("IPC.ui")
    sc2.setWindowTitle("Client")
    sc2.send_2.clicked.connect(Send)
    sc2.actionreceive.triggered.connect(rec)
    sc2.show()
    App.exec_()
    App.exit()
socket.close()
