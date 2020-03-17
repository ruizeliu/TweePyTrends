import util
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

###### Word Cloud Plotting ######

def word_list(lst_dic, type = None):
	if not type:
		return " ".join(lst_dic)
	else:
		if type == "text":
			text = util.extract_text(lst_dic)
		if type == "hashtag":
			text = util.extract_hash(lst_dic)
		return " ".join(text)

def plot_wordcloud(text, color, name, title, path = None):
	'''
	Plot word cloud for all texts in tweets
	'''
	wordcloud = WordCloud(collocations=False, max_font_size=50,
				colormap=color, background_color="white").generate(text)

	plt.figure(figsize=(10,10))
	plt.title(title,fontsize=20, weight = 'bold', fontfamily='sans-serif')
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	name = name + ".png"
	if path:
		name = path + name
	plt.savefig(name,bbox_inches='tight',dpi=100)
	plt.close()

