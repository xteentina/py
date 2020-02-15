a = 2
b = 0.5
print (a+b);

name = 'Кристина'
#a = 'Привет,'
print ('Привет,' + ' ' + name + '!');


name = 'Кристина'
#a = 'Привет,'
a = 2
b = 'Строка666'
print (f'Привет, {name}!')
print (type(name))
print (type(a))
print (type(b));


name = input ('Введите ваше имя: ')
print (f'Привет, {name}');

age = int (input('Сколько вам лет?'))
birth_year = 2020 - age
print (f'Вы родились в {birth_year} году');


#Ещё одна практика
#1
v = input ('Введите число от 1 до 10: ')
print (int (v) + 10);

#2.1
name = input ('Введите ваше имя: ')
print ('Привет, ' + name + '! Как дела?');

#2.2
name2 = input ('Введите ваше имя: ')
print (f'Привет, {name2}! Как дела???')


#3
print (float('1'), #int('2.5'), 
bool(1), bool(''), bool(0))


#Lists
num = [3,5,7,9,10.5]
print (num)


num.append('Python')
print (len(num))


#2
print (num[0])
print (num[-1])
print (num[1:4])

num.remove('Python')
print(num)


#Dict
#1
weather = {
    'city':'Москва',
    'temperature':'20'
}
print (weather['city'])

weather['temperature'] = int(weather['temperature']) - 5
print (weather['temperature'])

print(weather)

#2
print(weather.get('country'))

print(weather.get('country', 'Россия'))

weather['date'] = '27.05.2019'

print(len(weather))

print(weather);
