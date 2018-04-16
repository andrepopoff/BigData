import pandas as pd
import matplotlib.pyplot as plt
from os.path import join

# Сгруппируйте данные по полу и году и визуализируйте общую динамику рождаемости обоих полов

directory = 'babynames'
df = pd.DataFrame()

for i in range(1880, 2011):
    file = 'yob{}.txt'.format(i)
    new_df = pd.read_csv(join(directory, file), names=['name', 'sex', 'numbers', 'year'])
    new_df['year'] = i
    df = new_df if df.empty else df.append(new_df)

df2 = df.groupby(['year', 'sex']).sum()
# df2.plot.bar()
# plt.show()

