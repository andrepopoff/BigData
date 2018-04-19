import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os.path import join

# x = np.arange(0.0, 7.0, 0.1)
# y = np.cos(x)
#
# fig = plt.figure()
# plt.plot(x, y)
#
# plt.text(2, 0, 'Example')
# plt.vlines(2, -1, 1, colors='r')
# plt.show()

directory = 'babynames'
df = pd.DataFrame()

for i in range(1880, 2011):
    file = 'yob{}.txt'.format(i)
    new_df = pd.read_csv(join(directory, file), names=['name', 'sex', 'numbers', 'year'])
    new_df['year'] = i
    df = df.append(new_df)

american_presidents = pd.read_csv('us_presidents.csv')


def change_data(df, column, index, splitter=' '):
    for i, row in enumerate(df[column]):
        data = row.split(splitter)
        american_presidents.at[i, column] = data[index]


# Оставим в датах только года
change_data(american_presidents, 'start', -1, ', ')
change_data(american_presidents[american_presidents.index < 42], 'end', -1, ', ')

# Оставим в колонке president только имя
change_data(american_presidents, 'president', 0)

# Оставим данные в пределах нужных дат
american_presidents = american_presidents[american_presidents['start'].astype('int64').isin(range(1880, 2011))]
# american_presidents.president.values

for i in range(len(american_presidents)):
    start = american_presidents.iat[i, 2]
    end = american_presidents.iat[i, 3]
    name = american_presidents.iat[i, 4]
    fr = df[df['name'] == name]
    fr = fr.groupby(['name', 'year'], as_index=False).sum()
    x = fr['year']
    y = fr['numbers']
    fig = plt.figure()

    plt.plot(x, y)
    plt.title('{}: {}-{}'.format(name, start, end))
    plt.vlines(int(start), 0, fr['numbers'].max(), colors='r', linestyles='dashed', label='dates as president')
    if start != end:
        plt.vlines(int(end), 0, fr['numbers'].max(), colors='r', linestyles='dashed')
    plt.legend()
    plt.show()

# start = american_presidents.iat[1, 2]
# end = american_presidents.iat[1, 3]
# name = american_presidents.iat[1, 4]
# fr = df[df['name'] == name]
#
# fr = fr.groupby(['name', 'year'], as_index=False).sum()
#
# x = fr['year']
# y = fr['numbers']
#
# fig = plt.figure()
# plt.plot(x, y)
# plt.title('{}: {}-{}'.format(name, start, end))
# # plt.grid()
# # plt.text(2, 0, 'Example')
# plt.vlines(int(start), 0, fr['numbers'].max(), colors='r')
# if start != end:
#     plt.vlines(int(end), 0, fr['numbers'].max(), colors='r')
# plt.show()
