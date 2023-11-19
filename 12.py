#1
import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.plot(x ='Average_Pulse', y='Max_Pulse', kind='line')
plt.ylim(ymin=110)
plt.xlim(xmin=60)
plt.show()
#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#2
def slope(a1, b1, a2, b2):
  s = (b2-b1)*(a2-a1)
  return s
print(slope(120,360,90,240))


#3
def my_function(x):
  return 3*x + 75
print (my_function(106))

#4
import pandas as pd
import numpy as np
health_data = pd.read_csv("data.csv", header=0, sep=",")
x = health_data["Жұмыс_саны"]
y = health_data["Жұмыс_уакыты"]
slope_intercept = np.polyfit(x,y,1)


#5
import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.plot(x ='Max_Pulse', y='Calorie_Burnage', kind='line'),
plt.ylim(ymin=210, ymax=370)
plt.xlim(xmin=70, xmax=200)
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
