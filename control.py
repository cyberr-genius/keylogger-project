from pynput.mouse import Controller
from pynput.keyboard import Controller as keyboardController
def controlMouse():
    mouse=Controller()
    mouse.position = (500,20)

def controlKeyboard():
    keyboard=keyboardController()
    keyboard.type("i'm a super genius")
controlKeyboard()
