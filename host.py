from tkinter import *
import keyboard
import socket
import threading

CNT = 1
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"[Listening on]:- {SERVER} ")
conn, addr = server.accept()




def receive():
    global CNT
    host_msg = conn.recv(1024).decode(FORMAT)
    log.insert(CNT, "They: "+host_msg)
    CNT += 1


def send_message():
    global CNT
    msg = message.get()
    message.set("")
    log.insert(CNT, "YOU: "+msg)
    log.yview_moveto(1)
    CNT += 1
    conn.send(msg.encode(FORMAT))
    #todo:



keyboard.on_press_key("Enter", lambda _:send_message())


ROOT = Tk()
ROOT.geometry("300x400")
ROOT.maxsize(300, 400)
ROOT.title("Admin")

log = Listbox(ROOT, width=25, height=15, relief=SUNKEN, borderwidth=4,font="lucica 15")
log.place(x=0, y=0)
scrollbar= Scrollbar(ROOT, orient= 'vertical')
scrollbar.pack(side= RIGHT, fill= BOTH)
log.config(yscrollcommand= scrollbar.set)
#Configure the scrollbar
scrollbar.config(command= log.yview)

message = StringVar()
message_box = Entry(ROOT, textvariable=message, font="lucica 15", relief=GROOVE, width=25, borderwidth=4)
message_box.place(x=0, y=365)

Button(text="Send", font="lucica 14", relief=RAISED,
       command=send_message).place(x=228, y=360)
Button(text="Receive", font="lucica 10", relief=RAISED,
       command=receive).place(x=230, y=335)

ROOT.mainloop()





