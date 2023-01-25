'''1) Из строки «Python is the best programming language in the world» получить
подстроку начиная с 6 символа с начала исходной строки и до 7 символа с конца исходной
строки (нумерация символов начинается с нуля).'''
s = 'Python is the best programming language in the world'
s = s[5:-7]
print(s)

'''2) Вывести каждый третий символа строки «Guido van Rossum is the benevolent dictator for life».'''
s = 'Guido van Rossum is the benevolent dictator for life'
print(s[2::3])

'''4) Из строки «You have a problem with authority, Mr. Anderson.» получить словарь, где ключ -это символ, 
а значение - это количество повторений символа в строке.
Пример результата
{'A': 1, 'l': 1, 'o': 4,..}
Используйте функциональный подход (а не циклы), для этого ознакомьтесь с функцией map и zip
Для справки в интерактивном режиме наберите help(map) и help(zip)
Пример работы map()
>> list( map(len, ['a','aaa']) )
>>[1, 3]
Пример работы zip()
>> list( zip(['a', 'b'], [1, 2]))
>> [('a', 1), ('b', 2)]
'''
s = 'You have a problem with authority, Mr. Anderson.'
t = list(map(s.count, s))
##print(t)
u = list( zip(s, t))
##print(u)
v = dict(u)
print(v)
