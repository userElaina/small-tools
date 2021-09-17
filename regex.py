# 匹配一个字符串，其由且仅由偶数个0和奇数个1组成，不论顺序。

import re

def test(p:str,m:int):
	for i in range(m):
		for j in range(1<<i):
			s=bin(j)[2:].zfill(i)
			a=re.fullmatch(p,s)

			l=len(s)
			l1=len(s.replace('0',''))
			l0=len(s.replace('1',''))

			if bool(a)!=bool(l&l1&1):
				print(s,'l0:',l0,'l1:',l1,a.group(0),bool(l&l1&1))

test(r'(?=^1*((01*){2})*$)(^([01]{2})*[01]$)',20)
test(r'(?=^([01]{2})*[01]$)(^0*((10*){2})*(10*)$)',20)
test(r'(?=^0*((10*){2})*(10*)$)(^1*((01*){2})*$)',20)
test(r'1(00|11)*((01|10)(00|11)*(01|10)(00|11)*)*|0(00|11)*(01|10)(00|11)*((01|10)(00|11)*(01|10)(00|11)*)*',20)