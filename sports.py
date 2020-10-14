import requests
import json
import bs4 as bs


        

def get_news():
    res = requests.get("https://www.skysports.com/football")
    soup = bs.BeautifulSoup(res.text,'html.parser')
    headlines = []
    links = []
    for headline in soup.find_all('a', class_ = 'news-list__headline-link'):
            headlines.append(headline.text.strip())
            links.append(headline.get('href'))

    return headlines, links



if __name__ == '__main__':
    print(get_news())
    #print(s.get_scores())
