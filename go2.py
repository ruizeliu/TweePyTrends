
import word
import tweet_plot
import matplotlib.pyplot as plt
import tw_scraper
import sys


def go(key, start_date, end_date):
	tw_scraper.save_df(key, start_date, end_date)
	df = tweet_plot.read_tweets_file(key)
	text = tweet_plot.hash_list(df['hashtags'])
	word.plot_wordcloud(word.word_list(text), color=plt.cm.RdGy, 
						name="twitter_hist_wordcloud",
						title="Twitter Historical Keywords Cloud #{}".format(key),
						path="image/")
	tweet_plot.plot_day_freq(df, key, day_interval=10, n=3)
	top10 = tweet_plot.find_KOL(df)
	tweet_plot.plot_KOL_table(top10[["username", 'pop_score']])

if __name__ == '__main__':
	go(*sys.argv[1:])