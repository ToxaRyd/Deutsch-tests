
from random import shuffle

b1 = [
['Nominativ - maskulinum', 'ein'],   ['Nominativ - neutrum', 'ein'], ['Nominativ - femininum', 'eine'],
['Genetiv - maskulinum', 'eines'],   ['Genetiv - neutrum', 'eines'], ['Genetiv - femininum', 'einer'],
['Dativ - maskulinum', 'einem'],     ['Dativ - neutrum', 'einem'],   ['Dativ - femininum', 'einer'],
['Akkusativ - maskulinum', 'einen'], ['Akkusativ - neutrum', 'ein'], ['Akkusativ - femininum', 'eine'],
]

b2 = [
['Nominativ - maskulinum', 'der'], ['Nominativ - neutrum', 'das'], ['Nominativ - femininum', 'die'], ['Nominativ - plural', 'die'],
['Genetiv - maskulinum', 'des'],   ['Genetiv - neutrum', 'des'],   ['Genetiv - femininum', 'der'],   ['Genetiv - plural', 'der'],
['Dativ - maskulinum', 'dem'],     ['Dativ - neutrum', 'dem'],     ['Dativ - femininum', 'der'],     ['Dativ - plural', 'den'],
['Akkusativ - maskulinum', 'den'], ['Akkusativ - neutrum', 'das'], ['Akkusativ - femininum', 'die'], ['Akkusativ - plural', 'die'],
]

b3 = [
['in + dem', 'im'], ['in + das', 'ins'], ['an + das', 'ans'], ['an + dem', 'am'], ['auf + das', 'aufs'],
['von + dem', 'vom'], ['um + das', 'ums'], ['zu + dem', 'zum'], ['zu + der', 'zur'],
]

def main():

	print('\nВыбор доступных тестов:', '\n1. Склонение неопределенного артикля', '\n2. Склонение определенного артикля', '\n3. Слияние артикля с предлогом')

	try:
		a = int(input('\n Введите номер желаемого теста: '))
	except ValueError:
		input('\nНеверное значение!')
		main()
	
	print('\n')

	if a == 1:
		first(b1)

	elif a == 2:
		first(b2)

	elif a == 3:
		first(b3)

	else:
		input('Такого теста нет!')
		main()

def first(b):

	shuffle(b)

	print('*'*50, '\n')

	d = 0

	for i in b:
		c = input(f'{i[0]}: ').lower().replace(' ', '')
		if c == i[1]:
			print('Правильно!\n')
			d += 1
		else:
			print(f'Неверно! Правильно будет - {i[1]}\n')

	print('*'*50, '\n')
	input(f'Результат - {d} правильных ответов из {len(b)}-ти\n')
	print('*'*50, '\n')
	main()

main()
