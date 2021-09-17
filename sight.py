import sys
import tkinter as tk

l=sys.argv[1:]

js=dict()
for j in range(len(l)):
	i=l[j]
	if i.startswith('-'):
		try:
			js[i[1:]]=l[j+1]
		except:
			js['h']=1

if 'help' in js or 'h' in js:
	print('sight -x 1920 -y 1080 -color #ff0000 -name sight -r 20 -wd 6 -len 40')
	exit()


def u(k:str,v:all,t:type=int):
	if k not in js:
		js[k]=v
	js[k]=t(js[k])

u('waits',0.2,float)
u('alpha',0.4,float)
u('name','sight',str)
u('color','#ff0000',str)

if 'x' not in js and 'cx' not in js:
	import win32api,win32con
	js['x']=win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
if 'y' not in js and 'cy' not in js:
	import win32api,win32con
	js['y']=win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

u('cx',js['x']//2)
u('cy',js['y']//2)
mn=js['y'] if js['y']<=js['x'] else js['x']
u('r',mn//50)
u('len',js['r']*2)
u('wd',js['r']//6*2)

l=[
	str(js['wd'])+'x'+str(js['len'])+'+'+str(js['cx']-js['wd']//2)		+'+'+str(js['cy']-js['r']-js['len']),
	str(js['len'])+'x'+str(js['wd'])+'+'+str(js['cx']-js['len']-js['r'])+'+'+str(js['cy']-js['wd']//2),
	str(js['wd'])+'x'+str(js['len'])+'+'+str(js['cx']-js['wd']//2)		+'+'+str(js['cy']+js['r']),
	str(js['len'])+'x'+str(js['wd'])+'+'+str(js['cx']+js['r'])			+'+'+str(js['cy']-js['wd']//2),
]


def f(s):
	# print(s)
	qwq=tk.Tk()
	qwq.geometry(s)
	qwq.title(js['name'])
	qwq.wm_attributes('-alpha',float(js['alpha']))
	qwq.overrideredirect(1)
	qwq.wm_attributes('-topmost',True)
	tk.Label(
		qwq,
		text='        \n        ',
		font=('',64),
		bg=js['color'],
	).pack()
	qwq.mainloop()

import downs
a=downs.nThread(waits=js['waits'],f=f,args=l,fast=True)