import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# bar plot
data = pd.read_csv("bank.csv", sep=";")
sns.barplot(x="job", y="age", data=data)

# countplot -- it counts the occurances
sns.countplot(data=data, x="job")

# boxplot - comparison between variables
sns.boxplot(data=data, x="job")

# violin plot -- for quantitative data
sns.violinplot(x="job", y="age", data=data)

# distribution plot  -- shows dustribution and trendline
sns.distplot(data.age)
# plt.show()


# Faetgrid  - is like the subplots in matplotlib
g = sns.FacetGrid(data, col="age")

# adds a chart to this grid
g.map(plt.hist, "job")
plt.show()