import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("imdb_top_1000.csv")

print(df.columns)

df.groupby("Genre")["IMDB_Rating"].mean().sort_values(ascending=False).plot(
    kind="bar", figsize=(10,6), color="skyblue"
)
plt.title("Türlere Göre Ortalama IMDb Puaný")
plt.ylabel("Ortalama Puan")
plt.xlabel("Film Türü")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Runtime", y="IMDB_Rating", hue="Genre", alpha=0.6)
plt.title("Film Süresi ve IMDb Puaný")
plt.xlabel("Süre (dakika)")
plt.ylabel("IMDb Puaný")
plt.grid(True)
plt.tight_layout()
plt.show()

df["Released_Year"].value_counts().sort_index().plot(kind="line", figsize=(10,6))
plt.title("Yýllara Göre Film Sayýsý")
plt.ylabel("Film Sayýsý")
plt.xlabel("Yýl")
plt.grid(True)
plt.tight_layout()
plt.show()

df["Director"].value_counts().head(10).plot(kind="barh", color="pink")
plt.title("En Üretken 10 Yönetmen")
plt.xlabel("Film Sayýsý")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
