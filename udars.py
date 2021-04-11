import json

file = open('udars.txt', encoding='UTF-8')
s = file.read()
file.close()
vowels = 'аеёиоуыэюя'
ans = []

for x in s.splitlines():
	x = x.replace('Ё', 'Е')
	toAns = {'correct':x, 'all':[]}
	cntCorrectUdars = 0
	for i, s in enumerate(x.lower()):
		if s in vowels:
			if x[i].isupper():
				cntCorrectUdars += 1
			toAns['all'].append(x.lower()[:i]+x[i].upper()+x.lower()[i+1:])
		elif s == '(':
			break
	if cntCorrectUdars == 1:
		ans.append(toAns)
	else:
		print(x, 'is error')

jsonAns = json.dumps(ans, indent=4, sort_keys=True)
file = open('udars.json', 'w', encoding='UTF-8')
file.write(jsonAns)
file.close()