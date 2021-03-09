import random

#DICE

d20_possible = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d12_possible = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d10_possible = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d8_possible = [1, 2, 3, 4, 5, 6, 7, 8]
d6_possible = [1, 2, 3, 4, 5, 6]
d4_possible = [1, 2, 3, 4]

#END DICE.
#BEGIN RANDOM.

randomd20 = random.choice(d20_possible)
randomd12 = random.choice(d12_possible)
randomd10 = random.choice(d10_possible)
randomd8 = random.choice(d8_possible)
randomd6 = random.choice(d6_possible)
randomd4 = random.choice(d4_possible)

#END RANDOM.
#BEGIN ABILITIES.

strength = randomd20 - 1
dexterity = randomd20 + 4
constitution = randomd20 + 4
intelligence = randomd20 + 1
wisdom = randomd20 + 2
charisma = randomd20 + 1
acrobatics = randomd20 + 7
animal_handling = randomd20 + 5
arcana = randomd20 + 1
athletics = randomd20 - 1
deception = randomd20 + 1
history = randomd20 + 1
insight = randomd20 + 2
intimidation = randomd20 + 1
investigation = randomd20 + 4
medicine = randomd20 + 8
nature = randomd20 + 1
perception = randomd20 + 5
performance = randomd20 + 1
persuasion = randomd20 + 1
religion = randomd20 + 1
sleight_of_hand = randomd20 + 4
stealth = randomd20 + 10
survival = randomd20 + 5

#END ABILITIES.
#BEGIN INPUT.

ability = input("What are you rolling?	")
ability = str(ability)

if ability == "strength":
	print("You rolled " + str(strength) + "!")
elif ability == "dexterity":
	print(dexterity)
elif ability == "constitution":
	print(constitution)
elif ability == "intelligence":
	print(intelligence)
elif ability == "wisdom":
	print(wisdom)
elif ability == "charisma":
	print(charisma)
elif ability == "acrobatics":
	print(acrobatics)
elif ability == "animal handling":
	print(animal_handling)
elif ability == "arcana":
	print(arcana)
elif ability == "athletics":
	print(athletics)
elif ability == "deception":
	print(deception)
elif ability == "history":
	print(history)
elif ability  == "insight":
	print(insight)
elif ability == "intimidation":
	print(intimidation)
elif ability == "investigation":
	print(investigation)
elif ability == "medicine":
	print(medicine)
elif ability == "nature":
	print(nature)
elif ability == "perception":
	print(perception)
elif ability == "performance":
	print(performance)
elif ability == "persuasion":
	print(persuasion)
elif ability == "religion":
	print(religion)
elif ability == "sleight of hand":
	print(sleight_of_hand)
elif ability == "stealth":
	print(stealth)
elif ability == "survival":
	print(survival)
