import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Продажа"]
y = full_health_data["Остаток"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Продажа")
plt.ylabel ("Остаток")
plt.show()

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()



import pandas as pd
import statsmodels.formula.api as smf
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
model = smf.ols('Calorie_Burnage ~ Average_Pulse', data = full_health_data)
results = model.fit()
print(results.summary())



def Predict_Остаток(Продажа):
 return(0.3296 * Продажа + 346.8662)
#Try some different values:
print(Predict_Остаток(130))
print(Predict_Остаток(150))
print(Predict_Остаток(110))
print(Predict_Остаток(145))




import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Минимальная_продажа"]
y = full_health_data["Продажа"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

print(mymodel)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=700)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Минимальная_продажа")
plt.ylabel ("Продажа")
plt.show()

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


def Predict_Закуп(Продажа, Остаток):
 return(3.1695 * Продажа + 5.8434 * Остаток - 334.5194)
print(Predict_Закуп(120,40))
print(Predict_Закуп(150,45))
print(Predict_Закуп(135,70))
