import socket
from tkinter import *
import keyboard
import socket



CNT = 1
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())#to be changed

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


keyboard.on_press_key("Enter", lambda _:send_message())

def receive():
       global CNT
       host_msg = client.recv(1024).decode(FORMAT)
       log.insert(CNT, "Main: "+host_msg)
       CNT += 1
def send_message():
       global CNT
       msg = message.get()
       message.set("")
       log.insert(CNT, "YOU: "+msg)
       log.yview_moveto(1)
       CNT += 1
       client.send(msg.encode(FORMAT))


ROOT = Tk()
ROOT.geometry("300x400")
ROOT.maxsize(300, 400)
ROOT.title("Client")

log = Listbox(ROOT, width=25, height=15, relief=SUNKEN, borderwidth=4,font="lucica 15")
log.place(x=0, y=0)
scrollbar= Scrollbar(ROOT, orient= 'vertical')
scrollbar.pack(side= RIGHT, fill= BOTH)
log.config(yscrollcommand= scrollbar.set)
#Configure the scrollbar
scrollbar.config(command= log.yview)

message = StringVar()
message_box = Entry(ROOT, textvariable=message, font="lucica 15", relief=GROOVE, width=20, borderwidth=4)
message_box.place(x=0, y=365)

Button(text="Send", font="lucica 14", relief=RAISED,
       command=send_message).place(x=228, y=360)
Button(text="Receive", font="lucica 10", relief=RAISED,
       command=receive).place(x=230, y=335)


# log.insert(CNT, host_msg)
# CNT +=1
ROOT.mainloop()
