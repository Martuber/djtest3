from django.shortcuts import render
from .models import  *

# Create your views here.

def index(request):
    # 查询金庸作品书籍
    book_by_jy = BookInfo.original_manager.filter(author="金庸")

    # 查询所有倚天屠龙记中的英雄人物
    heroes_in_yitian = HeroInfo.manager.filter(hero_book__title="倚天屠龙记")

    # 查询英雄名为 “郭靖”的图书

    book_contain_xz = BookInfo.manager.filter(heroinfo__hero_name__contains="小朱")

    bookslist = {"books": book_by_jy, "heroes_in_yitian": heroes_in_yitian,
                 "book_contain_xz":book_contain_xz}
    return render(request, template_name="booktest/index.html", context=bookslist)
