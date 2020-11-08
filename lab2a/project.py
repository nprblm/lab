name='Vitalii'
print("2.1")
print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)

print("\n2.2")
print ("z in ASCII(Dec) = ", ord('z'))
print ("122 in ASCII(Char) = ", chr(122))
print (f"Lenght of my name {name} = ", len(name))

print("\n2.3")
print("What is your name? ==> ")
name = input()
if name == 'Vitalii':
    print("You are the owner of this code")
else :
    print("You are not the owner of this code")

k=1
for i in name:
    print(f"Number of letter in name = {k} = {i}")
    k=k+1
    
lenname=int(len(name))
enterlenght=0
while lenname != enterlenght:
    print("Enter lenght of your name ==>")
    enterlenght=int(input())

print("\n2.4")

try:
    print("Що буде якщо int + str?")
    10 + '5'
except Exception as e:
    print(e)
finally:
    print("Зрозуміло")

print("\n2.5")
print('Запишем щось у файл test.txt')
with open('test.txt', 'w', encoding='utf-8') as g:
    d = input()
    print(f'{d}', file=g)

print("\n2.6")
lambda_1 = lambda name, age: f'My name is {name} and my age is {age}'
print(lambda_1('Vitalii',19))
