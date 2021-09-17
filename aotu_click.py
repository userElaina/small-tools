import win32gui as wg
import win32con as wc
import win32api as wa
import keyboard
from time import sleep as slp
import threading

def throws(f,args:tuple=tuple())->None:
	if not f:
		f=args

	if isinstance(f,(list,tuple)):
		if len(f)==1:
			args=tuple()
		elif len(f)==2:
			args=f[1]
		else:
			args=f[1:]
		f=f[0]

	if not isinstance(args,tuple):
		args=(args,)
		
	_t=threading.Thread(target=f,args=args,daemon=True)
	_t.start()
	return _t

stp=False

def click():
	while True:
		wa.mouse_event(wc.MOUSEEVENTF_LEFTDOWN|wc.MOUSEEVENTF_LEFTUP,0,0)
		slp(0.04)
		wa.mouse_event(wc.MOUSEEVENTF_LEFTDOWN|wc.MOUSEEVENTF_LEFTUP,0,0)
		slp(0.04)
		wa.mouse_event(wc.MOUSEEVENTF_LEFTDOWN|wc.MOUSEEVENTF_LEFTUP,0,0)
		slp(0.59)
		wa.mouse_event(wc.MOUSEEVENTF_RIGHTDOWN|wc.MOUSEEVENTF_RIGHTUP,0,0)
		slp(0.04)
		wa.mouse_event(wc.MOUSEEVENTF_RIGHTDOWN|wc.MOUSEEVENTF_RIGHTUP,0,0)
		slp(0.04)
		wa.mouse_event(wc.MOUSEEVENTF_RIGHTDOWN|wc.MOUSEEVENTF_RIGHTUP,0,0)
		slp(0.19)
		if stp:
			return

while True:
	keyboard.wait('ctrl+alt+m')
	slp(1)
	stp=False
	t=throws(click)
	keyboard.wait('ctrl+alt+m')
	stp=True

