import matplotlib.pyplot as plt
import pandas as pd

data = {
    "PassengerId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [22, 38, 26, 35, 35, 27, 54, 2, 27, 14],
}

df = pd.DataFrame(data)

df_10 = df.head(10)
fig = plt.figure(figsize=(7, 3))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlabel("Passenger ID")
ax.set_ylabel("Age")
ax.bar(df_10["PassengerId"], df_10["Age"])
plt.show()