import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_crawl_web_pjt.settings")
import django
django.setup()
from crawling.models import crawlingData

# 당근 크롤링 (AI)
def naver_crawling_ai():
    req = requests.get('https://medium.com/daangn/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8%EB%A1%9C-%EB%8F%99%EB%84%A4%EC%83%9D%ED%99%9C-%EC%8B%A0%EA%B3%A0-%EC%97%85%EB%AC%B4-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0-3b96608960')
    # req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select(
        'div > a'
    )
    # links = []
    # for link in my_links:
    #     links.append(link.get('href'))
    print(my_links)
    # my_titles = soup.select(
    #     '#__next > div.p-container.p-container--default.css-1n6tk1w > div > div > ul > a > div > span.typography.typography--h3.typography--bold.color--grey800.css-ad3vzk.e3wfjt74'
    # )
    # my_contents = soup.select(
    #     '#__next > div.p-container.p-container--default.css-1n6tk1w > div > div > ul > a > div > span.typography.typography--h7.typography--medium.color--grey700.css-1kw8fmk.e3wfjt71'
    # )
    # links = []
    # for link in my_links:
    #     links.append(link.get('href'))
    # titles = []
    # for title in my_titles:
    #     titles.append(title.text.strip())
    # contents = []
    # for content in my_contents:
    #     contents.append(content.text.strip())

    # for item in zip(titles, contents, links):
    #     crawlingData(
    #         title=item[0],
    #         content=item[1],
    #         link=item[2],
    #         company = '토스',
    #         tech = 'FE'
    #     ).save()

    return

if __name__=='__main__':
    naver_crawling_ai()



