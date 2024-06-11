import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

print(df.head())

sns.pairplot(df, hue="species")

plt.show()
