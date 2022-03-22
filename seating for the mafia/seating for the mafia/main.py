

'''
Необходимо рассадить N количество учасников в мафию на Y игры. Некоторым учасникам нельзя сидеть вместе.
'''


from msilib.schema import tables
import numbers
import random


players = ['Мартовский',
           'Бэт',
           'Бага',
           'Домино',
           'Ежевика',
           'Пряня',
           'Кундалини',
           'Шьюдела',
           'Арачка',
           'Kurayami',
           'Лиса',
           'Гига',
           'Северный',
           'Каштан',
           'Пау',
           'Одуван',
           'Rain',
           'Шаман',
           'Стив',
           'Самара',
           'Eleon',
           'КЩ',
           'Питон',
           'Revolution',
           'Ермак',
           'Ахегао',
           'Вискас',
           'Джонни',
           'Животное',
           'Ред',
           'Мама моши',
           'Дровосек',
           'Микки',
           'Инкогнито',
           'Леся',
           'АВП', ]


# NUBMER_OF_TABLES = 3
# NUMBER_OF_GAME = 12

# games = []


# for i in range(NUBMER_OF_TABLES):
#     for j in range(NUMBER_OF_GAME):
#         game = {
#             'table': i+1,
#             'game': j + 1,
#             'players': []
#         }
#         games.append(game)


# for i in range(len(games)):
#     games[i]['players'].append(players[i])

# print(games)

f = open('text1.txt', 'w', encoding="utf-8")
for i in range(6):
    chill = players[i * 6: (i + 1) * 6]
    active = [item for item in players if item not in chill]
    random.shuffle(active)
    t1 = active[:10]
    t2 = active[10:20]
    t3 = active[20:]
    f.write('--' * 10 + 'Игра' + str(i + 1) + '--' * 10 + '\n')
    f.write('Отдыхающие:\n')
    for p in chill:
        f.write(p + '\n')
    f.write('*' * 10 + 'СТОЛ 1' + '*' * 10 + '\n')
    for p in t1:
        f.write(p + '\n')
    f.write('*' * 10 + 'СТОЛ 2' + '*' * 10 + '\n')
    for p in t2:
        f.write(p + '\n')
    f.write('*' * 10 + 'СТОЛ 3' + '*' * 10 + '\n')

    for p in t3:
        f.write(p + '\n')
    random.shuffle(active)
    t1 = active[:10]
    t2 = active[10:20]
    t3 = active[20:]
    f.write('--' * 10 + 'Игра' + str(i + 7) + '--' * 10 + '\n')
    f.write('*' * 10 + 'СТОЛ 1' + '*' * 10 + '\n')
    for p in t1:
        f.write(p + '\n')
    f.write('*' * 10 + 'СТОЛ 2' + '*' * 10 + '\n')
    for p in t2:
        f.write(p + '\n')
    f.write('*' * 10 + 'СТОЛ 3' + '*' * 10 + '\n')
    for p in t3:
        f.write(p + '\n')


# # games = []

# for i in range(10):
#     tables = [[], [], [], []]
#     head = players[4 * i: 4 * i + 4]
#     body = [item for item in players if item not in head]
#     random.shuffle(body)
#     for j, table in enumerate(tables):
#         table.append(head[j])
#         table += body[9 * j: 9 * j + 9]
#     games.append(tables)

# f = open('Рассадка41.txt', 'w', encoding="utf-8")
# for j, game in enumerate(games):
#     f.write('--------------Игра' + str(j+1) + '--------------\n')
#     for i, table in enumerate(game):
#         f.write('****СТОЛ' + str(i+1) + '****\n')
#         for p in table:
#             f.write(p + '\n')
# #