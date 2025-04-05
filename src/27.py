import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract headlines and images
    headlines = [a.text for a in soup.find_all('div', class_='headline') if a.get_text(strip=True).startswith('Headline: ') or not a.get_text(strip=True)]
    images = [img['src'] for img in soup.find_all('img')]

    return {'headlines': headlines, 'images': images}

url = "https://www.example.com/news"
news_data = fetch_news(url)
print(news_data)
