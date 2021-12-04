import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
import matplotlib.gridspec as gridspec

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

data = pd.read_csv('./resources/전체데이터.csv',
                   index_col=0,
                   encoding='CP949',
                   engine='python')

print(data)


fig = plt.figure(constrained_layout=True, figsize=(13,10))
spec2 = gridspec.GridSpec(ncols=3, nrows=2, figure=fig)

f2_ax1 = fig.add_subplot(spec2[0, 0], title='연령에 따른 고지혈증', ylabel='고지혈증(%)', ylim=[0, 100])
f2_ax2 = fig.add_subplot(spec2[0, 1], title='연령에 따른 당뇨 지수', ylabel='당뇨 지수')
f2_ax3 = fig.add_subplot(spec2[0, 2], title='연령에 따른 나트륨 섭취량', ylabel='나트륨 섭취량(mg)')
f2_ax4 = fig.add_subplot(spec2[1, 0], title='연령에 따른 비만율', ylabel='비만율(%)', ylim=[0, 100])
f2_ax5 = fig.add_subplot(spec2[1, 1], title='연령에 따른 음주율', ylabel='음주율(%)', ylim=[0, 100])
f2_ax6 = fig.add_subplot(spec2[1, 2], title='연령에 따른 흡연율', ylabel='흡연율')

# =========================================================================
men = data.query('성별 =="남자"')
women = data.query('성별 =="여자"')

menAge = men['특성별']
womenAge = women['특성별']

menHyper = men['고지혈증']
womenHyper = women['고지혈증']

f2_ax1.plot(menAge, menHyper, marker='o', label='남성', color='#74a3d6')
f2_ax1.plot(womenAge, womenHyper, marker='o', label='여성', color='#e099d9')
f2_ax1.legend()

# =========================================================================
menDiabetes = men['당뇨']
womenDiabetes = women['당뇨']

f2_ax2.plot(menAge, menDiabetes, marker='o', label='남성', color='#74a3d6')
f2_ax2.plot(womenAge, womenDiabetes, marker='o', label='여성', color='#e099d9')
f2_ax2.legend()

# =========================================================================
menSaltRate = men['나트륨섭취량']
womenSaltRate = women['나트륨섭취량']

f2_ax3.plot(menAge, menSaltRate, marker='o', label='남성', color='#74a3d6')
f2_ax3.plot(womenAge, womenSaltRate, marker='o', label='여성', color='#e099d9')
f2_ax3.legend()


# =========================================================================
menFatRate = men['비만율']
womenFatRate = women['비만율']

f2_ax4.plot(menAge, menFatRate, marker='o', label='남성', color='#74a3d6')
f2_ax4.plot(womenAge, womenFatRate, marker='o', label='여성', color='#e099d9')
f2_ax4.legend()


# =========================================================================
menDrinkingRate = men['음주율']
womenDrinkingRate = women['음주율']

f2_ax5.plot(menAge, menDrinkingRate, marker='o', label='남성', color='#74a3d6')
f2_ax5.plot(womenAge, womenDrinkingRate, marker='o', label='여성', color='#e099d9')
f2_ax5.legend()


# =========================================================================
menSmokingRate = men['흡연율']
womenSmokingRate = women['흡연율']

f2_ax6.plot(menAge, menSmokingRate, marker='o', label='남성', color='#74a3d6')
f2_ax6.plot(womenAge, womenSmokingRate, marker='o', label='여성', color='#e099d9')
f2_ax6.legend()


plt.show()