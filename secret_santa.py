from random import randint
import random
random.seed(848836)
oakland = ['francis', 'pat', 'suz', 'matt']
broomfield = ['linda', 'ed']
palm_springs = ['eddie', 'domo']
lafayette = ['mary', 'isaac', 'adrian', 'dusk']
fam = [oakland, broomfield, palm_springs, lafayette]
pairs = {}
b=-1
picked = []
for i in range(4):
	for person in fam[i]:
		while True:
			n=i-randint(1,3)
			pick=fam[n][randint(0,len(fam[n])-1)]
			if pick in picked:
				b+=1
				if b>100:
					raise Exception('Code is broken tell Francis!')
				continue
			else:
				break
		pairs[person]=pick
		picked.append(pick)
print(pairs.keys())
key = input("Enter your key:\n")
key = int(key)
locked_pairs = dict(zip(range(12),pairs.values()))
print(locked_pairs[key])
