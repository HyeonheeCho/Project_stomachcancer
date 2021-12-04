import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc


font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

data = pd.read_csv('./resources/전체데이터.csv',
                   index_col=0,
                   encoding='CP949',
                   engine='python')


print(data)
rate = data['나트륨섭취량']
print(rate)

men = data.query('성별 =="남자"')
women = data.query('성별 =="여자"')

menAge = men['특성별'][2:]
womenAge = women['특성별'][2:]

print(womenAge)
menSaltRate = men['나트륨섭취량'][2:]
womenSaltRate = women['나트륨섭취량'][2:]

print(menSaltRate)
print(womenSaltRate)

menSaltRate40 = men['나트륨섭취량'][2]
womenSaltRate40 = women['나트륨섭취량'][2]

menSaltRate50 = men['나트륨섭취량'][3]
womenSaltRate50 = women['나트륨섭취량'][3]

menSaltRate60 = men['나트륨섭취량'][4]
womenSaltRate60 = women['나트륨섭취량'][4]

menSaltRate70 = men['나트륨섭취량'][5]
womenSaltRate70 = women['나트륨섭취량'][5]

x = ['남', '여']
men = '남'
women ='여'

plt.title('남녀 나트륨 섭취량(40~70대 이상)')

plt.bar('남', menSaltRate40, label='40대', color="lightblue", alpha=0.5)
plt.bar('여', womenSaltRate40, label='40대', color="lightpink", alpha=0.5)

plt.bar([i * 2 for i in range(len(x))], menSaltRate50, label='50대', color="lightblue", alpha=0.5)
plt.bar([i * 2 + 1 for i in range(len(x))], womenSaltRate50, label='50대', color="lightpink", alpha=0.5)

plt.bar([i * 2 for i in range(len(x))], menSaltRate60, label='60대', color="lightblue", alpha=0.5)
plt.bar([i * 2 + 1 for i in range(len(x))], womenSaltRate60, label='60대', color="lightpink", alpha=0.5)

plt.bar([i * 2 for i in range(len(x))], menSaltRate70, label='70대 이상', color="lightblue", alpha=0.5)
plt.bar([i * 2 + 1 for i in range(len(x))], womenSaltRate70, label='70대 이상', color="lightpink", alpha=0.5)

plt.xticks([i * 2 + 0.5 for i in range(len(x))], x)

plt.xlabel('연령')
plt.ylabel('나트륨 섭취량(mg)')
plt.legend()
plt.show()



