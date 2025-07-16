import pandas as pd
import matplotlib.pyplot as plt

# Sample data to demonstrate the code
data = {"Survived": [1, 0, 1, 0, 1], "Age": [22, 38, 26, 35, 19]}
df = pd.DataFrame(data)

# Group age based on people who survived
dfsurvived = df.groupby("Survived").sum()["Age"].reset_index()

# Plotting the pie chart
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis("equal")
ax.pie(dfsurvived["Age"], labels=dfsurvived["Survived"], autopct="%1.2f%%")

plt.show()