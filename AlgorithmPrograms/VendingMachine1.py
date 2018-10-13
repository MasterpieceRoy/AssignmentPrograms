
def vendingMachine(notes, amount, i):
	total = 0
	if amount == 0:
		return
	else:
		if amount >= notes[i]:

			calculatedNotes = amount//notes[i]

			rem = amount % notes[i]

			amount = rem

			total = total + calculatedNotes

			print(notes[i], " notes=", calculatedNotes)
		i += 1
		vendingMachine(notes, amount, i)



class Vending_Machine:
	i = 0
	notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
	amount = int(input("enter the amount"))
	vendingMachine(notes, amount, i)

