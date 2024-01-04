import pandas as pd
import numpy as np
import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv("https://raw.githubusercontent.com/fidelmolday/website-data/master/instagram.csv", encoding='latin1')
data=data.dropna()
print(data.head())

figure=px.scatter(data_frame=data,
                x='impressions',
                y='Likes',
                size='Likes',
                trendline='ols',
                title='Relationship between Likes and impressions'
                )
figure.show()

plt.figure(figsize=(10.8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Between Likes & Impressions")
sns.regplot(x="Impressions",y="Likes",data=data)
plt.show()