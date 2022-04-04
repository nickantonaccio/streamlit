import matplotlib.pyplot as plt
from wordcloud import WordCloud
df_wc=df[(df['tags'] =='education')]
df_wc=df_wc[['talk_name','views']]
df_wc = df_wc.set_index('talk_name').to_dict()['views']

wc = WordCloud(width=800, height=400, max_words=200,).generate_from_frequencies(df_wc)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
