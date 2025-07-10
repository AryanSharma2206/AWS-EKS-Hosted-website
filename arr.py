import pandas as pd
import matplotlib.pyplot as plt

data = {'Name': ['Arnav', 'Nazar', 'Sheela', 'Azhar', 'Bincy', 'Yash'],
        'Height': [60, 61, 63, 65, 56, 60],
        'Weight': [47, 89, 52, 55, 56, 58]}

df = pd.DataFrame(data)
df.plot(kind='hist')
plt.show()
