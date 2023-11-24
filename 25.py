import pandas as pd
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
print (full_health_data.describe())



import pandas as pd
import numpy as np
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
Минимальная_продажа= full_health_data["Минимальная_продажа"]
percentile15 = np.percentile(Минимальная_продажа, 15)
print(percentile15)



import pandas as pd
import numpy as np
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
std = np.std(full_health_data)
print(std)


import pandas as pd
import numpy as np
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
cv = np.std(full_health_data) / np.mean(full_health_data)
print(cv)


import numpy as np
health_data = pd.read_csv("data.csv", header=0, sep=",")
var = np.var(health_data)
print(var)


import pandas as pd
import numpy as np
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
var = np.var(full_health_data)
print(var)

import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.plot(x ='Закуп', y='Продажа', kind='scatter'),
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
negative_corr = {'Продажа_за_день': [10,9,8,7,6,5,4,3,2,1],
'Продажа': [210, 120, 300, 400,325, 220, 145, 305,270, 415]}
negative_corr = pd.DataFrame(data=negative_corr)
negative_corr.plot(x ='Продажа_за_день', y='Продажа', kind='scatter')
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
full_health_data.plot(x ='Минимальная_продажа', y='Продажа_за_день', kind='scatter')
plt.show()
#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()



import pandas as pd
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
Corr_Matrix = round(full_health_data.corr(),2)
print(Corr_Matrix)



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
full_health_data = pd.read_csv("dataset.csv", header=0, sep=",")
correlation_full_health = full_health_data.corr()
axis_corr = sns.heatmap(
correlation_full_health,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True
)
plt.show()


import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
Продажа_за_день = [30,40,60,90,110,120,150,160,190,200]
Продажа = [30,40,60,90,110,120,150,160,190,200]
Drowning = {"Продажа_за_день": [30,40,60,90,110,120,150,160,190,200],
"Продажа": [30,40,60,90,110,120,150,160,190,200]}
Drowning = pd.DataFrame(data=Drowning)
Drowning.plot(x="Продажа", y="Продажа_за_день", kind="scatter")
plt.show()
correlation_beach = Drowning.corr()
print(correlation_beach)
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
