import pytrends
import seaborn as sns
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.style as style
import matplotlib.pyplot as plt
style.use('fivethirtyeight')


from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)

def interest_over_time(key, date):
    kw = [key]
    pytrends.build_payload(kw, cat=0, timeframe=date, geo='', gprop='')
    interest = pytrends.interest_over_time().reset_index()

    fig, ax = plt.subplots(figsize=(8,6))

    axs1 = sns.lineplot(x="date", y=kw[0], data=interest, ax=ax)

    plt.axhline(y=0, color='#414141', linewidth=1.5, alpha=.5)
    ax.set_yticks([0, 25, 50, 75, 100])

    plt.title('"{}" Google Interest Over Time   '.format(key),fontsize=25, weight = 'bold', fontfamily='sans-serif')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Interest', fontsize = 15)
    plt.xlabel("")
    ax.text(0.5, 0.6, key, horizontalalignment='center',verticalalignment='center', transform=ax.transAxes)
    plt.savefig("image/google_freq.png",bbox_inches='tight',dpi=100)
    plt.close()


def interest_related_topics(key, date):
    kw = [key]
    pytrends.build_payload(kw, cat=0, timeframe=date, geo='', gprop='')
    related = pytrends.related_topics()[key]['top']
    kw_list = []
    for i in related['topic_title']:
        if i not in kw_list:
            kw_list.append(i)
        if len(kw_list) == 5:
            break

    pytrends.build_payload(kw_list, cat=0, timeframe=date, geo='', gprop='')
    interest = pytrends.interest_over_time().reset_index()

    fig, ax = plt.subplots(figsize=(8,6))
    for i in range(len(kw_list)):
        no = i+1
        ax1 = sns.lineplot(x="date", y=kw_list[i],
                           label=kw_list[i], data=interest, ax=ax)

    plt.axhline(y=0, color='#414141', linewidth=1.5, alpha=.5)
    ax.set_yticks([0, 25, 50, 75, 100])
    plt.title('Interest Over Time of Related Topics',fontsize=25, weight = 'bold', fontfamily='sans-serif')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Interest', fontsize = 15)
    plt.xlabel("")
    plt.legend(frameon=False,bbox_to_anchor=(1, 0.8) )
    plt.savefig("image/google_topics.png",bbox_inches='tight',dpi=100)
    plt.close()
    

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def wordcloud_queries(key,date):
    pytrends.build_payload([key], cat=0, timeframe=date, geo='', gprop='')
    query = pytrends.related_queries()
    if query[key]['top'] is not None:
        input_top = list(query[key]['top']['query'])
        input_rising = list(query[key]['rising']['query'])
        def plot_wordcloud(output):
            text = " ".join(output)
            wordcloud = WordCloud(max_font_size=70, max_words=1000, colormap="Blues", background_color="white").generate(text)
            plt.figure(figsize=(8,6))
            plt.title("WordCloud of Top 25 Related Queries",fontsize=20, weight = 'bold', fontfamily='sans-serif')
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.savefig("image/{}_google_wordcloud.png".format(key),bbox_inches='tight',dpi=100)
            plt.close()
        plot_wordcloud(input_top)


def interest_by_country(key, date):
    kw_list = [key]
    pytrends.build_payload(kw_list, cat=0, timeframe=date, geo='', gprop='')
    interest_country = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=False, inc_geo_code=True)
    interest_country = interest_country.sort_values(key, ascending=False)
    interest_country = interest_country.iloc[:19, :].reset_index()
    fig, ax = plt.subplots(figsize=(10,6))
    plt.axhline(y=0, color='#414141', linewidth=1.5, alpha=.5)
    ax.set_yticks([0, 25, 50, 75, 100])

    ax = sns.barplot(x="geoName", y=kw_list[0], data=interest_country, palette='mako')
    plt.xticks(rotation=45, ha='right')
    plt.title('Search Interest By Country (Top 20)',fontsize=22, weight = 'bold', fontfamily='sans-serif')
    plt.xlabel("")
    plt.savefig("image/google_country.png",bbox_inches='tight',dpi=100)
    plt.close()


def go(key, start_date, end_date):
    date = start_date + " " + end_date
    interest_over_time(key, date)
    interest_related_topics(key, date)
    wordcloud_queries(key,date)
    interest_by_country(key, date)

# go('coronavirus', '2019-12-01', '2020-03-01')