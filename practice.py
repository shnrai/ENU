#1
import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
x = full_health_data["Конфеты"]
y = full_health_data["Сок"]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
 return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Мин")
plt.ylabel ("в_день_продается")
plt.show()
#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#2
Arbuz = [80, 75, 75, 75, 70, 85, 90]
print(Arbuz)

#3
import pandas as pd
d = {'Кино аты': ['Венецядағы елестер','Катастрофа','Келінжан 2','Дәстүр',], 'Кинотеатрлар адресі': ['Сарыарка','Мега','Арай','Керуен'], 'Шығарылған жылы': [2023, 2022, 2021, 2023], 'Көрсетілім уақыты': [120, 110, 90, 105]}
df = pd.DataFrame(data=d)
print(df)

#4
import numpy as np
Income = [240, 3500, 10000, 500, 50000, 610, 550, 61000, 41250, 12241]
Average_Income= np.mean(Income)
print(Average_Income)
print (max(Income))
print (min(Income))

#5
import pandas as pd
Shop_data = pd.read_csv("data.csv", header=0, sep=",")
print(Shop_data)