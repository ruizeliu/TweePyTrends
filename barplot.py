import util
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

###### Trending Issue Bar Chart Plotting ######


def plot_bar_toptopic(dic, key):
	'''
	Plot bar plot for trending issues with mentioned frequency
	'''
	hashtag = util.extract_hash(dic)
	top_freq = {h:hashtag.count(h) for h in hashtag}
	df = pd.DataFrame(list(top_freq.items()))
	df.columns =["Hashtag","Count"]
	df = df.sort_values(['Count'], ascending=False)
	if df.shape[0] >= 6:
		df = df.head(6)
	plt.figure(figsize=(15,5))
	plt.title("Top Related Hashtag of #{}".format(key),fontsize=20, 
				weight = 'bold', fontfamily='sans-serif')
	sns.barplot(df.Count, df.Hashtag, palette="ch:.25_r")
	plt.savefig("image/twitter_bar_plot.png")
	plt.close()
