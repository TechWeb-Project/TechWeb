import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_crawl_web_pjt.settings")
import django
django.setup()
from crawling.models import crawlingData



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

    # crawlingData(
    #     title=titles,
    #     content=contents,
    #     link=links,
    #     company = 'nhn',
    #     tech = '클라우드'
    # ).save()


    return

if __name__=='__main__':
    nhn_crawling_cloud()


