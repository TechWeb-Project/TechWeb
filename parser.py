import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_crawl_web_pjt.settings")
import django
django.setup()
from crawling.models import crawlingData

# 임시로 만든 카카오 기술블로그에서 글 하나 크롤링하는 로직
def crawling():
    req = requests.get('https://tech.kakao.com/tag/ai/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'body > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-4239a3ca.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div.elementor-column.elementor-col-66.elementor-top-column.elementor-element.elementor-element-25119388 > div > div > div.elementor-element.elementor-element-5cd2e69.elementor-grid-1.elementor-posts--thumbnail-none.elementor-grid-tablet-2.elementor-grid-mobile-1.elementor-widget.elementor-widget-archive-posts > div > div.elementor-posts-container.elementor-posts.elementor-posts--skin-classic.elementor-grid > article.elementor-post.elementor-grid-item.post-18816.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-blog.category-career.tag-2022_data.tag-ai.tag-algorithm-ml.tag-algorithm-ranking.tag-career.tag-machine-learning.tag-recommendation-system.tag-recruitment.tag-statistics-analysis.tag-tech > div > h3 > a'
        )
    my_contents = soup.select(
        'body > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-4239a3ca.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div.elementor-column.elementor-col-66.elementor-top-column.elementor-element.elementor-element-25119388 > div > div > div.elementor-element.elementor-element-5cd2e69.elementor-grid-1.elementor-posts--thumbnail-none.elementor-grid-tablet-2.elementor-grid-mobile-1.elementor-widget.elementor-widget-archive-posts > div > div.elementor-posts-container.elementor-posts.elementor-posts--skin-classic.elementor-grid > article.elementor-post.elementor-grid-item.post-18816.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-blog.category-career.tag-2022_data.tag-ai.tag-algorithm-ml.tag-algorithm-ranking.tag-career.tag-machine-learning.tag-recommendation-system.tag-recruitment.tag-statistics-analysis.tag-tech > div > div.elementor-post__excerpt > p'
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
        ).save()

    return

# 사용하려면 커맨드창에서 'python parser.py' 입력
if __name__=='__main__':
    crawling()
