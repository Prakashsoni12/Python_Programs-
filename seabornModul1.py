import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# sns.distplot(random.normal(size=1000), hist=False)
# plt.show()
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()