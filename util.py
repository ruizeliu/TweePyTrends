import requests
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re


########### Make Soup ###########

def read_url(url):
    '''
    Read-in url and return soup object
    '''
    r = get_request(url)
    text = r.text.encode("utf-8")
    soup = BeautifulSoup(text, "html.parser")
    return soup


def get_request(url):
    '''
    Send request
    '''
    try:
        agent = UserAgent().random 
        r = requests.get(url=url,headers={'User-Agent': agent})
        if r.status_code == 404 or r.status_code == 403:
            r = None
    except Exception:
        # fail on any kind of error
        r = None
    return r

########### Retrieve Web ###########

def retrieve_web(key, info_tuple):
    '''
    Crawl one web based on hashtag search and return related hashtags and tweet texts

    Input:
        key: key word used for searching
        info_tuple:
            dictionary of elements and related section tags, for example:
            {'hashtag':('tr', "tweet-container", "a", "twitter-hashtag dir-ltr")} 
    Output:
        dic: dictionary storing information retrieved from website
    '''
    soup = read_url("https://twitter.com/search?q=%23{}&src=typed_query&f=live".format(key))
    dic = {}
    for tag in info_tuple:
        info = info_tuple[tag]
        content = []
        tr = soup.find_all(info[0], info[1])
        for t in tr:
            content.append(t.find_all(info[2], class_=info[3]))
        dic.update({tag: content})
    return dic

########### Identify Word ###########

def find_word(word):
    '''
    Identify whether a term is a word
    '''
    word_pattern = re.compile("^[a-zA-Z0-9_.-]*$")
    if word_pattern.match(word):
        if word:
            return True
    return False

########### Read Hashtag & Text ###########
def process_hashtag(dic):
    '''
    Process dictionary from retrieve_web and store hashtags in a list
    '''
    hashtag = []
    for h in dic['hashtag']:
        for hh in h:
            word = hh.text.lower()[1:]
            if find_word(word):
                hashtag.append(word)
    return hashtag


def process_text(dic):
    '''
    Process dictionary from retrieve_web and store all texts as list
    '''
    words = []
    for t in dic['text']:
        word = t[0].text.lower()
        split_words = word.split(" ")
        for w in split_words:
            if find_word(w):
                words.append(w)
    return words

########### Extract Hash & Text from Dic ###########

def extract_hash(dic):
    tag = [dic[k][0] for k in dic.keys()]
    tag = [x for sub in tag for x in sub]
    tag = [x for x in tag if find_word(x)]
    return tag


def extract_text(dic):
    word = [dic[k][1] for k in dic.keys()]
    word = [x for sub in word for x in sub]
    word = [x for x in word if find_word(x)]
    return word
