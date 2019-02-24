#%%
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

array = [5, 8, 9, 45 ,3, 8]
array2 = [5,8, 9, 45, 3 ,8]

for i, element in enumerate(array):
    print("This is i :", i, "This is element: ", element)

#%%
sns.distplot(array)
plt.xlabel("Test")
plt.show()

#%%
