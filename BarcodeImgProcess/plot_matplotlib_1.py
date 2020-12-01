# from sklearn import set_config
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import OneHotEncoder, StandardScaler

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, 10*x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.plot(x, x**.15, label='SimpleEqu')


plt.xlabel('x label')
plt.ylabel('y label')

plt.title('--Sample Charting--')
plt.legend()
plt.show()
