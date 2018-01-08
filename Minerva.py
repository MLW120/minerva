input_layer = [0 for i in range(10)]
count_layer = [0 for i in range(8)]
output_layer = [0 for i in range(13)]
class abc:
	bool_to_exit = True
	position_of_mover = 0
text_to_print = '''
1: ADD
2: SUBSTRACT
3: CHANGE NUMBERS OF IMPUT
4: MOVE MOVER
5: RESET COUNTER
6: RESET OUTPUT
7: RESET BOTH
8: Help
9: QUIT
'''	

help_string = '''
Your calculator has three indicators:
1) Input: A indicator you can manipulate freely as you want.
2) Output: Shows the result of your operation and stores that value until you 
delete it.
3) Counter: Counts the amount of addition and substarctions in each position 
of the mover. Also you have a mover that enables the option to decide to which 
positions of the output to add or substract your imput.
If your mover position is equal to 1 then you will add the right number of the 
input to the right number of the output. 
If it is equal to 2 then your will add the right number of the input to the 
second number (counting from the right).
You can do two operations:
1) Add: Add the number of the Input to the one in the output.
2) Substraction: Substract the number of the Input of the one in the output.
Note: The numbers in the input and output can only be positiv!
How to calculate:
1) Addition: Set the output to 0, put the first number in the input and add 
once, put the second number in the input and add again. Your result is in the 
output.
2) Substraction: Set the output to 0, add the first number to the output and 
then substract, the second number.
3) Multiplication: Set counter and output to 0, put one number in the input 
and add in the diferent mover position so the second number is displayed in 
the counter. Your result is in the output.
4) Division: Put your first number in the output and substract as often as 
possible the second number in each mover position so the output gets 0. Your 
result is in the counter.
'''

def show():
	print('Input: ' + str(input_layer))
	print('Output: ' + str(output_layer))
	print('Counter: ' + str(count_layer))
	print('Mover at position: ' + str(pb.position_of_mover + 1))
	

def change_number():
	for i in range(len(input_layer)):
		input_layer[i] = int(input('Which number do you want to store ' +
		                       'in the Slot ' + str(i + 1) + " of " + 
							   str(len(input_layer)) + " : "))
							   
def clear_counter():
	for i in range(len(count_layer)):
		count_layer[i] = 0

def clear_output():
	for i in range(len(output_layer)):
		output_layer[i] = 0
		
def turn_add():
	for i in range(len(input_layer)):
		if get_index(i) >= 0:
			add_with_carry(i)
	# counter
	add_to_counter(pb.position_of_mover, 1)
	
def turn_substract():
	for i in range(len(input_layer)):
		if (i + pb.position_of_mover) < len(output_layer):
			substract_with_carry(i)
	# counter
	add_to_counter(pb.position_of_mover, -1)
	
def add_with_carry(i):
	# suma
	output_layer[get_index(i)] += input_layer[i]
	# carry
	if output_layer[get_index(i)] == 10:
		output_layer[get_index(i)] = 0
		repeat = True
		int = 1
		while repeat:
			if (get_index(i) - int) >= 0:
				if output_layer[get_index(i) - int] != 9:
					output_layer[get_index(i) - int] += 1
					repeat = False
				else:
					output_layer[get_index(i) - int] = 0
					int += 1
			else:
				repeat = False
	
def substract_with_carry(i):
	# resta
	output_layer[get_index(i)] -= input_layer[i]
	# carry
	if output_layer[get_index(i)] < 0:
		output_layer[get_index(i)] += 10
		repeat = True
		int = 1
		while repeat:
			if get_index(i) - int >= 0:
				if output_layer[get_index(i) - int] != 0:
					output_layer[get_index(i) - int] -= 1
					repeat = False
				else:
					output_layer[get_index(i) - int] = 9
					int += 1
			else:
				repeat = False
def add_to_counter(slot_num, number_to_add):
	count_layer[7 - slot_num] += number_to_add
	if count_layer[7 - slot_num] == -10:
		count_layer[7 - slot_num] = 8
	if count_layer[7 - slot_num] == 10:
		count_layer[7 - slot_num] = -8
		
def move_mover(quantity_of_slots):
	positiv_or_negativ = 1
	if quantity_of_slots < 0:
		positiv_or_negativ = -1
		quantity_of_slots = quantity_of_slots * (-1)
	
	for i in range(quantity_of_slots):
		pb.position_of_mover += quantity_of_slots * positiv_or_negativ
		if pb.position_of_mover < 0: pb.position_of_mover = 0
		if pb.position_of_mover > 7: pb.position_of_mover = 7
		
def get_index(int):
	return int + 3 - pb.position_of_mover
	
def help():
	print(help_string)
	
def interface():
	print(text_to_print)
	action_to_do = int(input('Type the number of what you want to do! '))
	if action_to_do == 1:
		turn_add()
		print('ADDED')
	elif action_to_do == 2:
		turn_substract()
		print('SUBSTRACTED')
	elif action_to_do == 3:
		change_number()
		print('CHANGED')
	elif action_to_do == 4:
		i = int(input('How many steps?'))
		move_mover(i)
		print('MOVED')
	elif action_to_do == 5:
		clear_counter()
		print('CLEARD')
	elif action_to_do == 6:
		clear_output()
		print('CLEARD')
	elif action_to_do == 7:
		clear_counter()
		clear_output()
		print('CLEARD')
	elif action_to_do == 8:
		help()
	elif action_to_do == 9:
		pb.bool_to_exit = False
		print('EXIT')
	show()

pb = abc
while pb.bool_to_exit:	
	interface()

