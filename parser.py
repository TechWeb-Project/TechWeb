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


# 당근 크롤링 (AI)
def daangn_crawling_ai():
    req = requests.get('https://medium.com/daangn/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8%EB%A1%9C-%EB%8F%99%EB%84%A4%EC%83%9D%ED%99%9C-%EC%8B%A0%EA%B3%A0-%EC%97%85%EB%AC%B4-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0-3b96608960')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links = ['https://medium.com/daangn/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8%EB%A1%9C-%EB%8F%99%EB%84%A4%EC%83%9D%ED%99%9C-%EC%8B%A0%EA%B3%A0-%EC%97%85%EB%AC%B4-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0-3b96608960']
    titles = []
    titles.append(my_titles.text.strip())
    contents = []
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/kubeflow-%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8-%EC%9A%B4%EC%9A%A9%ED%95%98%EA%B8%B0-6c6d7bc98c30')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/kubeflow-%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8-%EC%9A%B4%EC%9A%A9%ED%95%98%EA%B8%B0-6c6d7bc98c30')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/%EA%B8%80%EC%93%B0%EA%B8%B0-%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-cbbcc43e1f7f')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/%EA%B8%80%EC%93%B0%EA%B8%B0-%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-cbbcc43e1f7f')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/%EB%94%A5%EB%9F%AC%EB%8B%9D-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-in-production-fa623877e56a')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/%EB%94%A5%EB%9F%AC%EB%8B%9D-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-in-production-fa623877e56a')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')


    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '당근',
            tech = 'AI'
        ).save()

    return

# 당근 크롤링 (FE)
def daangn_crawling_FE():
    req = requests.get('https://medium.com/daangn/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93%EC%97%90-%EC%9B%B9-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-1-%ED%8C%8C%EC%9D%BC-%EA%B8%B0%EB%B0%98-%EC%9B%B9%EB%B7%B0-d312b17e697c')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links = ['https://medium.com/daangn/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93%EC%97%90-%EC%9B%B9-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-1-%ED%8C%8C%EC%9D%BC-%EA%B8%B0%EB%B0%98-%EC%9B%B9%EB%B7%B0-d312b17e697c']
    titles = []
    titles.append(my_titles.text.strip())
    contents = []
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93%EC%97%90-%EC%9B%B9-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-2-%EC%9B%B9-%EC%84%9C%EB%B2%84%EB%A1%9C-%EB%8F%8C%EC%95%84%EA%B0%80%EA%B8%B0-3030daea456c')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93%EC%97%90-%EC%9B%B9-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-2-%EC%9B%B9-%EC%84%9C%EB%B2%84%EB%A1%9C-%EB%8F%8C%EC%95%84%EA%B0%80%EA%B8%B0-3030daea456c')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')

    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '당근',
            tech = 'FE'
        ).save()

    return


# 당근 크롤링 (BE)
def daangn_crawling_BE():
    req = requests.get('https://medium.com/daangn/lambda-edge%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-on-the-fly-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%A6%AC%EC%82%AC%EC%9D%B4%EC%A7%95-f4e5052d49f3')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links = ['https://medium.com/daangn/lambda-edge%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-on-the-fly-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%A6%AC%EC%82%AC%EC%9D%B4%EC%A7%95-f4e5052d49f3']
    titles = []
    titles.append(my_titles.text.strip())
    contents = []
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%99%80-%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94-%ED%94%BC%EB%93%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%84%A4%EA%B3%84%ED%95%98%EA%B8%B0-6c5a5aa2b11f')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%99%80-%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94-%ED%94%BC%EB%93%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%84%A4%EA%B3%84%ED%95%98%EA%B8%B0-6c5a5aa2b11f')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/memory-allocator-for-mongodb-1953f9cee06c')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/memory-allocator-for-mongodb-1953f9cee06c')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/mysql-online-ddl-faf47439084c')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/mysql-online-ddl-faf47439084c')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/%EC%98%88%EC%B8%A1-%EA%B0%80%EB%8A%A5%ED%95%9C-%EB%8C%80%EA%B7%9C%EB%AA%A8-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-a33e2f3cef88')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/%EC%98%88%EC%B8%A1-%EA%B0%80%EB%8A%A5%ED%95%9C-%EB%8C%80%EA%B7%9C%EB%AA%A8-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-a33e2f3cef88')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')

    req = requests.get('https://medium.com/daangn/dynamodb-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B3%80%EA%B2%BD-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-feat-kinesis-1733db06066')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > div > h1'
    )
    my_contents = soup.select_one(
        '#root > div > div.l.c > div > div > main > div > div.gb.gc.gd.ge.gf.l > div:nth-child(1) > div > article > div > div:nth-child(2) > section > div > div:nth-child(2) > p'
    )
    links.append('https://medium.com/daangn/dynamodb-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B3%80%EA%B2%BD-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-feat-kinesis-1733db06066')
    titles.append(my_titles.text.strip())
    contents.append(my_contents.text.strip()[:120] + '...')


    for item in zip(titles, contents, links):
        crawlingData(
            title=item[0],
            content=item[1],
            link=item[2],
            company = '당근',
            tech = 'BE'
        ).save()

    return

# NHN 크롤링 (AI)
def nhn_crawling_ai():
    links = []
    posts_list = [299, 303, 280]
    url = 'https://meetup.toast.com/posts/'
    for post in posts_list:
        links.append(url + str(post))
    titles = ['AI Fashion 서비스 소개', 'Vehicle Plate Recognizer 서비스 소개', 'Face Recognition 서비스 소개']
    contents = [
        'AI Fashion은 다양한 카테고리 상품 데이터를 학습하여 패션 분야에 특화된 서비스를 제공합니다. 상품명이나 속성을 몰라도 이미지만으로 쉽고 빠르게 유사한 상품을 검색할 수 있어서...',
        'Vehicle Plate Recognizer는 NHN Cloud의 OCR(광학 문자 인식) 기술을 활용한 두 번째 상품입니다. 머신러닝을 통해 차량 번호판 인식 기능을 학습하였으며, 이미지의 번호판 영역을...',
        '얼굴 인식(Face Recognition) 기술은 컴퓨터 비전(Computer Vision)의 주요 분야로 기계학습(Machine Learning)을 이용해 시스템에 입력된 이미지 속 인물이 내부 데이터베이스(DB)에 미리...'
    ]

    for i in range(len(links)):
        crawlingData(
            title=titles[i],
            content=contents[i],
            link=links[i],
            company = 'nhn',
            tech = 'AI'
        ).save()


    return


# NHN 크롤링 (BE)
def nhn_crawling_BE():
    links = []
    posts_list = [288, 277]
    url = 'https://meetup.toast.com/posts/'
    for post in posts_list:
        links.append(url + str(post))
    titles = ['Terraform: IaC의 단짝', 'Docker Compose와 버전별 특징']
    contents = [
        '훌륭한 IaC(Infrastructure as Code) 도구인 Terraform을 사용하여 NHN Cloud의 리소스(서버 인스턴스 등)를 만들고 변경하고 제거하는 예제를 정리해보았습니다.',
        'Docker Compose란? 무엇일까요. 많은 곳에서 Docker Compose를 검색한다면 다음과 같은 설명을 많이 접할 수 있습니다.'
    ]

    for i in range(len(links)):
        crawlingData(
            title=titles[i],
            content=contents[i],
            link=links[i],
            company = 'nhn',
            tech = 'BE'
        ).save()

    return


# NHN 크롤링 (FE)
def nhn_crawling_FE():
    links = []
    posts_list = [326, 174, 178, 180, 191]
    url = 'https://meetup.toast.com/posts/'
    for post in posts_list:
        links.append(url + str(post))
    titles = [
        'SolidJS와 함께 되짚어보는 반응형 프로그래밍', 
        '실용적인 프론트엔드 테스트 전략 (1)',
        '실용적인 프론트엔드 테스트 전략 (2)',
        '실용적인 프론트엔드 테스트 전략 (3)',
        'Expo Web(React Native for web) 튜토리얼'
        ]
    contents = [
        '최근 몇 년 사이 반응형 프로그래밍(Reactive Programming)이라는 개념이 웹 프런트엔드 개발 분야에 많이 스며들었다. Vue.js가 대표적으로 반응형 프레임워크로 알려져있으며, 최근에는 Svelte가 많이 언급되고 있다.',
        '바야흐로 자바스크립트의 시대이다. 최근 2~3년 동안 자바스크립트는 가장 인기있는 언어 순위 1위를 유지하고 있고, 여전히 빠른 속도로 성장하고 있다. 10여년 전, 웹 표준이라는 개념조차...',
        '1부에서는 테스트 자동화와 테스트 전략의 중요성, 시각적 테스트를 자동화하는 것이 어려운 이유 등을 살펴보았다. 사실 시각적 테스트를 자동화하는 것이 불가능하지는 않지만 ...',
        '2부에서는 스토리북을 사용해서 시각적 요소에 대한 테스트를 자동화하는 방법에 대해 알아보았다. 기억을 되살리기 위해 우리가 작성하고 있는 할 일 관리 애플리케이션의 실행 단계를...',
        'React Native는 자바스크립트 프레임워크인 React로 개발하며 네이티브 앱(iOS와 안드로이드)을 만들어주는 프레임워크이다.'
    ]

    for i in range(len(links)):
        crawlingData(
            title=titles[i],
            content=contents[i],
            link=links[i],
            company = 'nhn',
            tech = 'FE'
        ).save()


    return


# NHN 크롤링 (클라우드)
def nhn_crawling_cloud():
    links = []
    posts_list = [272, 269, 313, 314]
    url = 'https://meetup.toast.com/posts/'
    for post in posts_list:
        links.append(url + str(post))
    titles = [
        'Security Compliance 서비스 소개', 
        'PostgreSQL Instance 서비스 소개',
        'Speech to Text 서비스 소개',
        'Text to Speech 서비스 소개',
        ]
    contents = [
        'Security Compliance 서비스는 정보보호 인증과 컴플라이언스에 효과적으로 대응할 수 있도록 정보보호 인증서와 상세 가이드를 제공하는 서비스입니다.',
        'postgresql.org 공식 사이트에 방문하면 다음과 같이 표현되어 있습니다. "세상에서 가장 진보된 오픈소스 관계형 데이터베이스"',
        'Speech to Text는 NHN Cloud의 음성 인식 및 문자 합성 기술을 통해, 입력된 음성을 인식하고, 인식된 음성을 텍스트로 변환하여 제공합니다.',
        'Text to Speech는 NHN Cloud의 문자 인식 및 음성 합성 기술을 통해, 입력된 텍스트를 인식하고 인식된 문자를 자연스러운 음성으로 합성하여 제공합니다.',
    ]

    for i in range(len(links)):
        crawlingData(
            title=titles[i],
            content=contents[i],
            link=links[i],
            company = 'nhn',
            tech = '클라우드'
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
    daangn_crawling_ai()
    daangn_crawling_FE()
    daangn_crawling_BE()
    nhn_crawling_ai()
    nhn_crawling_BE()
    nhn_crawling_FE()
    nhn_crawling_cloud()

