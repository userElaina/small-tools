import os
import ctypes
import platform

def fspace(folder):
	if platform.system()=='Windows':
		free_bytes=ctypes.c_ulonglong(0)
		ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder),None,None,ctypes.pointer(free_bytes))
		return free_bytes.value
	else:
		st=os.statvfs(folder)
		return st.f_bavail*st.f_frsize

def renhua(x:int):
	i=0
	while x>512 and i<8:
		x=x/1024
		i+=1
	return str(round(x,2))+('BKMGTPEZY'[i])

def get_bytes(x:int,l:int):
	if x==0:
		return b'\x00'*l
	if x==1:
		return b'\xff'*l
	if x==2:
		return os.urandom(l)
	if x==3:
		nmsl=b'Hello, are you trying to find your family\'s ashes from my hard drive? \n'
		return (nmsl*((len(nmsl)+l-1)//len(nmsl)))[:l]

def clear(pth:str='./',n:int=2,m:int=1,chunk_size=1024*1024,file_size=3600):
	pth=os.path.abspath(pth)

	num_b=int(fspace(pth))
	num_chunk=num_b//chunk_size
	num_file=num_chunk//file_size
	mo=num_chunk%file_size

	s='During this hard disk erasing, the '
	s+=renhua(num_b)
	s+=' free space of the hard disk where path "'
	s+=pth
	s+='is located will be overwritten multiple times in chunk sizes of '
	s+=renhua(chunk_size)
	s+=' and file sizes of '
	s+=str(file_size)
	s+=' chunks ('
	s+=renhua(num_chunk*file_size)
	s+=').\n'
	s+='Warning: A hard disk erasing will cause irreversible damage to your hard disk.\n'
	s+='Are you sure you want to perform a hard disk erasing? (Y/n)'
	print(s,end='')

	if input()!='Y':
		print('EXIT')
		input()
		exit()

	i2f=lambda x:os.path.join(pth,str(x)+'.disk_eraser')
	for _x in range(n):
		for _y in range(3):
			for i in range(num_file):
				f=open(i2f(i),'ab')
				for j in range(file_size):
					f.write(get_bytes(_y,chunk_size))
			f=open(i2f(num_file),'ab')
			for j in range(mo):
				f.write(get_bytes(_y,chunk_size))

			for _z in range(m):
				for i in range(num_file):
					open(i2f(i),'wb')
					f=open(i2f(i),'ab')
					for j in range(file_size):
						f.write(get_bytes(_y,chunk_size))
				open(i2f(num_file),'wb')
				f=open(i2f(num_file),'ab')
				for j in range(mo):
					f.write(get_bytes(_y,chunk_size))

			for i in range(num_file+1):
				os.remove(i2f(i))

clear()
