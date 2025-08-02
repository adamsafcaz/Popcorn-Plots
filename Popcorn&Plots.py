import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("imdb_top_1000.csv")

print(df.columns)

df.groupby("Genre")["IMDB_Rating"].mean().sort_values(ascending=False).plot(
    kind="bar", figsize=(10,6), color="skyblue"
)
plt.title("T�rlere G�re Ortalama IMDb Puan�")
plt.ylabel("Ortalama Puan")
plt.xlabel("Film T�r�")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Runtime", y="IMDB_Rating", hue="Genre", alpha=0.6)
plt.title("Film S�resi ve IMDb Puan�")
plt.xlabel("S�re (dakika)")
plt.ylabel("IMDb Puan�")
plt.grid(True)
plt.tight_layout()
plt.show()

df["Released_Year"].value_counts().sort_index().plot(kind="line", figsize=(10,6))
plt.title("Y�llara G�re Film Say�s�")
plt.ylabel("Film Say�s�")
plt.xlabel("Y�l")
plt.grid(True)
plt.tight_layout()
plt.show()

df["Director"].value_counts().head(10).plot(kind="barh", color="pink")
plt.title("En �retken 10 Y�netmen")
plt.xlabel("Film Say�s�")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
