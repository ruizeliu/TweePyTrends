import crawler
import word
import barplot
import network
import shutil
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

###### Pulling All Together ######

def go(key, max = 4):
	'''
	Pull all functions together
	Save four plots in local file holder
	'''
	info_tuple = {'hashtag': ('tr', 'tweet-container', 'a', 'twitter-hashtag dir-ltr'),
					'text': ('tr', 'tweet-container', 'div', 'dir-ltr')}
					
	dic = crawler.crawler(key, info_tuple, max)
	if dic.values() == [[[],[]]]:
		shutil.copy2("freeze.jpg", "twitter_network.png")
		shutil.copy2("freeze.jpg", "twitter_bar_plot.png")
		shutil.copy2("freeze.jpg", "twitter_wordcloud_text.png")
		shutil.copy2("freeze.jpg", "twitter_wordcloud_hash.png")
	else:
		network.plot_network(dic, key)
		barplot.plot_bar_toptopic(dic, key)
		word.plot_wordcloud(word.word_list(dic, "hashtag"), "YlOrBr", 
							"image/twitter_wordcloud_hashtag",
							"Twitter Real-time Related Hashtag #{}".format(key))
		word.plot_wordcloud(word.word_list(dic, "text"), plt.cm.inferno, 
							"image/twitter_wordcloud_text",
							"Twitter Real-time Content #{}".format(key))
