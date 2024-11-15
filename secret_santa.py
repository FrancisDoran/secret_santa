import random
random.seed(848836)
oakland = ['francis', 'pat', 'suz', 'matt']
broomfield = ['linda', 'ed']
palm_springs = ['eddie', 'domo']
lafayette = ['mary', 'isaac', 'adrian', 'dusk']
fam = [oakland, broomfield, palm_springs, lafayette]
all_fam = oakland + broomfield + palm_springs + lafayette
pairs = {}
picked = []
for i in range(4):
	for person in fam[i]:
		pick = random.choice([p for p in all_fam if p not in picked and p not in fam[i]])
		pairs[person]=pick
		picked.append(pick)
key = input("Enter your key:\n")
key = int(key)
locked_pairs = dict(zip(range(12),pairs.values()))
print(locked_pairs[key])
print(pairs)
