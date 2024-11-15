import json
import random
from datetime import date
from datetime import datetime
import os
# Generate a new seed based on the current year
current_year = date.today().year
random.seed(current_year)
b=0
fam=[]
units = {1:[]}
user_input = input(' [1] New\n [2] Load\n')
while True:

	if user_input in ['1', '2']:
		break
	else:
		b+=1
		print('Please input 1 or 2')
		if b > 10:
			user_input = '1'
		else:
			user_input = input(' [1] New\n [2] Load\n')
			continue

if user_input == '2':
	options = os.listdir('data/participants/')
	if options:
		a = 1
		for o in options:
			print(f'[{a}]: ', o)
			a+=1
		while True:
			user_input = input('Select your participants via index.\n')
			try:
				user_input = int(user_input)
				selection = options[user_input-1]
				break
			except:
				print('Please enter a valid index.')
		with open(f'data/participants/{selection}', 'r') as f:
			units = json.load(f)
	else:
		print('No valid data, please create a new entry.')
		user_input = '1'

n = 1
if user_input == '1':
	print("Enter participant's names, participants in the same unit will not be paired.\nEnter 'Next!' to go to the next unit.\nEnter 'Done!' to finalize your participants.\nEnter 'Help!', for other opitions")
	while True:
		user_input = input(f'Add a participant to family unit {n}:\n')
		if user_input == 'Help!':
			user_input = input("Enter Units! to navigate to an existing unit and see all unit's contents.\nEnter Remove! to remove a name from this unit.\n")

		if user_input == 'Units!':
			a = 1
			for u in units.values():
				print(f'[{a}]: ', u)
				a+=1
			while True:
				n = input('Enter the number of the unit you wish to edit:\n')
				try:
					n = int(n)
					if n not in units.keys():
						units[n] = []
					break
				except:
					print('Please enter a valid index.')
			continue

		if user_input == 'Remove!':
			units[n].remove(input('Enter the value you wish to remove:\n'))
			print(units[n])
			continue
		if user_input == 'Next!':
			n += 1
			if n not in units.keys():
				units[n] = []
			continue
		if user_input == 'Done!':
			keys_to_remove = [key for key, value in units.items() if value == []]
			for key in keys_to_remove:
				units.pop(key)
			user_input = input('Please name the group or hit enter for the default.\n')
			if user_input == '':
				user_input = datetime.now(	)
			with open(f"data/participants/participants-{user_input}.json", "w") as f:
				json.dump(units, f)
			break
		units[n].append(user_input)



all_fam = []
fam = list(units.values())
random.shuffle(fam)
for f in fam:
	all_fam += f
def make_pairs(fam, all_fam):
	pairs = {}
	picked = []
	for f in fam:
		for person in f:
			valid_picks = [p for p in all_fam if p not in picked and p not in f]
			pick = random.choice(valid_picks)
			# print(f"Person: {person}, Valid Picks: {valid_picks}")
			# pick = random.choice([p for p in all_fam if p not in picked and p not in f])
			pairs[person] = pick
			picked.append(pick)
			# print(pairs)
	return pairs
i = 0
while i < 25:
	try:
		pairs = make_pairs(fam, all_fam)
		break
	except Exception as e:
		print(f"Error during pairing: {e}")
		random.shuffle(fam)
		i+=1
		if i == 25:
			raise RuntimeError("Failed to generate valid pairs after 25 attempts.")
# Anonymize pairs with keys
locked_pairs = dict(zip(range(len(all_fam)), pairs.values()))
print('Distribute the key #s to individual participants:\n',dict(zip(range(len(all_fam)), pairs.keys())))
# print(pairs)
# Save to a JSON file
with open("data/pairs.json", "w") as f:
    json.dump(locked_pairs, f)
