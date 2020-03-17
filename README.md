# TweePyTrends

TweePyTrends is developed by Donimic, Ruize, Jiaqi, and Ya-han as our group project for CAPP30122.

## Introduction

TweePyTrends supports real-time data collection model and sample viewing model. 

In this app, we use three data sources:
1. Pytrends (API): retrieves data from Google Trends
2. Twitterscrapper (API): retrieves data from all historical tweets (work significantly slow)
3. Crawler (Web scrapping): scrap real-time data from twitter


## Usage

After installing all packages (as requirements.txt), run
```command
python3 GUI.py
```
To retrieve historical Tweets, run below before entering in the app
```command
python3 go2.py word start_date end_date
```
\
**Suggest search** \ 
chicago. 2020-03-01. 2020-03-05 \
coronavirus, 2020-02-01, 2020-03-05


## Common Errors

### Google Trends

1. Pytrends and Pandas Inconsistency
If encounter error message *"No module named 'pandas.io.json.normalize'"*, Please go to site-packages/pytrends/request.py and change line 13 into *pandas.io.josn.normalize*. This is a system inconsistency between two packages and we have not found other ways to solve.

### Real-time Twitter 

1. Crawler Frozen
Crawler can get frozen because of too many attempts within a short period. In this case, the app will show an error message picture saying "Crawler is frozen, try 5 mins later".

2. Pandas Inconsistency 
Pandas sometimes performs inconsistently with the crawler, but there is nothing inherently wrong with that. If see error message *"Length mismatch: Expected axis has 0 elements, new values have 2 elements"*. Please click the button again and it should work.

### TwitterScrapper

1. TwitterScrapper 
TwitterScrapper works less efficiently since it collects all historical data and UI works far less stable with TwitterScrapper connected. Thus, we seperate them into two functions. \
**To check historical tweets, user must run command line as below**

```command
python3 go2.py word start_date end_date
```

If forget to do so, the error message will be *QPixmap::scaleWidth: Pixmap is a null pixmap*
All input should have same form as in app. If the API crashes, the app will return error message picture.

## UI Page Details

1. Welcome Page - readmepic/6.png
2. Input Page - readmepic/5.png
3. Data Source Page - readmepic/2.png
4. Google Trends Page - readmepic/4.png
5. Historical Tweets Page - readmepic/3.png
6. Real-time Tweets Page - readmepic/1.png

## Requirements and Versions

Please check requirements.txt

## Video Demo

[Video Demo][1] produced by Laura.
[1]: https://drive.google.com/file/d/1jU-BqtF_r2aM-snOW0pBP6H-jinOm8nu/view

