
# Написать программу на Python, которая советует пользователю подходящие игры из Steam на основе ответов пользователя 
# в опросе.
# Программа должна обеспечивать:
# •   Диалоговый интерфейс с пользователем. Система последовательно узнает об интересующих жанрах, катерогиях, 
# платформах и т.д. (соответственно полям в csv файле). Например:
# •   Какой жанр игры вас интересует?
# •   >>> RPG, Adventure
# •   Какая категория?
# •   >>> # если пустая строка, то  пользователю это не очень важно
# ...
# •   Поиск в файле steam.csv названий подходящих пользователю игр
# •   Формирование отчета в виде файла
# Вход программы: Файл steam.csv
# Выход программы: Отчет в виде файла

import csv


##формирование критериев поиска в диалоге с пользователем
user_request = dict() #словарь-содержание запроса пользователя
parameters = list() #заголовок csv файла для записи ответа
with open('steam.csv', mode='r', encoding = 'utf-8-sig') as file:
    for parameter in file.readline().rstrip('\n').split(','): 
        #rstrip('\n') - убирает символ конца строки \n в конце строки
        parameters.append(parameter)
        user_request[parameter] = input(f'input desired "{parameter}": ')
print('===========================')
print('searching for this request:\n', user_request)
print('===========================')

##поиска по запаросу пользователя
i = 0 #ограничение на число строк для отладки
w_flag = False
with open('steam.csv', mode='r', encoding = 'utf-8-sig', newline='') as src_csv_file:
    data_src = csv.DictReader(src_csv_file)
    for row in data_src:
        print(row)
        r_flag = True
        for parameter in user_request.keys():
            print(f'Searching "{user_request[parameter].lower()}" in /{parameter} : "{row[parameter].lower()}"/')
            if (user_request[parameter].lower() in row[parameter].lower()): #.lower() - для совпадения регистров
                print('Match!')
            else:
                print(f'MISMATCH, going to next candidate!')
                r_flag = False
                break
        if r_flag:
            print(f'Full request MATCH found! Wrirting to "result.csv" => game: "{row[parameters[1]]}"')
            with open('result.csv', mode='a', encoding = 'utf-8-sig', newline='') as trg_csv_file:
                writer = csv.DictWriter(trg_csv_file, fieldnames=parameters)
                if not w_flag: #заголовок для csv фалйа пишем только для первой строки
                    writer.writeheader()
                writer.writerow(row)
                w_flag = True
        print('-------------------------')
        
        

        # #ограничение на число строк для отладки
        # i += 1;
        # if i == 20:
        #     break

print('Desired games has been written to "result.csv"')