import os
import sys
import time
import psutil

try:
	lmt=abs(int(sys.argv[1]))
except:
	lmt=10

def pt(x):
	print(str(x))
	open('battery_listener.log','ab').write(str(x).encode('utf8')+b'\n')

def listen(lmt:int=10,waits:int=60,command:str='shutdown -s -t 60',):
	pt('It will "'+command+'" when the power level <= %d%s'%(lmt,'%'))
	old_isplugged=None
	while True:
		b=psutil.sensors_battery()
		e=b.percent

		isplugged=b.power_plugged
		if isplugged!=old_isplugged:
			ans='Switch to '+('AC!' if isplugged else'Battery!')
			pt(ans)
		old_isplugged=isplugged

		t=time.localtime()
		ans='%d:%d %d%s'%(t.tm_hour,t.tm_min,e,'%',)
		pt(ans)

		if e<=lmt:
			pt(': '+command)
			os.system(command)
		time.sleep(waits)

listen()
