# Коды из справочника
# 2203, Пиво
# 2208 Спиртные напитки
# 2204, ВИНА ВИНОГРАДНЫЕ НАТУРАЛЬНЫЕ

import csv  # Используем модуль csv для более удобной работы с csv файлом
import matplotlib.pyplot as plt  # Используем matplotlib для построения графиков

beer = {}
wine = {}
alcohol = {}
all = {}
# Все словари вида {страна : количество}



with open('TCBT.csv', newline='', errors='replace') as csvfile:
    reader = csv.reader(csvfile, quotechar=',')
    for row in reader:
        if row[3] == '2203':
            beer[row[2]] = beer.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
            all[row[2]] = all.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
        elif row[3] == '2204':
            wine[row[2]] = wine.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
            all[row[2]] = all.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
        elif row[3] == '2208':
            alcohol[row[2]] = alcohol.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
            all[row[2]] = all.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])

beer_list = [(k, v) for k, v in beer.items()]
beer_list.sort(key=lambda x: x[1], reverse=True)
beer_list = beer_list[0:10]

wine_list = [(k, v) for k, v in wine.items()]
wine_list.sort(key=lambda x: x[1], reverse=True)
wine_list = wine_list[0:10]

alcohol_list = [(k, v) for k, v in alcohol.items()]
alcohol_list.sort(key=lambda x: x[1], reverse=True)
alcohol_list = alcohol_list[0:10]

all_list = [(k, v) for k, v in all.items()]
all_list.sort(key=lambda x: x[1], reverse=True)
all_list = all_list[0:10]




plt.style.use('seaborn-deep')
plt.rcParams['font.family'] = 'Tahoma'

def visualize_results(tuple_list, name):
    nam, val = map(list, zip(*tuple_list))
    fig, ax = plt.subplots()
    for i in range(len(tuple_list)):
        ax.bar(nam[i], val[i])
        ax.text(nam[i], val[i] + val[i] / 100, "{}\nтыс. штук".format(str(val[i] // 1000)),
                horizontalalignment='center', color='#949cab')
    ax.set(ylim=(min(val) - min(val) / 10, max(val) + max(val) / 10))

    ax.axes.get_yaxis().set_visible(False)
    ax.grid(False)
    ax.set_facecolor('#36393f')
    ax.tick_params(axis='both', which='major', labelsize=14)
    plt.setp(ax.spines.values(), color="#2f3136")
    ax.tick_params(axis='x', colors='#747c89')
    fig.set_figwidth(12)
    fig.set_figheight(6)
    plt.gcf().set_facecolor('#2f3136')
    plt.title(name, color='#c4cfe0', fontsize=16)
    plt.show()


visualize_results(beer_list, "Топ-{} стран по объёмам поставки пива".format(len(beer_list)))
visualize_results(wine_list, "Топ-{} стран по объёмам поставки вина".format(len(wine_list)))
visualize_results(alcohol_list, "Топ-{} стран по объёмам поставки спиртосодержащих напитков".format(len(alcohol_list)))
visualize_results(all_list,
                  "Топ-{} стран по объёмам поставки алкогольных напитков всех видов".format(len(alcohol_list)))

exit()

# Строки для вывода всех данных на экран, использовались для проверки, в готовом проекте не нужны

print("----->Топ стран по объёмам поставки пива: ")
for i in range(len(beer_list)):
    print("{} место: {}, количкство составило: {} штук".format(i + 1, beer_list[i][0], beer_list[i][1]))

print("----->Топ стран по объёмам поставки вина: ")
for i in range(len(wine_list)):
    print("{} место: {}, количкство составило: {} штук".format(i + 1, wine_list[i][0], wine_list[i][1]))

print("----->Топ стран по объёмам поставки спиртосодержащих напитков: ")
for i in range(len(alcohol_list)):
    print("{} место: {}, количкство составило: {} штук".format(i + 1, alcohol_list[i][0], alcohol_list[i][1]))

print("----->Топ стран по объёмам поставки алкогольных напитков всех видов: ")
for i in range(len(all_list)):
    print("{} место: {}, количкство составило: {} штук".format(i + 1, all_list[i][0], all_list[i][1]))
