import pandas as pd
import datetime as dt
import re
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import six
style.use('fivethirtyeight')
import word

def read_tweets_file(filename, path=""):
    '''
    Reads file contains tweets
    Inputs:
        filename: (str) file name
        path: (str) directory of the file
    Output:
        df: Pandas dataframe
    '''
    path = path + filename + ".csv"
    df = pd.read_csv(path, dtype={'retweets': "float64", 'likes': "float64", 'replies': "float64"},
                    error_bad_lines=False)
    return df


def hash_list(series):
    '''
    Cleans up hashtags
    Input: 
        series: (pd.series) the column of hashtags
    Output:
        hash_list: (list) list of hashtags
    '''
    series = series.apply(lambda tags: str(tags).strip('[]').split(', '))
    hash_list = []
    for tag_list in series:
        tag_list = list(map(lambda x: x.strip("''"), tag_list))
        hash_list += tag_list
    return hash_list


def trans_date(timestp):
    '''
    Transforms string to datetime structure
    Input:
        timestp: (str) string of date
    Output:
        datetime object of year-month-day
    '''
    if type(timestp) == str:
        timestp = timestp.replace('/', "-")
        time = timestp.replace(' ', "-").replace(":", "-").split("-")
        date = tuple(map(int, time))[0:3]
        return dt.date(date[0], date[1], date[2])


def plot_day_freq(df, hashtag, day_interval=10, n=2):
    '''
    Plots daily frequecy plot for a hashtag
    Inputs:
        df: (pd.dataframe) dataframe of tweets
        day_interval: (int) day interval of the ticker
        n: (int) number of peaks to tag, n < 50
    '''
    df.loc[:, "time"] = list(df.loc[:, "timestamp"].apply(trans_date))
    df_day = pd.DataFrame(df["time"].value_counts())
    df_day["date"] = df_day.index
    df_day.reset_index()
    day, freq = zip(*sorted(zip(df_day['date'], df_day['time'])))
    
    df_top = df_day.nlargest(50, 'time')
    
    date_ls = []
    num_ls = []
    for row in df_top.iterrows():
        date_in = False
        if date_ls:
            for date in date_ls:
                if date < row[0]+dt.timedelta(days=2) and date > row[0]-dt.timedelta(days=2):
                    date_in = True
                    break
        if not date_in:
            date_ls.append(row[1][1])
            num_ls.append((row[1][1], row[1][0]))
    
    plt.figure(figsize=(8, 6))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=day_interval))
    plt.plot(day, freq)
    plt.title("Number of Tweets Over Time {}".format("#"+hashtag))
    # for iters in num_ls[:n]:
    #     plt.text(iters[0], iters[1]+80, iters[0].strftime("%Y-%m-%d"))
    
    plt.gcf().autofmt_xdate()
    plt.savefig("image/twitter_hist_freq.png", bbox_inches='tight', dpi=100)

    
def find_KOL(df):
    '''
    Finds top 10 KOL of a hashtag by user's popular scores
    Popular score = # of likes + # of replies + 2 * # of retweets
    
    Input:
        df: (pd.dataframe) dataframe of tweets
    Output:
        df3.head(10): (pd.dataframe) dataframe of top 10 popular users
    '''
    df['pop_score'] = df['retweets'].apply(float)*2 + df['likes'].apply(float) + \
                      df['replies'].apply(float)
    
    df3 = pd.DataFrame({'user_id': df["user_id"].unique()})
    pop_score = []
    user_name = []
    for user in df3['user_id']:
        pop_score.append(sum(df.loc[df['user_id'] == user, 'pop_score']))
        if not df.loc[df['user_id'] == user, 'username'].empty:
            user_name.append(df.loc[df['user_id'] == user, 'username'].unique()[0])
        else:
            user_name.append(None)
    
    df3['username'] = user_name
    df3["pop_score"] = pop_score
    df3.sort_values(by=['pop_score'], inplace=True, ascending=False)
    
    return df3.head(10)


def plot_KOL_table(data, col_width=4.5, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    fig.savefig("image/twitter_hist_KOL.png", bbox_inches='tight', dpi=100)
