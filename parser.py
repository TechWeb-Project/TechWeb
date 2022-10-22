import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_crawl_web_pjt.settings")
import django
django.setup()
from crawling.models import crawlingData

# 카카오 크롤링 (AI)
def kakao_crawling_ai():
    req = requests.get('https://tech.kakao.com/?s=ai')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    my_contents = soup.select(
        'div.elementor-post__excerpt > p'
        )

    contents = []
    for content in my_contents:
        contents.append(content.text)
    titles = []
    links = []
    for title in my_titles:
        if title.text.strip() == 'Main':
            continue
        titles.append(title.text.strip())
        links.append(title.get('href'))

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '카카오',
            tech = 'AI'
        ).save()

    return

# 카카오 크롤링 (클라우드)
def kakao_crawling_cloud():
    req = requests.get('https://tech.kakao.com/tag/cloud/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    my_contents = soup.select(
        'div.elementor-post__excerpt > p'
        )

    contents = []
    for content in my_contents:
        contents.append(content.text)
    titles = []
    links = []
    for title in my_titles:
        titles.append(title.text.strip())
        links.append(title.get('href'))

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '카카오',
            tech = '클라우드'
        ).save()

    return

# 카카오 크롤링 (FE)
def kakao_crawling_FE():
    req = requests.get('https://tech.kakao.com/tag/front-end/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    my_contents = soup.select(
        'div.elementor-post__excerpt > p'
        )

    contents = []
    for content in my_contents:
        contents.append(content.text)
    titles = []
    links = []
    for title in my_titles:
        titles.append(title.text.strip())
        links.append(title.get('href'))

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '카카오',
            tech = 'FE'
        ).save()

    return

# 카카오 크롤링 (BE)
def kakao_crawling_BE():
    req = requests.get('https://tech.kakao.com/?s=%EC%84%9C%EB%B2%84')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    my_contents = soup.select(
        'div.elementor-post__excerpt > p'
        )

    contents = []
    for content in my_contents:
        contents.append(content.text)
    titles = []
    links = []
    for title in my_titles:
        titles.append(title.text.strip())
        links.append(title.get('href'))

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '카카오',
            tech = 'BE'
        ).save()

    return


# 쿠팡 크롤링 (AI)
def coupang_crawling_ai():
    req = requests.get('https://medium.com/coupang-engineering/tagged/ai')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select(
        'div > div.container.u-foreground.u-maxWidth1032.u-paddingTop40 > div > div > div > div.col.u-size8of12.u-sm-size12of12 > div.js-tagStream > div > div > div > div:nth-child(2) > a'
    )
    my_titles = soup.select(
        'div.section-content > div > h3'
    )
    my_content = soup.select(
        'div.section-content > div > h4'
    )

    titles = []
    for title in my_titles:
        titles.append(title.text.strip())

    links = []
    for link in my_links:
        links.append(link.get('href'))

    contents = []
    for content in my_content:
        contents.append(content.text.strip())

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '쿠팡',
            tech = 'AI'
        ).save()

    return


# 쿠팡 크롤링 (BE)
def coupang_crawling_BE():
    req = requests.get('https://medium.com/coupang-engineering/tagged/infrastructure')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select(
        'div > div.container.u-foreground.u-maxWidth1032.u-paddingTop40 > div > div > div > div.col.u-size8of12.u-sm-size12of12 > div.js-tagStream > div > div > div > div:nth-child(2) > a'
    )
    my_titles = soup.select(
        'div.section-content > div > h3'
    )
    my_content = soup.select(
        'div.section-content > div > h4'
    )

    titles = []
    for title in my_titles:
        titles.append(title.text.strip())

    links = []
    for link in my_links:
        links.append(link.get('href'))

    contents = []
    for content in my_content:
        contents.append(content.text.strip())

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '쿠팡',
            tech = 'BE'
        ).save()

    return

# 우아한 형제들 크롤링 (BE)
def woowahan_crawling_BE():
    links = []
    titles = []
    contents = []

    # BE 5개
    req = requests.get('https://techblog.woowahan.com/?s=%EC%82%AC%EC%9E%A5%EB%8B%98%EC%9A%A9')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div.item > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div.item > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div.item > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=%EC%9A%B0%EB%8B%B9%ED%83%95%ED%83%95')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=%EC%8B%A0%EC%9E%85+%EB%B0%B1%EC%97%94%EB%93%9C')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=%ED%9A%8C%EC%9B%90%EC%8B%9C%EC%8A%A4%ED%85%9C')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=%EC%8B%A4%EC%8B%9C%EA%B0%84')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '우아한형제들',
            tech = 'BE'
        ).save()
    
    return

# 우아한 형제들 크롤링 (FE)
def woowahan_crawling_FE():
    links = []
    titles = []
    contents = []

    # FE 5개
    req = requests.get('https://techblog.woowahan.com/?s=%EB%8B%A8%EC%9C%84+%ED%85%8C%EC%8A%A4%ED%8A%B8')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=%EB%82%98%EC%9D%98')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=%EB%A7%8C%EB%93%A4%EC%96%B4+%EA%B0%80%EB%A9%B0')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=react')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    req = requests.get('https://techblog.woowahan.com/?s=yarn')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_links = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a'
    )
    my_titles = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > h1'
    )
    my_content = soup.select_one(
        'body > div.content.vuejs > div.content-wrap > div > div:nth-child(1) > a > p:nth-child(3)'
    )
    links.append(my_links.get('href'))
    titles.append(my_titles.text.strip())
    contents.append(my_content.text.strip())

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '우아한형제들',
            tech = 'FE'
        ).save()
    
    return

# 라인 크롤링 (클라우드)
def line_crawling_cloud():
    req = requests.get('https://engineering.linecorp.com/ko/blog/tag/Cloud/Infra')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    url = 'https://engineering.linecorp.com'
    my_links = soup.select_one(
        '#contents > div > div > ul > li:nth-child(1) > h2 > a'
    )
    my_contents = soup.select_one(
        '#contents > div > div > ul > li:nth-child(1) > p > a > span'
    )

    links = []
    links.append(url + my_links.get('href'))
    titles = []
    titles.append(my_links.text.strip())
    contents = []
    my_contents = my_contents.text.strip()[:100].replace('\xa0',' ')
    contents.append(my_contents + "...")

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '라인',
            tech = '클라우드'
        ).save()

    return


# 라인 크롤링 (FE)
def line_crawling_FE():
    req = requests.get('https://engineering.linecorp.com/ko/blog/tag/Web%20Development')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    url = 'https://engineering.linecorp.com'
    my_links = soup.select(
        '#contents > div > div > ul > li > h2 > a'
    )
    my_contents = soup.select(
        '#contents > div > div > ul > li > p > a > span'
    )
    links = []
    for link in my_links[:6]:
        links.append(url + link.get('href'))
    titles = []
    for title in my_links[:6]:
        titles.append(title.text.strip())
    contents = []
    for content in my_contents[:6]:
        content = content.text[:100].replace('\xa0',' ').strip() 
        contents.append(content + '...')

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '라인',
            tech = 'FE'
        ).save()

    return


# 라인 크롤링 (BE)
def line_crawling_BE():
    req = requests.get('https://engineering.linecorp.com/ko/blog/tag/Server-side')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    url = 'https://engineering.linecorp.com'
    my_links = soup.select(
        '#contents > div > div > ul > li > h2 > a'
    )
    my_contents = soup.select(
        '#contents > div > div > ul > li > p > a > span'
    )
    links = []
    for link in my_links[:4]:
        links.append(url + link.get('href'))
    titles = []
    for title in my_links[:4]:
        titles.append(title.text.strip())
    contents = []
    for content in my_contents[:4]:
        content = content.text[:100].replace('\xa0',' ').replace('\n', '').strip() 
        contents.append(content + '...')

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '라인',
            tech = 'BE'
        ).save()

    return


# 토스 크롤링 (FE)
def toss_crawling_FE():
    req = requests.get('https://toss.tech/tech')
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    url = 'https://toss.tech'
    my_links = soup.select(
        '#__next > div.p-container.p-container--default.css-1n6tk1w > div > div > ul > a'
    )
    my_titles = soup.select(
        '#__next > div.p-container.p-container--default.css-1n6tk1w > div > div > ul > a > div > span.typography.typography--h3.typography--bold.color--grey800.css-ad3vzk.e3wfjt74'
    )
    my_contents = soup.select(
        '#__next > div.p-container.p-container--default.css-1n6tk1w > div > div > ul > a > div > span.typography.typography--h7.typography--medium.color--grey700.css-1kw8fmk.e3wfjt71'
    )
    links = []
    for link in my_links:
        links.append(url + link.get('href'))
    titles = []
    for title in my_titles:
        titles.append(title.text.strip())
    contents = []
    for content in my_contents:
        contents.append(content.text.strip())

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '토스',
            tech = 'FE'
        ).save()

    return

# 사용하려면 커맨드창에서 'python parser.py' 입력
if __name__=='__main__':
    kakao_crawling_ai()
    kakao_crawling_cloud()
    kakao_crawling_FE()
    kakao_crawling_BE()
    coupang_crawling_ai()
    coupang_crawling_BE()
    woowahan_crawling_BE()
    woowahan_crawling_FE()
    line_crawling_cloud()
    line_crawling_FE()
    line_crawling_BE()
    toss_crawling_FE()
