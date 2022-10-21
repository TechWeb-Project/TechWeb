from django.shortcuts import render, redirect
from .models import Article, Tech, Company

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail_tech(request, tech_pk):
    tech = Tech.objects.get(pk=tech_pk)
    articles = tech.article()
    context = {
        'tech': tech,
        'articles': articles,
    }
    return render(request, 'articles/detail.html', context)


def detail_company(request, company_pk):
    company = Tech.objects.get(pk=company_pk)
    articles = company.article()
    context = {
        'company': company,
        'articles': articles,
    }
    return render(request, 'articles/detail.html', context)

